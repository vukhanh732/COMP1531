import pytest
from timetable import timetable 
from datetime import date, time, datetime

def test_1():
    assert timetable([date(2019,9,27), date(2019,9,30)], [time(14,10), time(10,30)]) == [datetime(2019,9,27,10,30), datetime(2019,9,27,14,10), datetime(2019,9,30,10,30), datetime(2019,9,30,14,10)]
   
def test_2():
     assert timetable([date(2021,3,25)], [time(15,10), time(20,30)]) == [datetime(2021,3,25,15,10), datetime(2021,3,25,20,30)]