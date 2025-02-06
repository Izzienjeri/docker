import os
from extract_solution import extract_solution

llm_response = '''
Here's the completed function:

```python
import pandas as pd

def s(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fills missing values in numerical columns of a Pandas DataFrame with the mean of each column.
    
    Args:
        df: The input DataFrame.
        
    Returns:
        A new DataFrame with missing values in numerical columns filled with their respective column means.
    """
    # Create a copy of the DataFrame to avoid modifying the original
    df_filled = df.copy()
    
    # Get numerical columns
    numeric_columns = df_filled.select_dtypes(include=['int64', 'float64']).columns
    
    # Fill missing values with mean for each numerical column
    for column in numeric_columns:
        df_filled[column] = df_filled[column].fillna(df_filled[column].mean())
    
    return df_filled
```

This function:
1. Creates a copy of the input DataFrame to avoid modifying the original data
2. Identifies numerical columns using `select_dtypes()`
3. Iterates through each numerical column and fills missing values (NaN) with the column's mean value
4. Returns the new DataFrame with filled values

You could use this function like this:

```python
# Example usage
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2.5, 3.0, 4.5],
    'C': ['x', 'y', 'z', None]  # Non-numerical column
})

filled_df = fill_missing_values(df)
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
        print(os.getcwd())
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