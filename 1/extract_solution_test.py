import os
import json
from extract_solution import extract_solution

llm_response = '''
The error "NameError: name 'string' is not defined" occurs because you're using the `string` module without importing it first.  Here's the corrected and complete code:

```python
import string

def read_book(filename):
  """Reads a text file and returns a list of words."""

  with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

  words = text.split()
  return words

def clean_word(word):
  """Cleans a word by removing punctuation and converting to lowercase."""

  word = word.strip(string.punctuation)
  return word.lower()


# Example Usage:
filename = 'your_book.txt'  # Replace with the actual filename

try:
    words = read_book(filename)
    clean_words = [clean_word(word) for word in words]

    # You can now process the 'clean_words' list
    # For example, print the first 20 cleaned words:
    print(clean_words[:20])

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.  Make sure the file exists and the filename is correct.")
except Exception as e:
    print(f"An error occurred: {e}")
```

**Before running:**

1. **Make sure you have a file named `your_book.txt` (or whatever you named it) in the same directory as your Python script.**  You need to download a book from Project Gutenberg (or a similar source) and save it as a text file.
2. **Replace `'your_book.txt'` in the code above with the actual filename of your downloaded book.**

**Key change:**  The line `import string` has been added at the beginning of the script.  This imports the necessary module so that `string.punctuation` is defined and accessible within the `clean_word` function. I've also included error handling to make the script more robust.
'''

try:
    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):
        raise ValueError("Expected response to be a list of (file_name, code) tuples.")

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Proceed to write only if the file already exists
        with open(file_name, "w") as file:
            file.write(code)

        print(f"File '{file_name}' written successfully.")
        break

except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")

