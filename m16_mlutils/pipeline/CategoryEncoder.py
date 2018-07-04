from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

import numpy as np
import pandas as pd

class CategoryEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, labels={}):
        self.label_encoders = {}
        self.one_hot_encoders = {}
        self.labels = labels
    
    def fit(self, X, y=None):
        for c in X:
            self.label_encoders[c] = LabelEncoder()
            self.one_hot_encoders[c] = OneHotEncoder(sparse=False)
            if c in self.labels:
                self.label_encoders[c].fit(self.labels[c])
                values = self.label_encoders[c].transform(self.labels[c])
            else:
                self.label_encoders[c].fit(X[c])
                values =  self.label_encoders[c].transform(X[c])
            self.one_hot_encoders[c].fit(values.reshape(len(values),1))
            
        return self

    def transform(self, X):
        one_hots = []
        for c in X:
            values =  self.label_encoders[c].transform(X[c])
            o = self.one_hot_encoders[c].transform(values.reshape(len(values),1))
            one_hots.append(o)
            
        return np.concatenate(one_hots, axis=1)