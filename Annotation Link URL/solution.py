"""This module implements a forward stepwise selection algorithm."""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split


class ForwardStepwiseSelector:
    """A class for performing forward stepwise selection."""

    def __init__(self, filepath):
        """
        Initialize the ForwardStepwiseSelector with the file path.

        Args:
            filepath (str): Path to the CSV file containing the dataset.
        """
        self.filepath = filepath
        self.data = self.load_data()
        self.train_data, self.test_data = None, None
        self.split_data()

    def load_data(self):
        """
        Load the dataset from the specified file path.

        Returns:
            DataFrame: Loaded dataset with column names in lowercase.
            None: If the file is not found.
        """
        try:
            data = pd.read_csv(self.filepath)
            data.columns = [col.lower() for col in data.columns]
            return data
        except FileNotFoundError:
            print("File not found.")
            return None

    def split_data(self, test_size=0.2, random_state=42):
        """
        Split the data into training and test sets.

        Args:
            test_size (float): Proportion of data to use for the test set.
            random_state (int): Random seed for reproducibility.
        """
        if self.data is not None:
            self.train_data, self.test_data = train_test_split(
                self.data, test_size=test_size, random_state=random_state
            )

    def add_constant_to_data(self, data):
        """
        Add a constant column to the data for regression.

        Args:
            data (DataFrame): Data to which the constant column will be added.

        Returns:
            DataFrame: Data with a constant column added.
        """
        return sm.add_constant(data)

    def train_model(self, x, y):
        """
        Train an OLS regression model.

        Args:
            x (DataFrame): Predictor variables.
            y (Series): Response variable.

        Returns:
            RegressionResults: Trained OLS model.
        """
        model = sm.OLS(y, x)
        return model.fit()

    def calculate_rss(self, model, x, y):
        """
        Calculate the Residual Sum of Squares (RSS) for a model.

        Args:
            model (RegressionResults): Trained regression model.
            x (DataFrame): Predictor variables.
            y (Series): Actual response values.

        Returns:
            float: Residual Sum of Squares (RSS).
        """
        predictions = model.predict(x)
        residuals = y - predictions
        rss = np.sum(residuals**2)
        return rss

    def select_best_predictor(self, predictors_forward, remaining_predictors):
        """
        Select the best predictor to add to the model by minimizing RSS.

        Args:
            predictors_forward (list): Current predictors in the model.
            remaining_predictors (list): Predictors not yet added to the model.

        Returns:
            tuple: The best model, best predictor, and corresponding RSS.
        """
        best_rss = np.inf
        best_model = None
        best_predictor = None

        for predictor in remaining_predictors:
            trial_predictors = predictors_forward + [predictor]
            x_train = self.add_constant_to_data(
                self.train_data[trial_predictors]
            )
            y_train = self.train_data['mpg']
            model = self.train_model(x_train, y_train)
            rss = self.calculate_rss(model, x_train, y_train)

            if rss < best_rss:
                best_rss = rss
                best_model = model
                best_predictor = predictor

        return best_model, best_predictor

    def forward_stepwise_selection(self):
        """
        Perform forward stepwise selection to choose the best predictors.

        Returns:
            tuple: List of chosen models and their corresponding predictors.
        """
        predictors_forward = []
        chosen_models = []
        remaining_predictors = [
            col for col in self.train_data.columns if col != 'mpg'
        ]

        while remaining_predictors:
            model, predictor = self.select_best_predictor(
                predictors_forward, remaining_predictors
            )
            predictors_forward.append(predictor)
            chosen_models.append(model)
            remaining_predictors.remove(predictor)

        return chosen_models, predictors_forward

    def evaluate_models_on_test_data(self, chosen_models, predictors_forward):
        """
        Evaluate models on the test dataset to determine the best one.

        Args:
            chosen_models (list): Models from forward selection.
            predictors_forward (list): Predictors used in the models.

        Returns:
            tuple: Index of the best model and its RSS on the test set.
        """
        y_test = self.test_data['mpg']
        best_rss = np.inf
        best_model_index = None

        for i, model in enumerate(chosen_models):
            predictors = predictors_forward[:i + 1]
            x_test = self.add_constant_to_data(self.test_data[predictors])
            x_test = x_test.reindex(
                columns=model.model.exog_names, fill_value=0
            )
            rss = self.calculate_rss(model, x_test, y_test)

            if rss < best_rss:
                best_rss = rss
                best_model_index = i

        return best_model_index, best_rss

    def run(self):
        """
        Run the forward stepwise selection process and evaluates models.

        Prints the best model based on the test RSS.
        """
        chosen_models, predictors_forward = self.forward_stepwise_selection()
        best_index, best_test_rss = self.evaluate_models_on_test_data(
            chosen_models, predictors_forward
        )
        print(
            f"The best model (index {best_index}) based on test RSS "
            f"has a test RSS of: {best_test_rss:.2f}"
        )

# Usage example:
# selector = ForwardStepwiseSelector("auto.csv")
# selector.run()
