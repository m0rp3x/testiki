import pytest

x = 2
y = 3

result1 = x * y

result2 = x + y

result3 = x - y

result4 = x / y

result5 = x // y


def test_summary():
    assert x + y == 5
    assert x * y == 6
    assert x - y == -1
    assert x / y == 0.6666666666666666
    assert x // y == 0
