import pytest
from programs import sumdouble

def test_sumdouble_diff():
    assert sumdouble.sum_double(5,7) == 12
def test_sumdouble_same():
    assert sumdouble.sum_double(5,5) == 20