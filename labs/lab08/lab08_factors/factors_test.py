from factors import factors, is_prime
from hypothesis import given, strategies
import pytest

def test_error():
    with pytest.raises(ValueError):
        list(factors(0)) 

def test_primes():
    assert list(factors(7)) == [7]
    assert list(factors(11)) == [11]
    assert list(factors(13)) == [13]

def test_normal():
    assert list(factors(12)) == [2,2,3]
    assert list(factors(72)) == [2,2,2,3,3]
    assert list(factors(84)) == [2,2,3,7]
