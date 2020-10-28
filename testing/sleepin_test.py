import pytest  
from programs import sleepin

def test_sleep_in_tt():
    assert sleepin.sleep_in(True, True) == True, True