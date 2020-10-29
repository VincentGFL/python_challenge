import pytest
from programs import not_string

def test_not_string_add():
    assert not_string.not_string("andy dandy") == "not andy dandy"
def test_not_string_same():
    assert not_string.not_string("not so true") == "not so true"