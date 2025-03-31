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


filename = 'data.txt'
words = read_book(filename)

clean_words = [clean_word(word) for word in words]

print(clean_words)