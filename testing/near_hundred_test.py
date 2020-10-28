import pytest
from programs import near_hundred

def test_near_hundred_true():
    assert near_hundred.near_hundred(95) == True
def test_near_hundred_false():
    assert near_hundred.near_hundred(50) == False