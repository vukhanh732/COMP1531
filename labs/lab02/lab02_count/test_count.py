from count import count_char

def test_empty():
    assert count_char("") == {}

def test_simple():
    assert count_char("abc") == {"a": 1, "b": 1, "c": 1}

def test_double():
    assert count_char("aa") == {"a": 2}

def test_upper_lower():
    assert count_char("ooO") == {"o": 2, "O": 1}

def test_special_char():
    assert count_char("!!!") == {"!": 3}

