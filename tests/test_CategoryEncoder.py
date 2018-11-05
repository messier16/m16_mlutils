import pandas as pd

from m16_mlutils.pipeline import CategoryEncoder
from .NumPyTestCase import NumPyTestCase


class test_CategoryEncoder(NumPyTestCase):

    def test_two_categories(self):
        categoricalValues = ['s', 'n', 's', 's']
        expected = self.array([
            [0, 1],
            [1, 0],
            [0, 1],
            [0, 1]
        ])

        encoder = CategoryEncoder()

        actual = encoder.fit_transform(pd.DataFrame({
            'v': categoricalValues
        }))

        self.assertArrayEqual(expected, actual)

    def test_three_categories_custom_unobserved_labels(self):
        categoricalValues = ['s', 'n', 's', 's']
        expected = self.array([
            [0, 0, 1],
            [0, 1, 0],
            [0, 0, 1],
            [0, 0, 1]
        ])

        encoder = CategoryEncoder(labels={'v': ['s', 'n', 'a']})

        actual = encoder.fit_transform(pd.DataFrame({
            'v': categoricalValues
        }))

        self.assertArrayEqual(expected, actual)

    def test_three_categories(self):
        categoricalValues = ['a', 'b', 'c', 'b', 'a', 'c']
        expected = self.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])

        encoder = CategoryEncoder()

        actual = encoder.fit_transform(pd.DataFrame({
            'v': categoricalValues
        }))

        self.assertArrayEqual(expected, actual)

    def test_two_categorical_columns(self):
        categoricalValues1 = ['a', 'b', 'c', 'b', 'a', 'c']
        categoricalValues2 = ['x', 'y', 'z', 'y', 'x', 'z']
        expected = self.array([
            [1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 1],
            [0, 1, 0, 0, 1, 0],
            [1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1]
        ])

        encoder = CategoryEncoder()

        actual = encoder.fit_transform(pd.DataFrame({
            'v1': categoricalValues1,
            'v2': categoricalValues2
        }))

        self.assertArrayEqual(expected, actual)

    def test_previously_unseen(self):
        train = pd.DataFrame({
            'l': ['a', 'b', 'c', 'a']
        })

        test = pd.DataFrame({
            'l': ['z', 'y']
        })

        encoder = CategoryEncoder()

        expected = self.array([
            [0, 0, 0],
            [0, 0, 0],
        ])

        encoder.fit(train)
        actual = encoder.transform(test)

        self.assertArrayEqual(expected, actual)
