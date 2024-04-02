# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A square matrix is said to be an X-Matrix if both of the following
    conditions hold:

    1. All the elements in the diagonals of the matrix are non-zero.
    2. All other elements are 0.

    Given a 2D integer array grid of size n x n representing a square matrix
    return true if grid is an X-Matrix. Otherwise, return false.
    '''
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        s = set()
        for i in range(n):
            s.add((i,i))
            s.add((n-i-1,i))
        for r in range(n):
            for c in range(n):
                # alternate r + c == n - 1
                if (r,c) in s:
                    if grid[r][c] == 0:
                        return False
                else:
                    if grid[r][c] != 0:
                        return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
        o = True
        self.assertEqual(s.checkXMatrix(i), o)

    def test_two(self):
        s = Solution()
        i = [[5,7,0],[0,3,1],[0,5,0]]
        o = False
        self.assertEqual(s.checkXMatrix(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,0,0,0,1],[0,4,0,1,0],[0,0,5,0,0],[0,5,0,2,0],[4,0,0,0,2]]
        o = False
        self.assertEqual(s.checkXMatrix(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)