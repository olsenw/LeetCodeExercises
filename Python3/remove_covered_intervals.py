# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array intervals where intervals[i] = [li, ri] represents 
    the interval [li, ri), remove all intervals that are covered by
    another interval in the list.

    The interval [a,b) is covered by the interval [c,d) if and only if
    c <= a and b <= d.

    Return the number of remaining intervals
    '''
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        import heapq
        heapq.heapify(intervals)
        covered = 0
        a,b = heapq.heappop(intervals)
        while intervals:
            c,d = heapq.heappop(intervals)
            # new covers current
            if c <= a and b <= d:
                a,b = c,d
            # new interval
            elif b < d:
                covered += 1
                a,b = c,d
        return covered + 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,4],[3,6],[2,8]]
        o = 2
        self.assertEqual(s.removeCoveredIntervals(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,4],[2,3]]
        o = 1
        self.assertEqual(s.removeCoveredIntervals(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,4]]
        o = 1
        self.assertEqual(s.removeCoveredIntervals(i), o)

    def test_four(self):
        s = Solution()
        i = [[3,10],[4,10],[5,11]]
        o = 2
        self.assertEqual(s.removeCoveredIntervals(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)