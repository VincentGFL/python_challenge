import pytest
from programs import array_count9

def test_array_count9():
    assert array_count9.array_count9([1,2,3,9,9,9]) == 3
