import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

from m16_mlutils.pipeline import CategoryEncoder, DataFrameSelector
from .NumPyTestCase import NumPyTestCase


class test_IntegrationWithPipeline(NumPyTestCase):

    def test_pipeline(self):
        test = pd.read_csv("./tests/fakedata/test.csv")

        categorical_columns = [
            "HouseStyle",
            "Foundation",
            "KitchenQual",
            "ExterQual",
            "ExterCond",
            'Exterior1st',
            "LotShape"
        ]

        unique_values = 0
        # Count the number of different values as that is
        # the number of columns in the transformed data frame
        for column in categorical_columns:
            unique_values += len(test[column].unique())

        categorical_pipeline = Pipeline([
            ("selector", DataFrameSelector(categorical_columns)),
            ("encoder", CategoryEncoder())
        ])

        matrix = categorical_pipeline.fit_transform(test)

        assert matrix.shape == (len(test), unique_values)
