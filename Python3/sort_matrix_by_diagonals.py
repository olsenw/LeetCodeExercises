# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an n x n square matrix of integers grid.

    Return the matrix such that:
    * The diagonals in the bottom-left triangle (including the middle diagonal)
      are sorted in non-increasing order.
    * The diagonals in the top-right triangle are sorted in non-decreasing
      order.
    '''
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n):
            s = sorted((grid[i+j][j] for j in range(n-i)), reverse=True)
            pass
            for j in range(n-i):
                grid[i+j][j] = s[j]
        for i in range(1,n):
            s = sorted(grid[j][i+j] for j in range(n-i))
            for j in range(n-i):
                grid[j][i+j] = s[j]
        return grid

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,7,3],[9,8,2],[4,5,6]]
        o = [[8,2,3],[9,6,7],[4,5,1]]
        self.assertEqual(s.sortMatrix(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,1],[1,2]]
        o = [[2,1],[1,0]]
        self.assertEqual(s.sortMatrix(i), o)

    def test_three(self):
        s = Solution()
        i = [[1]]
        o = [[1]]
        self.assertEqual(s.sortMatrix(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)