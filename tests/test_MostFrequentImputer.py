import pandas as pd

from m16_mlutils.pipeline import MostFrequentImputer


def test_imputes_correct_value():
    inputValues1 = ['A', 'A', None, 'B']
    expectedValues1 = ['A', 'A', 'A', 'B']

    inputValues2 = ['1', '2', None, '1']
    expectedValues2 = ['1', '2', '1', '1']

    missingData = pd.DataFrame({
        'values1': inputValues1,
        'values2': inputValues2
    })

    expected = pd.DataFrame({
        'values1': expectedValues1,
        'values2': expectedValues2
    })

    imputer = MostFrequentImputer()

    actual = imputer.fit_transform(missingData)

    assert expected.equals(actual)
