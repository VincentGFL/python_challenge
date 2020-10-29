import pytest
from programs import wrapper

def test_decoration_isupper():
    assert wrapper.string_upper("poggers") == "POGGERS"