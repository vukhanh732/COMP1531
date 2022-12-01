'''
Tests for reverse_words()
'''
from reverse import reverse_words

def test_example():
    assert reverse_words(["Hello World", "I am here"]) == ['World Hello', 'here am I']

def test_one_string():
    assert reverse_words(["This is a test"]) == ["test a is This"]

def test_empty():
    assert reverse_words([]) == []

def test_one_word():
    assert reverse_words(["A", "Test"]) == ["A", "Test"]

def test_numbers():
    assert reverse_words(["1 2 3 4", "8 7 6 5"]) == ["4 3 2 1", "5 6 7 8"]
    assert reverse_words(["1 a 2 b", "3 c 4 d"]) == ["b 2 a 1", "d 4 c 3"]