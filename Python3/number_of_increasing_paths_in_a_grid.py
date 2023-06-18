# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n integer matrix grid, where it is possible to move from a cell
    to any adjacent cell in all four directions.

    Return the number of strictly increasing paths in the grid stating at any 
    cell and ending at any cell. Since the answer may be very large, return it
    modulo 10^9+7.

    Two paths are considered different if they do not have exactly the same
    sequence of visited cells.
    '''
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        m,n = len(grid), len(grid[0])
        @cache
        def dp(i,j):
            a,b,c,d = 0,0,0,0
            if i > 0 and grid[i-1][j] > grid[i][j]:
                a = dp(i-1, j)
            if i < m - 1 and grid[i+1][j] > grid[i][j]:
                b = dp(i+1, j)
            if j > 0 and grid[i][j-1] > grid[i][j]:
                c = dp(i, j-1)
            if j < n - 1 and grid[i][j+1] > grid[i][j]:
                d = dp(i, j+1)
            return (1 + a + b + c + d) % mod
        return sum(dp(i,j) for i in range(m) for j in range(n)) % mod

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1],[3,4]]
        o = 8
        self.assertEqual(s.countPaths(i), o)

    def test_two(self):
        s = Solution()
        i = [[1],[2]]
        o = 3
        self.assertEqual(s.countPaths(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)