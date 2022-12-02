from filter import filter_string
import pytest

def test_1():
    assert(filter_string("Hello, my name is Mr O'Toole.") == "Hello my name is mr otoole")

def test_2():
    assert(filter_string("this, is, a, test") == "This is a test")

def test_err():
    with pytest.raises(ValueError):
        filter_string("123") 
