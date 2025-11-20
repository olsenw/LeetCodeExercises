# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array intervals where intervals[i] = [starti, endi]
    represents all the integers from starti to endi inclusively.

    A containing set is an array nums where each interval from intervals has at
    least two integers in nums.

    Return the minimum possible size of a containing set.
    '''
    # based on leetcode editorial
    # https://leetcode.com/problems/set-intersection-size-at-least-two/?envType=daily-question&envId=2025-11-20
    # smart sorting prevents clashes
    # also tracks if two numbers have possibly been removed from given set already
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        todo = [2] * len(intervals)
        ans = 0
        while intervals:
            (s, e), t = intervals.pop(), todo.pop()
            # this is short circuited if nothing todo (ie two numbers already picked)
            for p in range(s, s+t):
                for i, (s0, e0) in enumerate(intervals):
                    if todo[i] and p <= e0:
                        todo[i] -= 1
                ans += 1
        return ans

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,3],[3,7],[8,9]]
        o = 5
        self.assertEqual(s.intersectionSizeTwo(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,3],[1,4],[2,5],[3,5]]
        o = 3
        self.assertEqual(s.intersectionSizeTwo(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2],[2,3],[2,4],[4,5]]
        o = 5
        self.assertEqual(s.intersectionSizeTwo(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)