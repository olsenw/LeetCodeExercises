# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer arrivalTime denoting the arrival time of a train in
    hours, and another positive integer delayedTime denoting the amount of delay
    in hours.

    Return the time the train will arrive at the station.

    Note that the time in this problem is in 24-hours format.
    '''
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 13
        j = 11
        o = 0
        self.assertEqual(s.findDelayedArrivalTime(i,j), o)

    def test_two(self):
        s = Solution()
        i = 15
        j = 5
        o = 20
        self.assertEqual(s.findDelayedArrivalTime(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)