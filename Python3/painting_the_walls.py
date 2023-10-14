# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 0-indexed integer arrays, cost and time, of size n representing
    the costs and the time taken to point n different walls respectively. There
    are two painters available:
    * A paid painter that paints the ith wall in time[i] units of time and takes
      cost[i] units of money.
    * A free painter that paints any wall in 1 unit of time at a cost of 0. But
      the free painter can only be used if the paid painter is already occupied.
    
    Return the minimum amount of money required to paint the n walls.
    '''
    # based on leetcode editorial
    # https://leetcode.com/problems/painting-the-walls/editorial/?envType=daily-question&envId=2023-10-14
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        @cache
        def dp(i, r):
            # no more walls to paint
            if r <= 0:
                return 0
            # no more walls for paid painter
            if i == n:
                return float('inf')
            # paint wall i and time[i] other walls
            a = cost[i] + dp(i + 1, r - 1 - time[i])
            # don't paint wall i
            b = dp(i + 1, r)
            # take the minimum cost
            return min(a,b)
        return dp(0, n)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,2]
        j = [1,2,3,2]
        o = 3
        self.assertEqual(s.paintWalls(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,3,4,2]
        j = [1,1,1,1]
        o = 4
        self.assertEqual(s.paintWalls(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)