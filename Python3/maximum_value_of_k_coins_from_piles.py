# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n piles of coins on a table. Each pile consists of a positive
    number of coins of assorted denominations.

    In one move, it possible to take a coin from the top of any pile and add it
    to a wallet.

    Given a list piles, where piles[i] is a list of integers denoting the
    composition of the ith pile from top to bottom, and a positive integer k,
    return the maximum total value of coins in a wallet if k coins are optimally
    chosen.
    '''
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        p = [list(accumulate(p)) for p in piles]
        @cache
        def dp(i:int, r:int) -> int:
            if i == len(p) or r == 0:
                return 0
            a = dp(i+1,r)
            for j in range(min(r,len(p[i]))):
                a = max(a, p[i][j] + dp(i+1,r-j-1))
            return a
        return dp(0,k)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,100,3],[7,8,9]]
        j = 2
        o = 101
        self.assertEqual(s.maxValueOfCoins(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]
        j = 7
        o = 706
        self.assertEqual(s.maxValueOfCoins(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]]
        j = 9
        o = 494
        self.assertEqual(s.maxValueOfCoins(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)