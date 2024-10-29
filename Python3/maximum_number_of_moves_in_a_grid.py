# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed m x n matrix grid consisting of positive integers.

    Start at any cell in the first column of the matrix, and traverse the grid
    in the following way:
    * From a cell (row, col), it is possible to move to any of the cells
      (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the
      value of the cell moved to, should be strictly bigger than the value of
      the current cell.
    
    Return the maximum number of moves that can perform.
    '''
    def maxMoves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        @cache
        def dp(i:int, j:int) -> int:
            answer = 0
            if j == n - 1:
                return answer
            for k in range(max(0, i - 1), min(i + 2, m)):
                if grid[i][j] < grid[k][j+1]:
                    answer = max(answer, 1 + dp(k,j+1))
            return answer
        return max(dp(i,0) for i in range(m))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
        o = 3
        self.assertEqual(s.maxMoves(i), o)

    def test_two(self):
        s = Solution()
        i = [[3,2,4],[2,1,9],[1,1,7]]
        o = 0
        self.assertEqual(s.maxMoves(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)