import os
from extract_solution import extract_solution

llm_response = '''
The IndexError occurs because there are cases where word_idx (an index corresponding to a tokenized word) is greater than or equal to the length of label. This happens because word_ids is always as long as the tokenized sequence, while label may have fewer entries than word_ids due to the truncation or padding applied to the text. You can fix this by checking the bounds of word_idx before accessing label.

Here’s the corrected function:

from transformers import AutoTokenizer

def p(texts, labels, max_length=512):
    """
    Tokenize the input text with truncation and padding, then align it
    with the provided labels. If the word index exceeds the label length,
    append -100 to ensure it is ignored by the loss function.

    Args:
        texts (list): A list of tokens or tokenized sentences.
        labels (list): A list of corresponding labels for each token in texts.
        max_length (int, optional): The max sequence length. Defaults to 512.

    Returns:
        dict: The tokenized encodings dictionary containing aligned labels.
    """
    # Tokenize the input text with truncation and padding
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    encodings = tokenizer(
        texts,
        is_split_into_words=True,
        return_offsets_mapping=True,
        padding=True,
        truncation=True,
        max_length=max_length)

    encoded_labels = []

    for i, label in enumerate(labels):
        word_ids = encodings.word_ids(batch_index=i)  # Map tokens to words
        label_ids = []
        previous_word_idx = None

        # Truncate word_ids to max_length
        word_ids = word_ids[:max_length]

        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)  # Ignored by the loss function
            elif word_idx != previous_word_idx:  # First token of the word
                # Ensure index does not go out of range
                if word_idx < len(label):
                    label_ids.append(label[word_idx])
                else:
                    label_ids.append(-100)  # If label is out of range
            else:
                label_ids.append(-100)  # Assign -100 to subword tokens
            previous_word_idx = word_idx

        # Handle cases where label_ids might not align with word_ids
        if len(label_ids) < max_length:
            label_ids += [-100] * (max_length - len(label_ids))

        encoded_labels.append(label_ids)

    # Add the aligned labels to the tokenized encodings
    encodings['labels'] = encoded_labels
    return encodings

Key Changes:
        1.        Bounds Check: Before accessing label[word_idx], ensure that word_idx < len(label). If word_idx exceeds the length of label, append -100.
        2.        Consistent Label Length: Ensure that label_ids matches the length of word_ids by padding it with -100 as necessary.

Explanation:
        •        The word_ids array can have more elements than label due to tokenization and padding.
        •        By adding a boundary check, we prevent accessing out-of-range indices in label.
        •        -100 is added for any mismatched lengths to ensure the model ignores these tokens during training.

This should resolve the IndexError.
'''

try:
    response = extract_solution(llm_response=llm_response)
    if not isinstance(response, list):
        raise ValueError(
            "Expected response to be a list of (file_name, code) tuples."
        )

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists
        if not os.path.isfile(file_name):
            raise FileNotFoundError(
                f"The file '{file_name}' does not exist. "
                "Please check the path."
            )

        # Proceed to write only if the file already exists
        with open(file_name, "w") as file:
            file.write(code)
        print(f"File '{file_name}' written successfully.")
        break


except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")
