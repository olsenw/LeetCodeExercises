# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array events where events[i] = [startDayi, endDayi, valuei]. The
    ith event starts at startDayi and ends at endDayi, and if the event is
    attended a value of valuei will be awarded. Also given an integer k which
    represents the maximum number of events that can be attended.

    It is only possible to attend one event at a time. If an event is attended,
    the event takes the full duration. Note that the end day is inclusive (ie it
    is not possible to attend two events where one of the starts and the other
    ends on the same day).

    Return the maximum sum of values that can received by attending events.
    '''
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        @cache
        def dp(index, attend):
            if index == len(events) or attend == k:
                return 0
            # take index course
            j = bisect.bisect_left(events, events[index][1] + 1, key=lambda x:x[0])
            a = dp(j, attend + 1) + events[index][2]
            # do not take index course
            b = dp(index + 1, attend)
            return max(a,b)
        return dp(0,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,4],[3,4,3],[2,3,1]]
        j = 2
        o = 7
        self.assertEqual(s.maxValue(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,4],[3,4,3],[2,3,10]]
        j = 2
        o = 10
        self.assertEqual(s.maxValue(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
        j = 3
        o = 9
        self.assertEqual(s.maxValue(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)