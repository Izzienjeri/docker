import unittest
from solution import parse_and_convert

class TestNumberPairsParser(unittest.TestCase):
    """A test suite for verifying the parse_and_convert function."""

    def test_empty_string(self):
        """Test to handle an empty string input."""
        self.assertEqual(parse_and_convert(""), [])

    def test_multiple_pairs(self):
        """Test to parse multiple consecutive number pairs."""
        self.assertEqual(parse_and_convert("1 2 3 4 5 6"), [(1, 2), (3, 4), (5, 6)])

    def test_newline_separator(self):
        """Test to handle newline characters as separators, ensuring new pairs start after a newline."""
        self.assertEqual(parse_and_convert("1 2\n3 4"), [(1, 2), (3, 4)])

    def test_mixed_separators(self):
        """Test to handle mixed spaces and newlines correctly."""
        self.assertEqual(parse_and_convert("1 2 3\n4 5 6\n7 8"), [(1, 2), (3, 4), (5, 6), (7, 8)])

    def test_negative_numbers(self):
        """Test to handle negative numbers correctly."""
        self.assertEqual(parse_and_convert("-1 2 -3 -4"), [(-1, 2), (-3, -4)])

    def test_extra_spaces(self):
        """Test to handle additional whitespace between numbers."""
        self.assertEqual(parse_and_convert("1  2\n 4 5"), [(1, 2), (4, 5)])

    def test_trailing_newline(self):
        """Test to handle cases where the input ends with a newline."""
        self.assertEqual(parse_and_convert("1 2\n"), [(1, 2)])

    def test_ignore_single_number(self):
        """Test to ensure single numbers without a pair are ignored."""
        self.assertEqual(parse_and_convert("1 20 30"), [(1, 20)])

if __name__ == '__main__':
    unittest.main()
