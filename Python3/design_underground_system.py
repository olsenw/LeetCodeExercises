# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

'''
An underground railway system is keeping track of customer travel times
between different stations. They are using this data to calculate the
average time it takes to travel from one station to another.

See method comments for what implementation should do.

It is assumed that all calls made to checkIn and checkOut methods are
consistent. If a customer checks in at time t1 then checks out at time
t2, then t1 < t2. All events happen in chronological order.
'''
class UndergroundSystem:

    def __init__(self):
        # id -> (station, time)
        self.checkIns = dict()
        # (station, station) -> [accumulator, customers]
        self.travel = dict()

    '''
    A customer with card ID equal to id, checks in at the station
    stationName at time t.
    A customer can only be checked into one place at a time.
    '''
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    '''
    A customer with card ID equal to id, checks out from the station
    stationName at time t.
    '''
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, start = self.checkIns[id]
        k = (startStation, stationName)
        if k in self.travel:
            self.travel[k][0] += t - start
            self.travel[k][1] += 1
        else:
            self.travel[k] = [t - start, 1]

    '''
    Returns the average time it takes to travel from startStation to
    endStation.

    The average time is computed from all the previous traveling times
    from startStation to endStation that happened directly, meaning a
    check in at startStation followed by a check out from endStation.

    The time it takes to travel from startStation to endStation may be
    different from the time it takes to travel from endStation to
    startStation.

    There will be at least one customer that has traveled from
    startStation to endStation before getAverage is called.
    '''
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        n, d = self.travel[(startStation, endStation)]
        return n / d

class UnitTesting(unittest.TestCase):
    # Your UndergroundSystem object will be instantiated and called as such:
    # obj = UndergroundSystem()
    # obj.checkIn(id,stationName,t)
    # obj.checkOut(id,stationName,t)
    # param_3 = obj.getAverageTime(startStation,endStation)

    def test_one(self):
        s = UndergroundSystem()
        s.checkIn(45, "Leyton", 3)
        s.checkIn(32, "Paradise", 8)
        s.checkIn(27, "Leyton", 10)
        s.checkOut(45, "Waterloo", 15)
        s.checkOut(27, "Waterloo", 20)
        s.checkOut(32, "Cambridge", 22)
        self.assertEqual(s.getAverageTime("Paradise", "Cambridge"), 14.0)
        self.assertEqual(s.getAverageTime("Leyton", "Waterloo"), 11.0)
        s.checkIn(10, "Leyton", 24)
        self.assertEqual(s.getAverageTime("Leyton", "Waterloo"), 11.0)
        s.checkOut(10, "Waterloo", 38)
        self.assertEqual(s.getAverageTime("Leyton", "Waterloo"), 12.0)

    def test_two(self):
        s = UndergroundSystem()
        s.checkIn(10, "Leyton", 3)
        s.checkOut(10, "Paradise", 8)
        self.assertEqual(s.getAverageTime("Leyton", "Paradise"), 5.0)
        s.checkIn(5, "Leyton", 10)
        s.checkOut(5, "Paradise", 16)
        self.assertEqual(s.getAverageTime("Leyton", "Paradise"), 5.5)
        s.checkIn(2, "Leyton", 21)
        s.checkOut(2, "Paradise", 30)
        self.assertEqual(s.getAverageTime("Leyton", "Paradise"), 20 / 3)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)