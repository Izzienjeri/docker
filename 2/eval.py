"""Unit tests for the evaluating a two-digit string according to the logic provided."""

import unittest
from solution import evaluate_string


class TestEvaluate_String(unittest.TestCase):
    """Tests for the evaluate_string function."""

    def test_valid_expected_true_first_condition(self):
        """Test for Valid Input - First digit > 4 and Second digit > 4."""
        result = evaluate_string("55")
        self.assertIsInstance(result, bool)
        self.assertTrue(result)

    def test_valid_expected_true_second_condition(self):
        """Test for Valid Input - First digit == 6."""
        result = evaluate_string("63")
        self.assertIsInstance(result, bool)
        self.assertTrue(result)

    def test_valid_expected_false(self):
        """Test for Valid Input - Neither condition met."""
        result = evaluate_string("33")
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

    def test_invalid_empty_string(self):
        """Test for Invalid Input - Empty String."""
        result = evaluate_string("")
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

    def test_invalid_single_digit(self):
        """Test for Invalid Input - Single Digit String."""
        result = evaluate_string("5")
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

    def test_invalid_more_than_two_digits(self):
        """Test for Invalid Input - More than Two Digits."""
        result = evaluate_string("555")
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

    def test_invalid_non_numeric(self):
        """Test for Invalid Input - Non-numeric String."""
        result = evaluate_string("ab")
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

    def test_valid_expected_false_first_condition_second_digit(self):
        """Test for Valid Input - First Digit > 4, Second Digit <=4."""
        result = evaluate_string("74")
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

    def test_valid_expected_false_first_condition_first_digit(self):
        """Test for Valid Input - First Digit <= 4, Second Digit > 4."""
        result = evaluate_string("45")
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

    def test_valid_expected_true_second_condition_higher(self):
        """Test for Valid Input - First Digit = 6 and Second Digit > 4."""
        result = evaluate_string("65")
        self.assertIsInstance(result, bool)
        self.assertTrue(result)

    def test_valid_expected_true_second_condition_lower(self):
        """Test for Valid Input - First Digit = 6 and Second Digit <= 4."""
        result = evaluate_string("64")
        self.assertIsInstance(result, bool)
        self.assertTrue(result)

    def test_invalid_special_characters(self):
        """Test for Invalid Input - Special Characters."""
        result = evaluate_string("!@")
        self.assertIsInstance(result, bool)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
