import unittest
from datetime import date
from typing import List
from math import log2, floor
from solution import binary_search_year


class TestBinarySearchYear(unittest.TestCase):
    def test_empty_list(self):
        """Test Case 1: Empty List"""
        dates: List[date] = []
        result = binary_search_year(dates, 2023)
        self.assertEqual(result, (False, 0))

    def test_single_date_year_present(self):
        """Test Case 2: Single date - Year Present"""
        dates = [date(2016, 1, 1)]
        found, calls = binary_search_year(dates, 2016)
        self.assertTrue(found)
        self.assertGreaterEqual(calls, 1)
        self.assertLessEqual(calls, 1)

    def test_single_date_year_not_present(self):
        """Test Case 3: Single date - Year Not Present"""
        dates = [date(2016, 1, 1)]
        found, calls = binary_search_year(dates, 2015)
        self.assertFalse(found)
        self.assertGreaterEqual(calls, 1)
        self.assertLessEqual(calls, 1)

    def test_multiple_dates_year_present(self):
        """Test Case 4: Multiple dates - Year Present"""
        dates = [
            date(2015, 6, 15),
            date(2016, 1, 1),
            date(2017, 12, 31)
        ]
        found, calls = binary_search_year(dates, 2016)
        self.assertTrue(found)
        self.assertGreaterEqual(calls, 1)
        self.assertLessEqual(calls, 2)

    def test_multiple_dates_year_not_present(self):
        """Test Case 5: Multiple dates - Year Not Present"""
        dates = [
            date(2015, 6, 15),
            date(2016, 1, 1),
            date(2017, 12, 31)
        ]
        found, calls = binary_search_year(dates, 2018)
        self.assertFalse(found)
        self.assertGreaterEqual(calls, 1)
        self.assertLessEqual(calls, 2)

    def test_unsorted_dates(self):
        """Test Case 6: Unsorted dates"""
        dates = [
            date(2017, 1, 1),
            date(2015, 1, 1),
            date(2016, 1, 1)
        ]
        found, calls = binary_search_year(dates, 2015)
        self.assertTrue(found)
        self.assertGreaterEqual(calls, 1)
        self.assertLessEqual(calls, 2)

    def test_multiple_dates_same_year(self):
        """Test Case 7: Multiple dates with Same Year"""
        dates = [
            date(2016, 1, 1),
            date(2016, 6, 15),
            date(2016, 12, 31)
        ]
        found, calls = binary_search_year(dates, 2016)
        self.assertTrue(found)
        self.assertGreaterEqual(calls, 1)
        self.assertLessEqual(calls, 2)

    def test_larger_dataset(self):
        """Test Case 8: Larger Dataset with Recursive Depth"""
        dates = [date(year, 1, 1) for year in range(2000, 2021)]
        found, calls = binary_search_year(dates, 2010)
        max_calls = floor(log2(len(dates))) + 1

        self.assertTrue(found)
        self.assertGreaterEqual(calls, 1)
        self.assertLessEqual(calls, max_calls)


def run_tests():
    """Helper function to run all tests"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBinarySearchYear)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == '__main__':
    run_tests()