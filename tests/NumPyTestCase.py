from unittest import TestCase
import numpy as np


class NumPyTestCase(TestCase):

    def assertArrayEqual(self, expected: np.array, actual: np.array):
        return self.assertTrue(np.array_equal(expected, actual),
                               "The arrays do not match")

    def array(self, array):
        return np.array(array, dtype=np.float32)
