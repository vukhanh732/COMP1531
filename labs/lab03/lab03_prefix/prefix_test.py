from prefix import prefix_search
import pytest

def test_documentation():
    assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a") == { "ac": 1, "ab": 3}

def test_exact_match():
    assert prefix_search({"category": "math", "cat": "animal"}, "cat") == {"category": "math", "cat": "animal"}

def test_number():
    assert prefix_search({"1": "100", "100": "1000", "2":"2000"}, "1") == {"1": "100", "100": "1000"}

def test_error():
    with pytest.raises(KeyError):
        assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "c")