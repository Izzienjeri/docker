import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
import unittest
from solution import CategoricalEncoder

class TestCategoricalEncoder(unittest.TestCase):

    def setUp(self):
        # Initialize a CategoricalEncoder instance before each test
        self.encoder = CategoricalEncoder()

        # Training data
        self.train_data = pd.DataFrame({
            'color': ['red', 'green', 'blue', 'red'],
            'size': ['S', 'M', 'L', 'XL'],
            'price': [10, 20, 30, 40]
        })

        # Inference data
        self.inference_data = pd.DataFrame({
            'color': ['green', 'blue', 'yellow'],
            'size': ['M', 'L', 'XXL'],
            'price': [25, 35, 45]
        })

        self.categorical_cols = ['color', 'size']

    def test_initialization(self):
        # Test Case 1: Initialization
        self.assertIsInstance(self.encoder.encoder, OrdinalEncoder)
    
    def test_fit_transform_training_data(self):
        # Test Case 2: Fit and transform training data
        encoded_train_data = self.encoder.fit_transform(self.train_data.copy(), self.categorical_cols)
        
        # Expected Output:
        expected_train_data = pd.DataFrame({
            'color': [2., 1., 0., 2.],
            'size': [2., 1., 0., 3.],
            'price': [10, 20, 30, 40]
        })

        pd.testing.assert_frame_equal(encoded_train_data, expected_train_data)

    def test_transform_inference_data(self):
        # Test Case 3: Transform inference data
        self.encoder.fit_transform(self.train_data.copy(), self.categorical_cols)
        encoded_inference_data = self.encoder.transform(self.inference_data.copy())

        # Expected Output:
        expected_inference_data = pd.DataFrame({
            'color': [1., 0., -1.],
            'size': [1., 0., -1.],
            'price': [25, 35, 45]
        })

        pd.testing.assert_frame_equal(encoded_inference_data, expected_inference_data)

    def test_handle_new_categories(self):
        # Test Case 4: Handle new categories in inference data
        self.encoder.fit_transform(self.train_data.copy(), self.categorical_cols)
        encoded_inference_data = self.encoder.transform(self.inference_data.copy())

        # Expected Output: (Assuming unknown categories are encoded as -1)
        expected_inference_data = pd.DataFrame({
            'color': [1., 0., -1.],
            'size': [1., 0., -1.],
            'price': [25, 35, 45]
        })
        
        pd.testing.assert_frame_equal(encoded_inference_data, expected_inference_data)
   
    def test_no_categorical_columns(self):
        # Test Case 5: No categorical columns specified
        encoded_df = self.encoder.fit_transform(self.train_data.copy(), [])
        pd.testing.assert_frame_equal(encoded_df, self.train_data)

    def test_transform_before_fit(self):
        # Test case 6: Transform called before fit_transform
        with self.assertRaises(Exception):
            self.encoder.transform(self.inference_data.copy())

    def test_invalid_column_names(self):
        # Test case 7: Invalid column names
        invalid_cols = ["nonexistent_col"]
        with self.assertRaises(KeyError):
            self.encoder.fit_transform(self.train_data.copy(), invalid_cols)

if __name__ == '__main__':
    unittest.main()