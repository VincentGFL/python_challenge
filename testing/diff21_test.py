import pytest
from programs import diff21

def test_diff21_under():
    assert diff21.diff21(10) == 11
def test_diff21_on():
    assert diff21.diff21(21) == 0
def test_diff21_over():
    assert diff21.diff21(50) == 58