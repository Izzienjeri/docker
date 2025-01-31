"""This module contains unit tests for the ForwardStepwiseSelector class."""

import os
import unittest
import pandas as pd
from tempfile import NamedTemporaryFile
from io import StringIO
import sys
import re

from solution import ForwardStepwiseSelector


class TestForwardStepwiseSelector(unittest.TestCase):
    """Unit tests for the ForwardStepwiseSelector class."""

    def setUp(self):
        """Set up mock CSV data and reusable DataFrames for tests."""
        self.mock_csv_file_path = self.create_mock_csv()
        self.small_subset_df = self.create_small_subset_df()

    def tearDown(self):
        """Clean up any temporary files created during tests."""
        if os.path.exists(self.mock_csv_file_path):
            os.remove(self.mock_csv_file_path)

    def create_mock_csv(self):
        """
        Create a temporary CSV file with automotive-like data.

        Returns:
            str: Path to the temporary CSV file.
        """
        df = pd.DataFrame({
            'MPG': [18.0, 15.0, 36.0, 24.0, 22.0, 35.0, 20.0],
            'CYLINDERS': [8, 8, 4, 4, 6, 4, 6],
            'DISPLACEMENT': [307.0, 350.0, 107.0, 121.0, 146.0, 120.0, 156.0],
            'HORSEPOWER': [130.0, 165.0, 93.0, 90.0, 105.0, 88.0, 95.0],
            'WEIGHT': [3504.0, 3693.0, 2130.0, 2264.0, 2800.0, 2100.0, 3003.0],
            'ACCELERATION': [12.0, 11.5, 16.5, 14.0, 15.5, 14.5, 16.0],
            'YEAR': [70, 70, 82, 76, 78, 81, 79],
            'ORIGIN': [1, 1, 2, 1, 3, 2, 1],
        })

        with NamedTemporaryFile(mode='w', suffix=".csv", delete=False,
                                prefix="test_auto") as tf:
            df.to_csv(tf.name, index=False)
            return tf.name

    def create_small_subset_df(self):
        """
        Return a small, in-memory DataFrame for model training tests.

        Returns:
            DataFrame: A small subset DataFrame for testing purposes.
        """
        data = {
            'mpg': [18.0, 15.0, 36.0, 24.0, 22.0],
            'cylinders': [8, 8, 4, 4, 6],
            'displacement': [307.0, 350.0, 107.0, 121.0, 146.0],
            'horsepower': [130.0, 165.0, 93.0, 90.0, 105.0],
            'weight': [3504.0, 3693.0, 2130.0, 2264.0, 2800.0],
            'acceleration': [12.0, 11.5, 16.5, 14.0, 15.5],
            'year': [70, 70, 82, 76, 78],
            'origin': [1, 1, 2, 1, 3],
        }
        return pd.DataFrame(data)

    def test_file_loading_and_preprocessing(self):
        """Test that the CSV file is correctly loaded and preprocessed."""
        selector = ForwardStepwiseSelector(self.mock_csv_file_path)

        self.assertIsInstance(selector.data, pd.DataFrame,
                              "load_data() did not return a DataFrame.")

        self.assertTrue(all(col.islower() for col in selector.data.columns),
                        "Not all columns are lowercase.")

        selector.split_data(test_size=0.2, random_state=42)

        self.assertIsNotNone(selector.train_data,
                             "train_data not set after splitting.")
        self.assertIsNotNone(selector.test_data,
                             "test_data not set after splitting.")
        self.assertGreaterEqual(len(selector.test_data), 1,
                                "test_data size is too small.")

    def test_file_loading_error_handling(self):
        """Test error handling for non-existent file paths."""
        selector = ForwardStepwiseSelector("non_existent_file.csv")
        self.assertIsNone(selector.data,
                          "Data should be None for non-existent file.")

    def test_model_training_and_rss_calculation(self):
        """Test model training and RSS calculation functionality."""
        selector = ForwardStepwiseSelector(self.mock_csv_file_path)
        selector.train_data = self.small_subset_df.copy()
        selector.test_data = self.small_subset_df.copy()

        x_train = selector.add_constant_to_data(
            selector.train_data[['cylinders', 'horsepower']]
        )
        y_train = selector.train_data['mpg']
        model = selector.train_model(x_train, y_train)

        self.assertTrue(hasattr(model, 'params'),
                        "train_model() did not return a valid model.")

        rss_train = selector.calculate_rss(model, x_train, y_train)
        self.assertGreaterEqual(rss_train, 0, "RSS should be non-negative.")

    def test_forward_stepwise_selection_logic_manual_iterations(self):
        """Test forward stepwise selection logic with manual iterations."""
        selector = ForwardStepwiseSelector(self.mock_csv_file_path)
        selector.train_data = self.small_subset_df.copy()
        selector.test_data = self.small_subset_df.copy()

        all_predictors = ['cylinders', 'displacement', 'horsepower']
        predictors_forward = []

        for _ in range(len(all_predictors)):
            model, predictor = selector.select_best_predictor(
                predictors_forward,
                [p for p in all_predictors if p not in predictors_forward]
            )
            predictors_forward.append(predictor)

        self.assertEqual(len(predictors_forward), len(all_predictors),
                         "Not all predictors selected.")

    def test_full_forward_stepwise_selection(self):
        """Test the full forward stepwise selection process."""
        selector = ForwardStepwiseSelector(self.mock_csv_file_path)
        selector.split_data(test_size=0.2, random_state=42)

        chosen, predictors_forward = selector.forward_stepwise_selection()

        self.assertIsNotNone(chosen)
        self.assertIsNotNone(predictors_forward)
        self.assertEqual(len(chosen), len(predictors_forward))

    def test_model_evaluation_and_selection(self):
        """Test model evaluation and selection based on test RSS."""
        selector = ForwardStepwiseSelector(self.mock_csv_file_path)

        chosen, predictors_forward = selector.forward_stepwise_selection()
        best_model, best_model_rss = selector.evaluate_models_on_test_data(
            chosen, predictors_forward
        )

        self.assertGreaterEqual(best_model, 0)
        self.assertGreaterEqual(best_model_rss, 0)

    def test_end_to_end_run(self):
        """End-to-end test for the ForwardStepwiseSelector class."""
        selector = ForwardStepwiseSelector(self.mock_csv_file_path)

        captured_output = StringIO()
        sys.stdout = captured_output

        selector.run()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        numbers = re.findall(r"\d+\.\d+|\d+", output)

        self.assertGreaterEqual(len(numbers), 2,
                                "Output does not contain model index and RSS.")

        model_index = numbers[0]
        self.assertTrue(model_index.isdigit(),
                        "The first number should represent the model index.")

        test_rss = numbers[1]
        self.assertTrue(re.match(r"\d+\.\d+", test_rss),
                        "The second number should represent the RSS.")


if __name__ == '__main__':
    unittest.main()
