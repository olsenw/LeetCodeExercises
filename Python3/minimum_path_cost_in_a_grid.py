# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed m x n integer matrix grid consisting of distinct integers
    from 0 to m * n - 1. It is possible to move in this matrix from a cell to
    any other cell in the next row. Note that it is not possible to move from
    cells in the last row.

    Each possible move has a cost given by a 0-indexed 2D array moveCost of size
    (m * n) * n, where moveCost[i][j] is the cost of moving from a cell with
    value i to a cell in column j of the next row. The cost of moving from cells
    in the last row of grid can be ignored.

    The cost of path in grid is the sum of all values of cells visited plus the
    sum of costs of all the moves made. Return the minimum cost of a path that
    starts from any cell in the first row and ends at any cell in the last row.
    '''
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        # moveCost = {i:j for i,j in enumerate(moveCost)}
        @cache
        def dp(i:int, j:int) -> int:
            if i == m - 1:
                return grid[i][j]
            # answer = float('inf')
            # value = grid[i][j]
            # for k in range(n):
            #     a = moveCost[value][k] + value + dp(i+1,k)
            #     answer = min(answer,a)
            # return answer
            return min(moveCost[grid[i][j]][k] + grid[i][j] + dp(i+1,k) for k in range(n))
        return min(dp(0,j) for j in range(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[5,3],[4,0],[2,1]]
        j = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
        o = 17
        self.assertEqual(s.minPathCost(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[5,1,2],[4,0,3]]
        j = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]
        o = 6
        self.assertEqual(s.minPathCost(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)