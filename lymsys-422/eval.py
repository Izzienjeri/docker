import unittest
from unittest.mock import patch
import datetime  
from solution import generate_leap_years


class TestGenerateLeapYears(unittest.TestCase):
    """Tests for generate_leap_years function."""

    @patch('solution.datetime.datetime')
    def test_current_year_is_leap(self, mock_datetime):
        """Test that the current leap year is excluded."""
        mock_datetime.now.return_value = datetime.datetime(2024, 1, 1)  
        leap_years = generate_leap_years()
        self.assertNotIn(2024, leap_years)

    @patch('solution.datetime.datetime')
    def test_current_year_is_not_leap(self, mock_datetime):
        """Test that the current non-leap year is excluded."""
        mock_datetime.now.return_value = datetime.datetime(2023, 1, 1)  
        leap_years = generate_leap_years()
        self.assertNotIn(2023, leap_years)

    @patch('solution.datetime.datetime')
    def test_next_20_leap_years(self, mock_datetime):
        """Test that the function generates the next 20 leap years."""
        mock_datetime.now.return_value = datetime.datetime(2023, 1, 1)  
        leap_years = generate_leap_years()
        expected_leap_years = [
            2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060,
            2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2104
        ]
        self.assertEqual(leap_years, expected_leap_years)

    @patch('solution.datetime.datetime')
    def test_leap_year_divisible_by_100_not_400(self, mock_datetime):
        """Test that a year divisible by 100 but not 400 is excluded."""
        mock_datetime.now.return_value = datetime.datetime(2099, 1, 1)  
        leap_years = generate_leap_years()
        self.assertNotIn(2100, leap_years)

    @patch('solution.datetime.datetime')
    def test_leap_year_divisible_by_400(self, mock_datetime):
        """Test that a year divisible by 400 is included."""
        mock_datetime.now.return_value = datetime.datetime(1999, 1, 1)  
        leap_years = generate_leap_years()
        self.assertIn(2000, leap_years)


if __name__ == '__main__':
    unittest.main()
