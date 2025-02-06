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
            df.columns = df.columns.str.lower()  # Ensure all column names are lowercase
            return df
        except FileNotFoundError:
            print("Error: The file was not found.")
            return None

    def split_data(self, test_size=0.2, random_state=42):
        if self.data is not None:
            self.train_data, self.test_data = train_test_split(self.data, test_size=test_size, random_state=random_state)
        else:
            print("Error: Data not loaded correctly.")

    def add_constant_to_data(self, data):
        return sm.add_constant(data)

    def train_model(self, X, y):
        model = sm.OLS(y, X).fit()
        return model

    def calculate_rss(self, model, X, y):
        predictions = model.predict(X)
        rss = np.sum((y - predictions) ** 2)
        return rss

    def select_best_predictor(self, predictors_forward, remaining_predictors):
        best_rss = np.inf
        best_model = None
        best_predictor = None
        for predictor in remaining_predictors:
            current_predictors = predictors_forward + [predictor]
            X_train = self.add_constant_to_data(self.train_data[current_predictors])
            y_train = self.train_data['mpg']
            try:
                model = self.train_model(X_train, y_train)
                rss = self.calculate_rss(model, X_train, y_train)
                if rss < best_rss:
                    best_rss = rss
                    best_model = model
                    best_predictor = predictor
            except Exception as e:
                print(f"Error while training model with predictors {current_predictors}: {e}")
        return best_model, best_predictor

    def forward_stepwise_selection(self):
        predictors_forward = []
        chosen_models = []
        remaining_predictors = list(self.data.columns)
        remaining_predictors.remove('mpg')  # Remove the target variable from predictor list
        # Perform at least 3 iterations
        for _ in range(min(3, len(remaining_predictors))):
            best_model, best_predictor = self.select_best_predictor(predictors_forward, remaining_predictors)
            if best_model is not None:
                predictors_forward.append(best_predictor)
                chosen_models.append(best_model)
                remaining_predictors.remove(best_predictor)
            else:
                print("No valid model found during this iteration.")
                break
        # Continue until all predictors have been considered
        while remaining_predictors:
            best_model, best_predictor = self.select_best_predictor(predictors_forward, remaining_predictors)
            if best_model is not None:
                predictors_forward.append(best_predictor)
                chosen_models.append(best_model)
                remaining_predictors.remove(best_predictor)
            else:
                print("No valid model found. Exiting selection.")
                break
        return chosen_models, predictors_forward

    def evaluate_models_on_test_data(self, chosen_models, predictors_forward):
        best_rss = np.inf
        best_model_index = -1
        y_test = self.test_data['mpg']
        for i, model in enumerate(chosen_models):
            # Ensure that the test data for predictors is properly sliced
            X_test = self.add_constant_to_data(self.test_data[predictors_forward[:i+1]])
            try:
                rss = self.calculate_rss(model, X_test, y_test)
                if rss < best_rss:
                    best_rss = rss
                    best_model_index = i
            except Exception as e:
                print(f"Error while evaluating model {i}: {e}")
        return best_model_index, best_rss

    def run(self):
        self.split_data()
        if self.train_data is not None and self.test_data is not None:
            chosen_models, predictors_forward = self.forward_stepwise_selection()
            if chosen_models:
                best_model_index, best_rss = self.evaluate_models_on_test_data(chosen_models, predictors_forward)
                print(f"The best model (index {best_model_index}) based on test RSS has a test RSS of: {best_rss:.2f}")
            else:
                print("No models were selected.")
        else:
            print("Data could not be loaded or split correctly. Please check the file path and try again.")

# Example of how to use the class:
selector = ForwardStepwiseSelector("auto.csv")
selector.run()
