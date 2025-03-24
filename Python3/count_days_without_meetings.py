# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer days representing the total number days an employee
    is available for work (starting from day 1). Also given a 2D array meetings
    of size n where meetings[i] = [start_i, end_i] represents the starting and
    ending days of meeting i (inclusive).

    Return the count of days when the employee is available for work but no
    meetings are scheduled.

    Note: the meetings may overlap.
    '''
    def countDays_tle(self, days: int, meetings: List[List[int]]) -> int:
        answer = 0
        meetings.sort()
        m = 0
        queue = []
        for d in range(1, days + 1):
            while queue and queue[0] < d:
                heapq.heappop(queue)
            while m < len(meetings) and meetings[m][0] == d:
                heapq.heappush(queue, meetings[m][1])
                m += 1
            if len(queue) == 0:
                answer += 1
        return answer

    def countDays_passes(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        m = 0
        queue = []
        answer = meetings[0][0] - 1
        while m < len(meetings):
            s,e = meetings[m]
            last = s
            while queue and queue[0] < s:
                last = heapq.heappop(queue)
            if not queue:
                answer += max(0, s - last - 1)
            heapq.heappush(queue, e)
            m += 1
        last = days
        while queue:
            last = heapq.heappop(queue)
        answer += days - last
        return answer

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        last = 0
        answer = 0
        for s,e in meetings:
            if last < s:
                answer += max(s - last - 1, 0)
            last = max(last, e)
            pass
        answer += days - last
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10
        j = [[5,7],[1,3],[9,10]]
        o = 2
        self.assertEqual(s.countDays(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [[2,4],[1,3]]
        o = 1
        self.assertEqual(s.countDays(i,j), o)

    def test_three(self):
        s = Solution()
        i = 6
        j = [[1,6]]
        o = 0
        self.assertEqual(s.countDays(i,j), o)

    def test_four(self):
        s = Solution()
        i = 1000000000
        j = [[1,1000000000]]
        o = 0
        self.assertEqual(s.countDays(i,j), o)

    def test_five(self):
        s = Solution()
        i = 20
        j = [[1,4],[2,6],[10,12],[16,18]]
        o = 8
        self.assertEqual(s.countDays(i,j), o)

    def test_six(self):
        s = Solution()
        i = 8
        j = [[3,4],[4,8],[2,5],[3,8]]
        o = 1
        self.assertEqual(s.countDays(i,j), o)

    def test_seven(self):
        s = Solution()
        i = 14
        j = [[6,11],[7,13],[8,9],[5,8],[3,13],[11,13],[1,3],[5,10],[8,13],[3,9]]
        o = 1
        self.assertEqual(s.countDays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)