import os
from extract_solution import extract_solution

llm_response = r'''
```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split

class ForwardStepwiseSelector:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.load_data()
        self.train_data = None
        self.test_data = None

    def load_data(self):
        try:
            df = pd.read_csv(self.filepath)
            df.columns = df.columns.str.lower()
            return df
        except FileNotFoundError:
            print(f"Error: File '{self.filepath}' not found.")
            return None

    def split_data(self, test_size=0.2, random_state=42):
        if self.data is not None:
            self.train_data, self.test_data = train_test_split(self.data, test_size=test_size, random_state=random_state)

    def add_constant_to_data(self, data):
        data = data.copy()
        data['const'] = 1  # Adding constant for the intercept term.
        return data

    def train_model(self, X, y):
        model = sm.OLS(y, X)
        results = model.fit()
        return results

    def calculate_rss(self, model, X, y):
        return np.sum(np.square(y - model.predict(X)))


    def select_best_predictor(self, predictors_forward, remaining_predictors):
        best_rss = float('inf')
        best_model = None
        best_predictor = None

        for predictor in remaining_predictors:
            predictors_current = predictors_forward + [predictor]
            X_train = self.add_constant_to_data(self.train_data[predictors_current])
            model = self.train_model(X_train, self.train_data['mpg'])
            rss = self.calculate_rss(model, X_train, self.train_data['mpg'])

            if rss < best_rss:
                best_rss = rss
                best_model = model
                best_predictor = predictor

        return best_model, best_predictor

    def forward_stepwise_selection(self):
        predictors_forward = []
        remaining_predictors = list(self.data.columns)
        remaining_predictors.remove('mpg')  # Assuming 'mpg' is the target variable
        chosen_models = []

        while remaining_predictors:
            model, predictor = self.select_best_predictor(predictors_forward, remaining_predictors)
            predictors_forward.append(predictor)
            remaining_predictors.remove(predictor)
            chosen_models.append(model)

        return chosen_models, predictors_forward

    def evaluate_models_on_test_data(self, chosen_models, predictors_forward):
        best_test_rss = float('inf')
        best_model_index = -1

        for i, model in enumerate(chosen_models):
            predictors = ['const'] + predictors_forward[:i+1]
            X_test = self.add_constant_to_data(self.test_data[predictors])
            test_rss = self.calculate_rss(model, X_test, self.test_data['mpg'])

            if test_rss < best_test_rss:
                best_test_rss = test_rss
                best_model_index = i

        return best_model_index, best_test_rss

    def run(self):
        self.split_data()

        if self.train_data is not None and self.test_data is not None:
            chosen_models, predictors_forward = self.forward_stepwise_selection()
            best_model_index, best_test_rss = self.evaluate_models_on_test_data(chosen_models, predictors_forward)

            print(f"The best model (index {best_model_index}) based on test RSS has a test RSS of: {best_test_rss:.2f}")


# Example usage (assuming 'auto.csv' is in the same directory):
selector = ForwardStepwiseSelector("auto.csv")
selector.run()

```

**To make this code runnable, you'll need to:**

1.  **Save the code:** Save the code above as a Python file (e.g., `forward_stepwise.py`).
2.  **Download the dataset:** Download the `auto.csv` dataset.  Make sure that the `name` column is removed and it has a column named 'mpg' as the target variable. A working copy of the dataset can be found [here](https://www.google.com/url?sa=E&source=gmail&q=https://github.com/JWarmenhoven/ISLR-python/blob/master/Notebooks/Data/Auto.csv). Ensure it's in the same directory as your Python script or provide the correct path.
3.  **Install libraries:** If you haven't already, install the necessary libraries using pip:  `pip install pandas numpy statsmodels scikit-learn`
4.  **Run the script:** Execute the script from your terminal: `python forward_stepwise.py`

The output will show the index of the best model and its corresponding test RSS.  Note that the specific output values may differ slightly depending on the contents of your "auto.csv" if it deviates from the standard `Auto` dataset in the ISLR Python repository. If no output is generated and the script does not terminate, it's likely due to the `auto.csv` file not being found or an issue in loading it. Review the error messages, verify the file path, and ensure the file is correctly formatted.
'''

try:
    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):
        raise ValueError(
            "Expected response to be a list of (file_name, code) tuples."
        )

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists
        if not os.path.isfile(file_name):
            raise FileNotFoundError(
                f"The file '{file_name}' does not exist. "
                "Please check the path."
            )

        # Proceed to write only if the file already exists
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(code)

        print(f"File '{file_name}' written successfully.")
except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")
