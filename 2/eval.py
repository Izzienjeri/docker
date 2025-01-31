import unittest
import random
from solution import find_duplicates

# Unit Tests
def find_duplicates_verify(arr):
    counts = {}
    duplicates = []
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    for num, count in counts.items():
        if count > 1:
            duplicates.append(num)
    return sorted(duplicates)

class TestFindDuplicates(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_duplicates([]), [])

    def test_no_duplicates(self):
        self.assertEqual(find_duplicates([1, 2, 3, 4, 5]), [])

    def test_single_duplicate(self):
        self.assertEqual(find_duplicates([1, 2, 3, 4, 2]), [2])

    def test_multiple_duplicates(self):
        self.assertEqual(find_duplicates([1, 2, 2, 3, 4, 4, 5]), [2,4])

    def test_multiple_duplicates_out_of_order(self):
        self.assertEqual(find_duplicates([4, 2, 2, 1, 4, 1, 3, 4, 2, 4]), [1,2,4])

    def test_negative_numbers(self):
        self.assertEqual(find_duplicates([-1, -2, -2, 0, 1, 1]), [-2, 1])

    def test_large_list_with_duplicates(self):
        data = [random.randint(1, 1000) for _ in range(10000)] + [random.randint(1, 1000) for _ in range(500)]
        correct = find_duplicates_verify(data)
        self.assertEqual(find_duplicates(data), correct)

    def test_zero_and_duplicates(self):
        self.assertEqual(find_duplicates([0, 1, 2, 3, 0]), [0])

    def test_only_duplicates(self):
        self.assertEqual(find_duplicates([2, 2, 2, 2, 2]), [2])

# Run the tests
if __name__ == '__main__':
    unittest.main()
