import unittest
from solution import reformat_date

class Test(unittest.TestCase):
    def test_valid_dates(self):
        self.assertEqual(reformat_date("2024-9-18"), "18-09-2024")
        self.assertEqual(reformat_date("2024/10/05"), "05-10-2024")
        self.assertEqual(reformat_date("2024.1.1"), "01-01-2024")
        self.assertEqual(reformat_date("2024 1 1"), "01-01-2024")
        self.assertEqual(reformat_date("2024,1,1"), "01-01-2024")
        self.assertEqual(reformat_date("2022-01-2"), "02-01-2022")
        self.assertEqual(reformat_date("2023-12-30"), "30-12-2023")

    def test_valid_dates_with_whitespace(self):
        self.assertEqual(reformat_date(" 2024-9-18"), "18-09-2024")
        self.assertEqual(reformat_date("2024/10/05 "), "05-10-2024")
        self.assertEqual(reformat_date("  2024.1.1  "), "01-01-2024")
        self.assertEqual(reformat_date(" 2024 1 1 "), "01-01-2024")
        self.assertEqual(reformat_date("2024 , 1 , 1"), "01-01-2024")
        self.assertEqual(reformat_date(" 2024 - 01 - 2 "), "02-01-2024")
        self.assertEqual(reformat_date(" 2023-12-30\t"), "30-12-2023")

    def test_valid_dates_with_inconsistent_delimiters(self):
        self.assertEqual(reformat_date("2024-9/18"), "18-09-2024")
        self.assertEqual(reformat_date("2024/10.05"), "05-10-2024")
        self.assertEqual(reformat_date("2024.1 1"), "01-01-2024")
        self.assertEqual(reformat_date("2022 1,2"), "02-01-2022")
        self.assertEqual(reformat_date("2023,12-30"), "30-12-2023")

    def test_valid_edge_year_dates(self):
        self.assertEqual(reformat_date("1951-01-01"), "01-01-1951")
        self.assertEqual(reformat_date("2050-12-31"), "31-12-2050")

    def test_invalid_dates(self):
        with self.assertRaises(Exception):
            reformat_date("2024-13-01")
        with self.assertRaises(Exception):
            reformat_date("2024-02-30")
        with self.assertRaises(Exception):
            reformat_date("2024/01/32")

    def test_invalid_year_range(self):
        with self.assertRaises(Exception):
            reformat_date("1949-01-01")
        with self.assertRaises(Exception):
            reformat_date("2051-12-31")

    def test_invalid_input_length(self):
        with self.assertRaises(Exception):
            reformat_date("20245-01-01")
        with self.assertRaises(Exception):
            reformat_date("2024-001-01")
        with self.assertRaises(Exception):
            reformat_date("2024-01-001")
        with self.assertRaises(Exception):
             reformat_date("24-01-0001")

    def test_invalid_input_types(self):
        with self.assertRaises(Exception):
            reformat_date("")
        with self.assertRaises(Exception):
            reformat_date("abcd")
        with self.assertRaises(Exception):
            reformat_date("2023")
        with self.assertRaises(Exception):
            reformat_date("2023-12")
        with self.assertRaises(Exception):
            reformat_date("2023-12-1-1")
    
    def test_valid_dates_without_delimiters(self):
        with self.assertRaises(Exception):
            reformat_date("19520701")
    
    def test_february_leap_year(self):
         self.assertEqual(reformat_date("2020-02-29"), "29-02-2020")
         with self.assertRaises(Exception):
            reformat_date("2021-02-29")
    
    def test_february_non_leap_year(self):
        self.assertEqual(reformat_date("2023-02-28"), "28-02-2023")
        with self.assertRaises(Exception):
            reformat_date("2023-02-29")

    def test_date_format_year_month_day(self):
        self.assertEqual(reformat_date("2024-03-04"), "04-03-2024")
        self.assertEqual(reformat_date("2024/12/25"), "25-12-2024")
        self.assertEqual(reformat_date("2024.01.05"), "05-01-2024")
        
    def test_invalid_single_digit_year(self):
        with self.assertRaises(Exception):
            reformat_date("4-05-01")
        with self.assertRaises(Exception):
            reformat_date("5-01-01")
        with self.assertRaises(Exception):
            reformat_date("9-12-30")