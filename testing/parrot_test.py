import pytest
from programs import parrot

def test_parrot_speak():
    assert parrot.parrot_trouble(True, 5) == True
def test_parrot_nospeak():
    assert parrot.parrot_trouble(False, 10) == False
