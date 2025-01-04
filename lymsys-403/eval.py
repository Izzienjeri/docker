import unittest
from solution import efficient_sort

class Test(unittest.TestCase):

    def test_small_dataset(self):
        self.assertEqual(efficient_sort([7, 3, 5, 2, 4, 6, 1]), "Insertion Sort")

    def test_nearly_sorted_data(self):
        self.assertEqual(efficient_sort([1, 2, 3, 4, 6, 5, 7, 8, 10, 9]), "Insertion Sort")

    def test_large_dataset_with_duplicates(self):
        self.assertEqual(efficient_sort([0, 1, 2, 0, 1, 2, 0, 1, 3, 2, 1, 0, 1, 2, 0, 1, 2, 0, 1, 3, 2, 1, 0, 1]), "3-way Quick sort")

    def test_large_dataset_no_duplicates(self):
        self.assertEqual(efficient_sort([45, 23, 89, 11, 77, 30, 50, 67, 22, 91, 43, 8, 60, 71, 34, 19, 25, 55, 12, 39, 80, 28]), "Quick sort")

    def test_small_dataset_with_duplicates(self):
        self.assertEqual(efficient_sort([3, 1, 2, 1, 2]), "Insertion Sort")
    
    def test_large_dataset_with_many_duplicates(self):
        self.assertEqual(efficient_sort([5, 3, 7, 3, 5, 8, 3, 6, 7, 3, 8, 5, 3, 9, 5, 3, 7, 3, 5, 8, 3, 8, 3, 6, 7, 3, 8, 5, 3, 9, 5, 3, 7, 3, 5, 8, 3]), "3-way Quick sort")

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            efficient_sort([])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            efficient_sort("not a list")

    def test_non_integer_elements(self):
        with self.assertRaises(ValueError):
            efficient_sort([1, 2, "a", 4])
    
    def test_large_dataset_nearly_sorted(self):
        self.assertEqual(efficient_sort([i for i in range(25)] + [24]), "Insertion Sort")


        