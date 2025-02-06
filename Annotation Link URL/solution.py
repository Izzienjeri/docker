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
