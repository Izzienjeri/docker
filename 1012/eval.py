"""Unit tests for the find_number_of_lis function."""

import unittest
from solution import find_number_of_lis


class TestFindNumberOfLIS(unittest.TestCase):
    """Test cases for the find_number_of_lis function."""

    def test_basic_case(self):
        """Test with a basic case of multiple increasing subsequences."""
        nums = [1, 3, 2, 4, 5]
        self.assertEqual(find_number_of_lis(nums), 2, "Failed on basic case")

    def test_empty_input(self):
        """Test with an empty input list."""
        nums = []
        self.assertEqual(find_number_of_lis(nums), 0, "Failed on empty input")

    def test_all_numbers_decreasing(self):
        """Test with all numbers in decreasing order."""
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(find_number_of_lis(nums), 5,
                         "Failed on all numbers decreasing")

    def test_all_numbers_equal(self):
        """Test with all numbers being equal."""
        nums = [3, 3, 3, 3, 3]
        self.assertEqual(find_number_of_lis(nums), 5,
                         "Failed on all numbers equal")


if __name__ == "__main__":
    unittest.main()
