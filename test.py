import pytest
from calcul.calculator import Calculator

cal = Calculator()

def testik_passing():
    assert cal.summary(4, 5) == 9
def tested_passing():
    assert cal.ne_summary(3, 2) == 1
def testyd_passing():
    assert cal.multiply(3, 2) == 6
def testob_passing():
    assert cal.ne_muptiply_s_ostatkom(3,   1) == 3
def test_passobie():
    assert cal.ne_multiply_bez_ostatka(3, 2) == 1
