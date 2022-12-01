from inverse import inverse
from hypothesis import given, strategies

def test_empty():
    assert inverse({}) == {}

def test_given_example():
    assert inverse({1: 'A', 2: 'B', 3: 'A'}) == {'A': [1, 3], 'B': [2]}

    

