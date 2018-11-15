from unittest import TestCase

import pandas as pd

from m16_mlutils.pipeline import DataFrameSelector


class test_DataFrameSelector(TestCase):

    def test_selects_right_columns(self):
        A, B, C = list(range(10)), list(range(5, 15)), list(range(-1, 9))
        expected = pd.DataFrame({'A': A, 'C': C})

        full = pd.DataFrame({'A': A, 'B': B, 'C': C})
        selector = DataFrameSelector(['A', 'C'])
        actual = selector.fit_transform(full)

        pd.testing.assert_frame_equal(actual, expected)

    def test_select_single_column(self):
        A, B, C = list(range(10)), list(range(5, 15)), list(range(-1, 9))

        full = pd.DataFrame({'A': A, 'B': B, 'C': C})
        expected = full[['A']].copy()
        selector = DataFrameSelector(['A'])
        actual = selector.fit_transform(full)

        pd.testing.assert_frame_equal(actual, expected)

    def test_select_series(self):
        A, B, C = list(range(10)), list(range(5, 15)), list(range(-1, 9))

        full = pd.DataFrame({'A': A, 'B': B, 'C': C})
        expected = full['A'].copy()
        selector = DataFrameSelector('A')
        actual = selector.fit_transform(full)

        pd.testing.assert_series_equal(actual, expected)
