from .NumPyTestCase import NumPyTestCase
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
import os

from m16_mlutils.pipeline import DataFrameSelector, CategoryEncoder

class test_IntegrationWithPipeline(NumPyTestCase):

    def test_pipeline(self):

        train = pd.read_csv("./tests/fakedata/train.csv")
        test = pd.read_csv("./tests/fakedata/test.csv")


        categorical_pipeline = Pipeline([
            ("selector", DataFrameSelector([
                "HouseStyle","Foundation","KitchenQual","ExterQual","ExterCond",'Exterior1st',"LotShape"])),
            ("encoder",  CategoryEncoder())
        ])


        print(np.unique(test['HouseStyle']))
        print(np.unique(test['Foundation']))
        print(np.unique(test['KitchenQual']))
        print(np.unique(test['ExterQual']))
        #categorical_pipeline.fit(train)

        #print(categorical_pipeline.transform(test))
        print("RRR")
        print(test['ExterQual'])