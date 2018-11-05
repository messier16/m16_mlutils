import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.exceptions import FitFailedWarning
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.utils.validation import check_array


class CategoryEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, labels=None):
        self.labels = labels
        self.label_encoders = {}
        self.one_hot_encoders = {}

    def __find_names(self, X):
        if type(X) == pd.DataFrame:
            return list(X.columns)
        elif type(X) == np.ndarray:
            return ["%c" % chr(i + ord('A')) for i in range(X.shape[1])]
        return []

    def fit(self, X, y=None):
        check_array(X, dtype=str)
        if type(X) != pd.DataFrame:
            raise FitFailedWarning(
                'You are not supposed to use this with other thing that is not a pandas DataFrame')
        names = self.__find_names(X)
        for c in names:
            self.label_encoders[c] = LabelEncoder()
            self.one_hot_encoders[c] = OneHotEncoder(sparse=False,
                                                     categories='auto')
            if self.labels is not None and c in self.labels:
                self.label_encoders[c].fit(self.labels[c])
                values = self.label_encoders[c].transform(self.labels[c])
            else:
                self.label_encoders[c].fit(X[c].astype(str))
                values = self.label_encoders[c].transform(X[c].astype(str))
            self.one_hot_encoders[c].fit(values.reshape(len(values), 1))

        return self

    def transform(self, X):
        names = self.__find_names(X)
        one_hots = []
        for c in names:
            try:
                values = self.label_encoders[c].transform(X[c].astype(str))
                o = self.one_hot_encoders[c].transform(
                    values.reshape(len(values), 1))
            except (KeyError, ValueError):
                o = np.zeros((len(X), len(self.label_encoders[c].classes_)))
            one_hots.append(o)
        return np.concatenate(one_hots, axis=1)
