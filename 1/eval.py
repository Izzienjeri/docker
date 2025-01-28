import unittest
import random
from solution import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_one_element_list(self):
        self.assertEqual(bubble_sort([5]), [5])

    def test_already_sorted_list(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_reverse_sorted_list(self):
        self.assertEqual(bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_list_with_duplicate_elements(self):
        self.assertEqual(bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_list_with_negative_numbers(self):
        self.assertEqual(bubble_sort([-5, -2, 0, 3, -1, 4, 8, -6, 2, 5]), [-6, -5, -2, -1, 0, 2, 3, 4, 5, 8])

    def test_large_random_list(self):
        large_list = [random.randint(-1000, 1000) for _ in range(1000)]
        expected_output = sorted(large_list)
        actual_output = bubble_sort(large_list.copy()) 
        self.assertEqual(actual_output, expected_output)

    def test_ten_identical_elements(self):
        self.assertEqual(bubble_sort([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]), [5, 5, 5, 5, 5, 5, 5, 5, 5, 5])

if __name__ == '__main__':
    unittest.main()