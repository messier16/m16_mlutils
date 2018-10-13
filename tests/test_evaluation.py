from m16_mlutils.datatools.evaluation import eval_summary

from .NumPyTestCase import NumPyTestCase


class test_evaluation(NumPyTestCase):

    def test_eval_summary(self):
        y_true = [True, True, True, False]
        y_pred = [True, True, True, False]

        summary, report, matrix = eval_summary(y_true, y_pred)

        assert matrix.shape == (2, 2)
        assert report
        assert len(summary) == 4
        assert summary['precision'] == 1
