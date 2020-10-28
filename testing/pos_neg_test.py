import pytest
from programs import pos_neg

def test_pos_neg_pnf():
    assert pos_neg.pos_neg(1, -1, False) == True
def test_pos_neg_npf():
    assert pos_neg.pos_neg(-1, 1, False) == True
def test_pos_neg_nnt():
    assert pos_neg.pos_neg(-1, -1, True) == True    