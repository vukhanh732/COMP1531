from primes import factors

def test_zero():
    assert(factors(0) == [])

def test_small():
    assert(factors(2) == [2])
    assert(factors(8) == [2, 2, 2])

def test_prime():
        assert(factors(13) == [13])

def test_big():
    assert(factors(870) == [2, 3, 5, 29])