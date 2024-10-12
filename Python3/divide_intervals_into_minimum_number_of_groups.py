# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array intervals where intervals[i] = [lefti, righti]
    represents the inclusive interval [lefti, righti].

    Divide the intervals into one of more groups such that each interval is in
    exactly one group, and no two intervals that are in the same group intersect
    each other.

    Return the minimum number of groups needed.

    Two intervals intersect if there is at least one common number between them.
    For example, the intervals [1, 5] and [5, 8] intersect.
    '''
    # hints really helped with this
    # that and line-scan was an answer to a recent-ish problem
    def minGroups(self, intervals: List[List[int]]) -> int:
        answer = 0
        count = 0
        s = []
        for i,j in sorted(intervals):
            while s and s[0] < i:
                heapq.heappop(s)
                answer = max(answer, count)
                count -= 1
            heapq.heappush(s, j)
            count += 1
        return max(answer, count)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[5,10],[6,8],[1,5],[2,3],[1,10]]
        o = 3
        self.assertEqual(s.minGroups(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,3],[5,6],[8,10],[11,13]]
        o = 1
        self.assertEqual(s.minGroups(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)