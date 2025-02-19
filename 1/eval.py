"""This file contains the tests of the golden solution."""
import os
import unittest
from solution import clean_word, read_book

class TestTextProcessing(unittest.TestCase):
    """Unit tests for text processing functions."""

    def test_basic_punctuation_removal(self):
        """Test with basic punctuation at the end."""
        words = ["hello!", "world,", "test.", "example?", "clean"]
        expected = ['hello', 'world', 'test', 'example', 'clean']
        cleaned_words = [clean_word(word) for word in words]
        self.assertEqual(cleaned_words, expected)

    def test_no_punctuation(self):
        """Test with no punctuation."""
        words = ["hello", "world", "test", "example", "clean"]
        expected = ['hello', 'world', 'test', 'example', 'clean']
        cleaned_words = [clean_word(word) for word in words]
        self.assertEqual(cleaned_words, expected)

    def test_words_with_only_punctuation(self):
        """Test with only punctuation."""
        words = ["!", ",", ".", "?"]
        expected = ['', '', '', '']
        cleaned_words = [clean_word(word) for word in words]
        self.assertEqual(cleaned_words, expected)

    def test_mixed_punctuation_start_end(self):
        """Test with mixed punctuation at start and end."""
        words = ["!hello", "world!", ",test.", "?example"]
        expected = ['hello', 'world', 'test', 'example']
        cleaned_words = [clean_word(word) for word in words]
        self.assertEqual(cleaned_words, expected)

    def test_empty_word_list(self):
        """Test with an empty list of words."""
        words = []
        expected = []
        cleaned_words = [clean_word(word) for word in words]
        self.assertEqual(cleaned_words, expected)

    def test_words_with_hyphens_apostrophes(self):
        """Test words with hyphens and apostrophes."""
        words = ["hello-world", "it's", "test-case"]
        expected = ['hello-world', "it's", 'test-case']
        cleaned_words = [clean_word(word) for word in words]
        self.assertEqual(cleaned_words, expected)

    def test_words_with_repeated_punctuation(self):
        """Test words with repeated punctuation."""
        words = ["!!hello!!", ",,world,,", "..test..", "??example??"]
        expected = ['hello', 'world', 'test', 'example']
        cleaned_words = [clean_word(word) for word in words]
        self.assertEqual(cleaned_words, expected)

    def test_words_with_embedded_punctuation(self):
        """Test words with embedded punctuation."""
        words = ["he!llo", "wo,rld", "te.st", "ex?ample"]
        expected = ['he!llo', 'wo,rld', 'te.st', 'ex?ample']
        cleaned_words = [clean_word(word) for word in words]
        self.assertEqual(cleaned_words, expected)

    def test_words_with_all_numbers(self):
        """Test words with only numbers."""
        words = ["1", "2", "3", "4"]
        expected = ['1', '2', '3', '4']
        cleaned_words = [clean_word(word) for word in words]
        self.assertEqual(cleaned_words, expected)

    def test_words_with_alphanumeric_number(self):
        """Test words with alphanumeric and numbers."""
        words = ["hello1", "2world"]
        expected = ['hello1', '2world']
        cleaned_words = [clean_word(word) for word in words]
        self.assertEqual(cleaned_words, expected)

    def test_words_with_special_characters(self):
        """Test words with special characters."""
        words = ["#$%", "%^&$"]
        expected = ['', '']
        cleaned_words = [clean_word(word) for word in words]
        self.assertEqual(cleaned_words, expected)


class TestFileProcessing(unittest.TestCase):
    """Unit tests for the file processing function."""

    def setUp(self):
        """Set up for test methods."""
        self.test_file = "test_book.txt"
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("This is a test. It has multiple lines.\nAnd some words.")

    def tearDown(self):
        """Tear down for test methods."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_book_valid_file(self):
        """Test reading a valid file."""
        expected_words = [
            "This", "is", "a", "test.", "It", "has", "multiple",
            "lines.", "And", "some", "words."
        ]
        actual_words = read_book(self.test_file)
        self.assertEqual(actual_words, expected_words)

    def test_read_book_empty_file(self):
        """Test reading an empty file."""
        empty_file = "empty_book.txt"
        open(empty_file, 'w').close()  # Create an empty file
        self.addCleanup(os.remove, empty_file)  # Clean up after test
        words = read_book(empty_file)
        self.assertEqual(words, [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
