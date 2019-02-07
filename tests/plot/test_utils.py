import pytest

from m16_mlutils.plot.utils import get_rows_columns


@pytest.mark.parametrize('items,columns,expected', [
    (3, 3, (1, 3)),
    (3, 1, (3, 1)),
    (1, 3, (1, 1)),
    (6, 3, (2, 3)),
    (7, 3, (3, 3)),
])
def test_get_rows_columns(items, columns, expected):
    actual = get_rows_columns(items, columns)
    assert actual == expected
