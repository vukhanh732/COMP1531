from mono import monotonic

def test_1():
    data = [(1,3,2),(1,2)]
    out = ['neither', 'monotonically increasing']
    assert monotonic(data) == out

def test_2():
    data = [(1,1,1),(6,5,4,3)]
    out = ['neither', 'monotonically descreasing']
    assert monotonic(data) == out
