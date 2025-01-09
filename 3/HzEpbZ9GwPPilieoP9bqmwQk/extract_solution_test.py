import os

from extract_solution import extract_solution

llm_response = '''
```python
def process_string(input_string: str, target_letter: str) -> dict:
    """
    Arranges words in a string alphabetically, then returns a dictionary where keys are words
    starting with a given letter and values are lists of indices where these words appear
    in the sorted list of words.
    """
    words = input_string.lower().split()
    words.sort()

    result = {}
    for i, word in enumerate(words):
        if word.startswith(target_letter.lower()):
            if word not in result:
                result[word] = []
            result[word].append(i)

    return result
```
'''

try:

    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):

        raise ValueError("Expected response to be a list of (file_name, code) tuples.")

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:

            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists

        if not os.path.isfile(file_name):

            raise FileNotFoundError(

                f"The file '{file_name}' does not exist. Please check the path."

            )

        # Proceed to write only if the file already exists

        with open(file_name, "w") as file:

            file.write(code)

        print(f"File '{file_name}' written successfully.")

except FileNotFoundError as fnf_error:

    print(f"File error: {fnf_error}")

except Exception as e:

    print(f"An error occurred while running extract solution test: {e}")