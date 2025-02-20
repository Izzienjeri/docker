"""Test file."""
import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
import os
from solution import calculate_user_trait_correlations


class TestCalculateUserTraitCorrelations(unittest.TestCase):
    """Test functions."""

    @patch("solution.pearsonr", new=None)
    @patch("solution.spearmanr", new=None)
    def test_missing_pearsonr_and_spearmanr_import(self):
        """Test Case 1: Missing `pearsonr` and `spearmanr` Imports."""
        with self.assertRaises(TypeError) as context:
            calculate_user_trait_correlations()
        self.assertIn("object is not callable",
                      str(context.exception))

    @patch('pandas.read_csv')
    def test_empty_dataframes(self, mock_read_csv):
        """Mock read_csv to return DF with correct structure but no rows."""
        def mock_read(file_path, *args, **kwargs):
            if file_path == 'ratings.csv':
                return pd.DataFrame(
                    columns=['userId',
                             'movieId',
                             'rating',
                             'timestamp'])
            elif file_path == 'user_personality.csv':
                return pd.DataFrame(
                    columns=['userId',
                             'Extraversion',
                             'Agreeableness',
                             'Openness',
                             'Conscientiousness',
                             'Neuroticism'])
            elif file_path == 'movies.csv':
                return pd.DataFrame(
                    columns=['movieId',
                             'title',
                             'genres'])
            return pd.DataFrame()

        mock_read_csv.side_effect = mock_read

        # Run function and check output
        result = calculate_user_trait_correlations()
        self.assertTrue(result.empty)

    def test_users_with_one_rating(self):
        """Test Case 4: Users with only one rating."""
        # Create a sample DataFrame with one user having only one rating
        ratings_data = {
            'userId': [1],
            'movieId': [1],
            'rating': [4],
            'timestamp': [1234567890]
        }
        user_personality_data = {
            'userId': [1],
            'Extraversion': [3],
            'Agreeableness': [4],
            'Openness': [5],
            'Conscientiousness': [2],
            'Neuroticism': [1]
        }
        ratings_df = pd.DataFrame(ratings_data)
        user_personality_df = pd.DataFrame(user_personality_data)

        with patch('pandas.read_csv', side_effect=[pd.DataFrame(),
                                                   ratings_df,
                                                   user_personality_df]):
            result = calculate_user_trait_correlations()
            # Ensure users with one rating are filtered out
            self.assertTrue(result.empty)

    def test_valid_dataset(self):
        """Test Case 5: Calculate correlations for a valid dataset."""
        # Create sample data
        ratings_data = {
            'userId': [1, 1, 2, 2],
            'movieId': [1, 2, 1, 2],
            'rating': [4, 5, 3, 4],
            'timestamp': [1234567890,
                          1234567891,
                          1234567892,
                          1234567893]
        }
        user_personality_data = {
            'userId': [1, 2],
            'Extraversion': [3, 4],
            'Agreeableness': [4, 3],
            'Openness': [5, 2],
            'Conscientiousness': [2, 5],
            'Neuroticism': [1, 2]
        }
        ratings_df = pd.DataFrame(ratings_data)
        user_personality_df = pd.DataFrame(user_personality_data)

        with patch('pandas.read_csv',
                   side_effect=[pd.DataFrame(),
                                ratings_df,
                                user_personality_df]):
            result = calculate_user_trait_correlations()
            self.assertFalse(result.empty)
            self.assertIn('Pearson', result.columns)
            self.assertIn('Spearman', result.columns)

    def test_save_results_to_csv(self):
        """Test Case 6: Save results to CSV."""
        # Create sample data
        ratings_data = {
            'userId': [1, 1],
            'movieId': [1, 2],
            'rating': [4, 5],
            'timestamp': [1234567890, 1234567891]
        }
        user_personality_data = {
            'userId': [1],
            'Extraversion': [3],
            'Agreeableness': [4],
            'Openness': [5],
            'Conscientiousness': [2],
            'Neuroticism': [1]
        }
        ratings_df = pd.DataFrame(ratings_data)
        user_personality_df = pd.DataFrame(user_personality_data)

        with patch('pandas.read_csv',
                   side_effect=[pd.DataFrame(),
                                ratings_df,
                                user_personality_df]):
            calculate_user_trait_correlations()
            self.assertTrue(os.path.exists(
                'user_correlation_results.csv'))
            os.remove('user_correlation_results.csv')  # Clean up

    def test_performance_on_large_datasets(self):
        """Test Case 7: Performance on large datasets."""
        # Create a large dataset
        np.random.seed(42)
        num_users = 1000
        num_ratings = 10000
        ratings_data = {
            'userId': np.random.randint(1, num_users + 1, num_ratings),
            'movieId': np.random.randint(1, 100, num_ratings),
            'rating': np.random.randint(1, 6, num_ratings),
            'timestamp': np.random.randint(1e9, 2e9, num_ratings)
        }
        user_personality_data = {
            'userId': np.arange(1, num_users + 1),
            'Extraversion': np.random.randint(1, 6, num_users),
            'Agreeableness': np.random.randint(1, 6, num_users),
            'Openness': np.random.randint(1, 6, num_users),
            'Conscientiousness': np.random.randint(1, 6, num_users),
            'Neuroticism': np.random.randint(1, 6, num_users)
        }
        ratings_df = pd.DataFrame(ratings_data)
        user_personality_df = pd.DataFrame(user_personality_data)

        with patch('pandas.read_csv',
                   side_effect=[pd.DataFrame(),
                                ratings_df,
                                user_personality_df]):
            import time
            start_time = time.time()
            calculate_user_trait_correlations()
            end_time = time.time()
            # Ensure it completes within 10 seconds
            self.assertLess(end_time - start_time, 10)

    @patch('pandas.read_csv')
    def test_verify_pandas_read_csv(self, mock_read_csv):
        """Test Case 8: Verify pandas `read_csv` is used."""
        # Create sample DataFrames
        movies_df = pd.DataFrame()
        ratings_df = pd.DataFrame({
            'userId': [1, 1],
            'movieId': [1, 2],
            'rating': [4, 5],
            'timestamp': [1234567890, 1234567891]
        })
        user_personality_df = pd.DataFrame({
            'userId': [1],
            'Extraversion': [3],
            'Agreeableness': [4],
            'Openness': [5],
            'Conscientiousness': [2],
            'Neuroticism': [1]
        })

        mock_read_csv.side_effect = [movies_df,
                                     ratings_df,
                                     user_personality_df]
        calculate_user_trait_correlations()
        # Verify `read_csv` was called 3 times
        self.assertEqual(
            mock_read_csv.call_count, 3)


if __name__ == '__main__':
    unittest.main()
