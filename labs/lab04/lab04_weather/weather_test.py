import pytest
from weather import weather

def test_spec():
    assert weather('08-08-2010','Albury') == (10.8, 10.0)

def test_na_min_temp():
    assert weather("11-09-2009", "Albury") == (None, None)

def test_na_max_temp():
    assert weather("07-09-2016", "CoffsHarbour") == (None, None)

def test_invalid_town():
    assert weather('20-01-2010', '') == (None, None)

def test_newcastle():
    # avg_min = 13.7, avg_max = 24.1
    result = weather("04-12-2008", "Newcastle")
    assert (round(result[0], 1), round(result[1], 1)) == (5.5, 0.1)