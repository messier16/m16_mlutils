from unittest import TestCase
import pandas as pd

from  m16_mlutils.pipeline import DataFrameSelector


class test_DataFrameSelector(TestCase):

    def test_selects_right_columns(self):
    
        A, B, C = list(range(10)), list(range(5, 15)), list(range(-1, 9))
        expected = pd.DataFrame({ 'A': A, 'C': C })

        full = pd.DataFrame({ 'A': A, 'B': B, 'C': C })
        selector = DataFrameSelector(['A', 'C'])
        actual = selector.fit_transform(full)

        self.assertTrue(expected.equals(actual))
        