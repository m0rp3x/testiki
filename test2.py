import pytest
from app.calculator import Сalculator

cal = Сalculator()

def test_faild():
    assert cal.summary(4, 5) == 3
    assert cal.otnimanie(3, 2) == 2
    assert cal.ymnogenie(3, 2) == 3
    assert cal.delenie_ostatok(3, 2) == 3
    assert cal.delenie_bez_ostatka(3, 2) == 0

