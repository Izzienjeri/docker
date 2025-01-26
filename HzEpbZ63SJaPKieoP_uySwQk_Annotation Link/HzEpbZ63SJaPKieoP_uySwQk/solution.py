from sklearn.preprocessing import OrdinalEncoder
import pandas as pd

class CategoricalEncoder:
    def __init__(self):
        """
        Initializes an instance of CategoricalEncoder with an OrdinalEncoder object.
        """
        self.encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
        self.categorical_cols = None 

    def fit_transform(self, df, categorical_cols):
        """
        Fits the OrdinalEncoder to the specified categorical columns of a pandas DataFrame 
        and transforms those columns.

        Args:
            df (pandas.DataFrame): The input DataFrame.
            categorical_cols (list): A list of column names to encode.

        Returns:
            pandas.DataFrame: The DataFrame with the specified columns transformed.
        """
        self.categorical_cols = categorical_cols 
        df_encoded = df.copy()
        self.encoder.fit(df[categorical_cols])
        df_encoded[categorical_cols] = self.encoder.transform(df[categorical_cols])
        return df_encoded

    def transform(self, df):
        """
        Transforms the specified categorical columns in a pandas DataFrame 
        using the fitted OrdinalEncoder.

        Args:
            df (pandas.DataFrame): The input DataFrame.

        Returns:
            pandas.DataFrame: The DataFrame with the specified columns transformed.
        """
        if self.categorical_cols is None:
            raise ValueError("CategoricalEncoder must be fitted before transforming data.")

        df_encoded = df.copy()
        df_encoded[self.categorical_cols] = self.encoder.transform(df[self.categorical_cols])
        return df_encoded
    

train_df = pd.DataFrame({'color': ['red', 'green', 'blue'], 'size': ['small', 'medium', 'large']})
test_df = pd.DataFrame({'color': ['red', 'green', 'yellow'], 'size': ['small', 'medium', 'extra large']})
encoder = CategoricalEncoder()
train_encoded = encoder.fit_transform(train_df.copy(), categorical_cols=['color', 'size'])
test_encoded = encoder.transform(test_df.copy())
print("Encoded Training Data:\n", train_encoded)
print("\nEncoded Test Data:\n", test_encoded)
