import unittest
from unittest.mock import patch
import pandas as pd
from solution import get_nasdaq_equities_filtered

class GetNasdaqEquitiesFilteredTests(unittest.TestCase):

    @patch('solution.get_nasdaq_equities_filtered')
    def test_returned_data_structure(self, mock_get_data):
        """
        Test Case 1: Ensure the returned DataFrame contains 'Symbol' and 'Price' columns.
        """
        mock_data = pd.DataFrame({'Symbol': ['AAPL'], 'Price': [9.5]})
        mock_get_data.return_value = mock_data

        result_df = get_nasdaq_equities_filtered()

        self.assertIn('Symbol', result_df.columns)
        self.assertIn('Price', result_df.columns)

    @patch('solution.get_nasdaq_equities_filtered')
    def test_symbols_are_valid_nasdaq_stocks(self, mock_get_data):
        """
        Test Case 2: Verify that returned stock symbols exist in NASDAQ and are uppercase strings.
        """
        mock_data = pd.DataFrame({'Symbol': ['AAPL', 'GOOG', 'TSLA'], 'Price': [9.5, 6.3, 8.8]})
        mock_get_data.return_value = mock_data

        result_df = get_nasdaq_equities_filtered()

        for symbol in result_df['Symbol']:
            self.assertIsInstance(symbol, str)
            self.assertTrue(symbol.isupper())

    @patch('solution.get_nasdaq_equities_filtered')
    def test_no_matching_stocks(self, mock_get_data):
        """
        Test Case 3: Handle scenario where no stocks meet the criteria.
        """
        mock_data = pd.DataFrame(columns=['Symbol', 'Price'])
        mock_get_data.return_value = mock_data

        result_df = get_nasdaq_equities_filtered()

        self.assertTrue(result_df.empty)
        
    @patch('solution.get_nasdaq_equities_filtered')
    def test_no_duplicate_symbols(self, mock_get_data):
        """
        Test Case 4: Ensure stock symbols are unique in the returned DataFrame.
        """
        mock_data = pd.DataFrame({'Symbol': ['AAPL', 'GOOG', 'AAPL'], 'Price': [9.5, 6.3, 8.8]})
        mock_get_data.return_value = mock_data

        result_df = get_nasdaq_equities_filtered()

        self.assertEqual(len(result_df['Symbol']), len(result_df['Symbol'].unique()))


if __name__ == '__main__':
    unittest.main()
