# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n integer matrix grid.

    Define an hourglass as a part of the matrix with th following form:

    A B C
      D  
    E F G

    Return the maximum sum of the elements of an hourglass.

    Note that an hourglass cannot be rotated and must be entirely contained
    within the matrix.
    '''
    def maxSum(self, grid: List[List[int]]) -> int:
        return max(grid[i+1][j+1] + sum(grid[i][j+k] + grid[i+2][j+k] for k in range(3)) for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
        o = 30
        self.assertEqual(s.maxSum(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        o = 35
        self.assertEqual(s.maxSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)