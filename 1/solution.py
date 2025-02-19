"""This file contains the golden solution of 1182."""
import string

def read_book(filename):
    """Read a text file and returns a list of words."""
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    words = text.split()
    return words

def clean_word(word):
    """Clean a word by removing punctuation and converting to lowercase."""
    word = word.strip(string.punctuation)
    return word.lower()

if __name__ == "__main__":
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
