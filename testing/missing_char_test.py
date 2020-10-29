import pytest
from programs import missing_char

def test_missing_char():
    assert missing_char.missing_char("Hello", 1) == "Hllo"