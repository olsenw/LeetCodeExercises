# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an n x n integer matrix grid, return the minimum sum of a falling path
    with non-zero shifts.

    A falling path with non-zero shifts is a choice of exactly one element from
    each row of grid such that no two elements chosen in adjacent rows are in
    the same column.
    '''
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(1,n):
            for j in range(n):
                grid[i][j] += min(grid[i-1][k] for k in range(n) if k != j)
        return min(grid[-1])

    '''
    Could improve by only tracking the two smallest per each row, as one of the
    two smallest is going to be used in the falling path. (need two when
    columns line up for smallest value)

    line 22 is run multiple times calculating redundant information

    add between line 20 and 21:
        find index of smallest
        find index of 2n smallest
    alter line 22:
        if index != index of smallest
        add smallest
        else
        add 2nd smallest
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        o = 13
        self.assertEqual(s.minFallingPathSum(i), o)

    def test_two(self):
        s = Solution()
        i = [[7]]
        o = 7
        self.assertEqual(s.minFallingPathSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)