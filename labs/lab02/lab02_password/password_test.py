'''
Tests for check_password()
'''
from password import check_password

def test_horrible_password():
    assert(check_password("password")) == "Horrible password"
    assert(check_password("iloveyou")) == "Horrible password"
    assert(check_password("123456")) == "Horrible password"

def test_strong_password():
    assert(check_password("1234567891011Ab")) == "Strong password"

def test_moderate_password():
    assert(check_password("12345678a")) == "Moderate password"

def test_poor_password():
    assert(check_password("1234567")) == "Poor password"