import os

from extract_solution import extract_solution

llm_response = r'''
```python
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

class CategoricalEncoder:
    """"""
    Encodes categorical data using OrdinalEncoder, handling unseen categories during inference.
    """"""
    def __init__(self) -> None:
        """"""
        Initializes the CategoricalEncoder with an OrdinalEncoder and handles unknown value and categorical_cols.
        """"""
        self.encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
        self.categorical_cols = None
    def fit_transform(self, df: pd.DataFrame, categorical_cols: list[str]) -> pd.DataFrame:
        """"""
        Fits the OrdinalEncoder to the specified categorical columns and transforms them.
        Args:
            df: The input DataFrame.
            categorical_cols: A list of column names to encode.
        Returns:
            The transformed dataframe.
        """"""
        self.categorical_cols = categorical_cols
        df[self.categorical_cols] = self.encoder.fit_transform(df[self.categorical_cols])
        return df
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """"""
        Transforms the specified categorical columns using the fitted OrdinalEncoder.
        Args:
            df: The input DataFrame.
        Returns:
            The DataFrame with the specified columns transformed.
        """"""
        if self.categorical_cols is None:
            raise ValueError(""Encoder has not been fitted yet. Call 'fit_transform' first."")
        # Ensure all categorical columns from training are present in the inference data
        missing_cols = set(self.categorical_cols) - set(df.columns)
        if missing_cols:
            raise ValueError(f""The following columns are missing in the inference data: {missing_cols}"")
        df[self.categorical_cols] = self.encoder.transform(df[self.categorical_cols])
        return df
    
# Example usage:
train_df = pd.DataFrame({'color': ['red', 'green', 'blue'], 'size': ['small', 'medium', 'large']})
test_df = pd.DataFrame({'color': ['red', 'green', 'yellow'], 'size': ['small', 'medium', 'extra large']})
encoder = CategoricalEncoder()
train_encoded = encoder.fit_transform(train_df.copy(), categorical_cols=['color', 'size'])
test_encoded = encoder.transform(test_df.copy())
print(""Encoded Training Data:\n"", train_encoded)
print(""\nEncoded Test Data:\n"", test_encoded)
```
'''

try:

    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):
        raise ValueError("Expected response to be a list of (file_name, code) tuples.")

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists

        if not os.path.isfile(file_name):
            raise FileNotFoundError(

                f"The file '{file_name}' does not exist. Please check the path."

            )

        # Proceed to write only if the file already exists

        with open(file_name, "w") as file:

            file.write(code)

        print(f"File '{file_name}' written successfully.")

except FileNotFoundError as fnf_error:

    print(f"File error: {fnf_error}")

except Exception as e:

    print(f"An error occurred while running extract solution test: {e}")