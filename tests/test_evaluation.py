from m16_mlutils.datatools.evaluation import eval_summary


def test_eval_summary_matrix_expected():
    y_true = [True, True, True, False]
    y_pred = [True, True, True, False]

    summary, report, matrix = eval_summary(y_true, y_pred, need_matrix=True)

    assert matrix.shape == (2, 2)
    assert report
    assert len(summary) == 4
    assert summary['precision'] == 1


def test_eval_summary():
    y_true = [True, True, True, False]
    y_pred = [True, True, True, False]

    summary, report, matrix = eval_summary(y_true, y_pred, need_matrix=False)

    assert matrix is None
    assert report
    assert len(summary) == 4
    assert summary['precision'] == 1
