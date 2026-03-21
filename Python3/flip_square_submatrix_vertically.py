# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n integer matrix grid, and three integers x, y, and k.

    The integers x and y represent the row and column indices of the top-left
    corner of a square submatrix and the integer k represents the size (side
    length) of the square submatrix.

    Flip the submatrix by reversing the order of its rows vertically.

    Return the updated matrix.
    '''
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        flip = []
        for i in range(k):
            flip.append([])
            for j in range(k):
                flip[-1].append(grid[x+i][y+j])
        flip = flip[::-1]
        for i in range(k):
            for j in range(k):
                grid[x+i][y+j] = flip[i][j]
        return grid

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        j = 1
        k = 0
        l = 3
        o = [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]
        self.assertEqual(s.reverseSubmatrix(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = [[3,4,2,3],[2,3,4,2]]
        j = 0
        k = 2
        l = 2
        o =[[3,4,4,2],[2,3,2,3]]
        self.assertEqual(s.reverseSubmatrix(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)