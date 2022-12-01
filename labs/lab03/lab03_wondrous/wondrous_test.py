import pytest
from wondrous import wondrous

def test_basic():
    assert wondrous(3) == [3, 10, 5, 16, 8, 4, 2, 1]

def test_0():
    with pytest.raises(Exception):
        assert wondrous(0)

def test_1():
    assert wondrous(1) == [1]

def test_negative():
    with pytest.raises(Exception):
        assert wondrous(-1)
