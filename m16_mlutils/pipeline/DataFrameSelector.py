from sklearn.base import BaseEstimator, TransformerMixin


# A class to select numerical or categorical columns
# since Scikit-Learn doesn't handle DataFrames yet
# From: https://github.com/ageron/handson-ml/blob/master/02_end_to_end_machine_learning_project.ipynb

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        """
        
        :param columns: Pass a str to get a Pandas Series when transforming, pass a list to get a Pandas DataFrame
        """
        self.attribute_names = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names]
