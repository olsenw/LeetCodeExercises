# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array events where events[i] = [startDayi, endDayi]. Every event i
    starts at startDayi and ends at endDayi.

    It is possible to attend an an event i at any day d where
    startTimei <= d <= endTimei. Only one event can be attended for a given d.

    Return the maximum number of events that can be attended.
    '''
    # single possible event in middle of longer events
    def maxEvents_fails(self, events: List[List[int]]) -> int:
        heapq.heapify(events)
        day = 1
        answer = 0
        while events:
            s,e = heapq.heappop(events)
            if day < s:
                day = s
            if s <= day <= e:
                day += 1
                answer += 1
        return answer

    # attempt at using hints
    def maxEvents_fail(self, events: List[List[int]]) -> int:
        events.sort()
        days = set()
        answer = 0
        for s,e in events:
            for d in range(e,s-1,-1):
                if d not in days:
                    days.add(d)
                    answer += 1
                    break
        return answer

    # does not account for large end times extending farther past earlier event starts
    def maxEvents_failure(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:(x[1],x[0]))
        answer = 0
        day = 0
        for s,e in events:
            if day < s:
                day = s
            if s <= day <= e:
                day += 1
                answer += 1
        return answer

    def maxEvents_fail_fail(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:(x[1],-x[0]))
        days = set()
        for s,e in events:
            for d in range(e,s-1,-1):
                if d not in days:
                    days.add(d)
                    break
        return len(days)

    # based on Editorial
    # https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/editorial/?envType=daily-question&envId=2025-07-07
    def maxEvents(self, events: List[List[int]]) -> int:
        answer = 0
        events.sort()
        e = 0
        # currently possible events
        h = []
        # iterate all days from 1 to max end date
        for day in range(1, max(e[1] for e in events) + 1):
            # add possible events onto the heap
            while e < len(events) and events[e][0] <= day:
                heapq.heappush(h, events[e][1])
                e += 1
            # remove impossible events from heap
            while h and h[0] < day:
                heapq.heappop(h)
            # remove event being attended on day
            if h:
                heapq.heappop(h)
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,3],[3,4]]
        o = 3
        self.assertEqual(s.maxEvents(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[2,3],[3,4],[1,2]]
        o = 4
        self.assertEqual(s.maxEvents(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,4],[4,4],[2,2],[3,4],[1,1]]
        o = 4
        self.assertEqual(s.maxEvents(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,2],[1,2],[3,3],[1,5],[1,5]]
        o = 5
        self.assertEqual(s.maxEvents(i), o)

    def test_five(self):
        s = Solution()
        i = [[1,2],[2,2],[3,3],[3,4],[3,4]]
        o = 4
        self.assertEqual(s.maxEvents(i), o)

    def test_six(self):
        s = Solution()
        i = [[1,5],[1,5],[1,5],[2,3],[2,3]]
        o = 5
        self.assertEqual(s.maxEvents(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)