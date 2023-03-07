# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array time where time[i] denotes the time taken by the ith bus to
    complete one trip.

    Each bus can make multiple trips successively; that is, the next trip can
    start immediately after completing the current trip. Also, each bus operates
    independently; that is, the trips of one bus do not influence the trips of
    any other bus.

    Given an integer totalTrips, which denotes the number of trips all buses
    should make in total. Return the minimum time required for all buses to
    complete at least totalTrips trips.
    '''
    def minimumTime_slow(self, time: List[int], totalTrips: int) -> int:
        i,j = 1, 10**14 + 1
        while i <= j:
            k = (j - i) // 2 + i
            t = sum(k // b for b in time)
            if t < totalTrips:
                i = k + 1
            else:
                j = k - 1
        return i

    # from sample 1853 ms submission on LeetCode
    # better calc for upper bound
    def minimumTime_fast(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 1, min(time) * totalTrips
        while lo < hi:
            mt = lo + (hi - lo) // 2
            trips_count = sum(mt // t for t in time)
            if trips_count < totalTrips:
                lo = mt + 1
            else:
                hi = mt
        return lo

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        j = 5
        o = 3
        self.assertEqual(s.minimumTime(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2]
        j = 1
        o = 2
        self.assertEqual(s.minimumTime(i,j), o)

    def test_three(self):
        s = Solution()
        i = [10000000]
        j = 10000000
        o = 100000000000000
        self.assertEqual(s.minimumTime(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)