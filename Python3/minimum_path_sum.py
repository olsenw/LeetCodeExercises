# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a m x n grid filled with non-negative numbers, find a path from top
    left to bottom right, which minimizes the sum of all numbers along its path.

    Note: it is only possible to move right or down at any point in time.
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        # process the first row
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        # process the left column
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        # process the rest
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        # answer
        return grid[-1][-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,3,1],[1,5,1],[4,2,1]]
        o = 7
        self.assertEqual(s.minPathSum(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3],[4,5,6]]
        o = 12
        self.assertEqual(s.minPathSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)