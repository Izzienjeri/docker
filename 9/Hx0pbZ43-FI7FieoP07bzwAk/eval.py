import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from solution import fill_missing_values

class TestFillNullWithMean(unittest.TestCase):  

    def test_multiple_missing_values(self):
        df=pd.DataFrame({'A': [1, None, 3], 'B': [None, 5.0, 6.0]})

        df_expected = pd.DataFrame({'A': [1, 2, 3], 'B': [5.5, 5.0, 6.0]})
        assert_frame_equal(df_expected, fill_missing_values(df),check_dtype=False)

    def test_non_numerical_columns(self):
        df = pd.DataFrame({'A': [1, None, 3], 'B': ['a', None, 'c']})
        df_expected = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', None, 'c']})
        assert_frame_equal(df_expected, fill_missing_values(df),check_dtype=False)

    def test_mixed_columns(self):
        df = pd.DataFrame({'A': [1, None, 3], 'B': [1.0, None, 'c']})
        df_expected = pd.DataFrame({'A': [1, 2, 3], 'B': [1.0, None, 'c']})
        assert_frame_equal(df_expected, fill_missing_values(df),check_dtype=False)
        
    def test_original_unmodified(self):
        df=pd.DataFrame({'A': [1, None, 3], 'B': [None, 5.0, 6.0]})
        assert not df.equals(fill_missing_values(df))
        
    def test_non_standard_numeric_input(self):
        df=pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]},dtype='int16')
        
        df_expected = df.copy()
        # set an element in column A to NaN
        df.at[1,'A'] = pd.NA
        assert_frame_equal(df_expected,fill_missing_values(df),check_dtype=False)

if __name__ == "__main__":
    unittest.main()