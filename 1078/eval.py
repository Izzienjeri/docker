"""Unit tests for the 'can_transform' function."""

import unittest
from solution import can_transform


class TestArrayTransform(unittest.TestCase):
    """Test cases for the can_transform function."""

    def test_case1_basic_transformation(self):
        """Test Case 1: Basic transformation possible."""
        self.assertEqual(can_transform([1, 2, 3], [2, 3, 4]), "YES 1")

    def test_case2_impossible_transformation(self):
        """Test Case 2: Impossible transformation."""
        self.assertEqual(can_transform([1, 2, 3], [2, 3, 5]), "NO 2")

    def test_case3_empty_arrays(self):
        """Test Case 3: Empty arrays."""
        self.assertEqual(can_transform([], []), "YES 0")

    def test_case4_single_element(self):
        """Test Case 4: Single element transformation."""
        self.assertEqual(can_transform([5], [10]), "YES 5")

    def test_case5_no_common_elements(self):
        """Test Case 5: Arrays with no common elements."""
        arr1 = [1, 2, 3, 7, 8, 9, 10, 11, 12, 13]
        arr2 = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        self.assertEqual(can_transform(arr1, arr2), "NO 0")

    def test_case6_multiple_varying_differences(self):
        """Test Case 6: Multiple varying differences within valid subarray."""
        arr1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        arr2 = [6, 7, 8, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(can_transform(arr1, arr2), "NO 8")

    def test_case7_different_lengths(self):
        """Test Case 7: Arrays of different lengths."""
        with self.assertRaises(ValueError):
            can_transform([1, 2, 3], [1, 2])

    def test_case8_restrictive_difference(self):
        """Test Case 8: Overly restrictive difference handling."""
        self.assertEqual(can_transform([1, 2, 3, 4, 5], [2, 3, 4, 6, 7]),
                         "NO 3")

    def test_case9_large_numbers(self):
        """Test Case 9: Edge case with large numbers."""
        arr1 = [1000000000, 1000000000, 1000000000]
        arr2 = [999999999, 999999999, 999999999]
        self.assertEqual(can_transform(arr1, arr2), "NO 0")

    def test_case10_out_of_range(self):
        """Test Case 10: Element out of valid range."""
        with self.assertRaises(ValueError):
            can_transform([1, 2, 3, 1000000001], [2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
