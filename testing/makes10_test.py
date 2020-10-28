import pytest
from programs import makes10

def test_makes10_does():
    assert makes10.makes10(1,9) == True
def test_makes10_doesnot():
    assert makes10.makes10(12, 4) == False