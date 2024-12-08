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
    Given a 0-indexed 2D integer array of events where
    event[i] = [startTimei, endTimei, valuei]. The ith event starts at
    startTimei and ends at entTimei, and if the event it attended a value of
    valuei is obtained. Choose up to two non-overlapping events to attend such
    the sum of their values is maximized.

    Return the maximum sum.

    Note that the start time and end time is inclusive: that is it is impossible
    to attend two events where one starts and the other ends at the same time.
    More specifically, if an event is attended with end time t, the next event
    must start at or after t + 1.
    '''
    # does not grab the hightest value event
    def maxTwoEvents_fails(self, events: List[List[int]]) -> int:
        answer = 0
        events.sort(key=lambda i:(i[0],i[1],-i[2]))
        for a,b,c in events:
            i = bisect.bisect(events, b, key=lambda i: i[0])
            if i < len(events):
                answer = max(answer, c + events[i][2])
            else:
                answer = max(answer, c)
        return answer

    # dp does not work correctly
    def maxTwoEvents_fails(self, events: List[List[int]]) -> int:
        answer = 0
        events.sort(key=lambda i:(i[0],i[1],-i[2]))
        @cache
        def dp(start):
            i = bisect.bisect_left(events, start, key=lambda i: i[0])
            if i == len(events):
                return 0
            if i == len(events) - 1:
                return events[i][2]
            return max(events[i][2], dp(events[i+1][0]))
        for _,b,c in events:
            d = dp(b+1)
            answer = max(answer, c + d)
        return answer

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        answer = 0
        events.sort()
        @cache
        def dp(i):
            if i == len(events):
                return 0
            return max(events[i][2], dp(i+1))
        # for i in len(events):
        #     dp(i)
        # d = [dp(i) for i in range(len(events))]
        for i in range(len(events)):
            j = bisect.bisect_left(events, events[i][1] + 1, key=lambda i: i[0])
            answer = max(answer, events[i][2] + dp(j))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,3,2],[4,5,2],[2,4,3]]
        o = 4
        self.assertEqual(s.maxTwoEvents(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,3,2],[4,5,2],[1,5,5]]
        o = 5
        self.assertEqual(s.maxTwoEvents(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,5,3],[1,5,1],[6,6,5]]
        o = 8
        self.assertEqual(s.maxTwoEvents(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,2,8],[3,10,1],[3,10,2],[3,10,3]]
        o = 11
        self.assertEqual(s.maxTwoEvents(i), o)

    def test_five(self):
        s = Solution()
        i = [[1,2,8],[3,10,1],[3,10,2],[4,10,3]]
        o = 11
        self.assertEqual(s.maxTwoEvents(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)