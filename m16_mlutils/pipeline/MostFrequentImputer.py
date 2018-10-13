from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


# A class to impute missing values given a collection of seen values
# From: https://github.com/ageron/handson-ml/blob/master/02_end_to_end_machine_learning_project.ipynb
# Inspired from stackoverflow.com/questions/25239958
class MostFrequentImputer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        self.most_frequent_ = pd.Series(
            [X[c].value_counts().index[0] for c in X],
            index=X.columns)
        return self

    def transform(self, X, y=None):
        return X.fillna(self.most_frequent_)
