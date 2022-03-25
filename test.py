import pytest
from app.calculator import Сalculator

cal = Сalculator()

def test_passing():
    assert cal.summary(4, 5) == 9
    assert cal.otnimanie(3, 2) == 1
    assert cal.ymnogenie(3, 2) == 6
    assert cal.delenie_ostatok(3, 2) == 1.5
    assert cal.delenie_bez_ostatka(3, 2) == 1


