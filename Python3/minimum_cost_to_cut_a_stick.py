# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a wooden stick of length n units. The stick is labelled from 0 to n.

    Given an integer array cuts where cuts[i] denotes a position where a cut
    should occur.

    The order of the cuts can be changed.

    The cost of one cut is the length of the stick to be cut, the total cost is
    the sum of costs of all cuts. When the stick is cut, it is split into two
    smaller sticks (ie the sum of their lengths is the length of the stick
    before the cut).

    Return the minimum total cost of the cuts.
    '''
    # leetcode hint gives recurrence relation...
    def minCost(self, n: int, cuts: List[int]) -> int:
        # dp is cost of all cuts between i and j
        @cache
        def dp(i,j):
            a = 10**9
            for k in cuts:
                if i < k < j:
                    a = min(a, dp(i,k) + dp(k,j))
            return 0 if a == 10**9 else a + (j - i)
        return dp(0,n)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 7
        j = [1,3,4,5]
        o = 16
        self.assertEqual(s.minCost(i,j), o)

    def test_two(self):
        s = Solution()
        i = 9
        j = [5,6,1,4,2]
        o = 22
        self.assertEqual(s.minCost(i,j), o)

    def test_three(self):
        s = Solution()
        i = 2
        j = [1]
        o = 2
        self.assertEqual(s.minCost(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)