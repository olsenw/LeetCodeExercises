# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a floating-point number hour, representing the amount of time a person
    has to reach the office. To commute to the office, n trains in sequential
    order. Also given is an integer array dist of length n, where dist[i]
    describes the distance (in kilometers) of the ith train ride.

    Each train can only depart at an integer hour, so there may be a wait
    between each train ride.

    Return the minimum positive integer speed (in kilometers per hour) that all
    the trains must travel at for the person to reach the office on time, or -1
    if it is impossible to be on time.

    Tests are generated such that the answer will not exceed 10^7 and hour will
    have at most two digits.
    '''
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def valid(speed:int) -> bool:
            return sum(math.ceil(d / speed) for d in dist[:-1]) + (dist[-1] / speed) <= hour
        a = -1
        i,j = 1, 10**7 + 1
        while i <= j:
            k = (i + j) // 2
            if valid(k):
                a = k
                j = k - 1
            else:
                i = k + 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2]
        j = 6.0
        o = 1
        self.assertEqual(s.minSpeedOnTime(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,3,2]
        j = 2.7
        o = 3
        self.assertEqual(s.minSpeedOnTime(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,3,2]
        j = 1.9
        o = -1
        self.assertEqual(s.minSpeedOnTime(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)