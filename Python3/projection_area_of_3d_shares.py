# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an n x n grid where some 1x1x1 cubes that are axis-aligned with the x,
    y, and z axes.

    Each value v = grid[i][j] represents a tower of v cubes placed on top of the
    cell (i,j).

    The projection of these cubes are viewed on the xy, yz, and zx planes.

    A projection is like a shadow, that maps our 3-dimensional figure to a
    2-dimensional plane. It is the shadow being viewed from the top, the front,
    and the side.

    Return the total area of all three projections.
    '''
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    xy += 1
        xz = 0
        for i in range(n):
            a = 0
            for j in range(n):
                a = max(a, grid[i][j])
            xz += a
        yz = 0
        for i in range(n):
            a = 0
            for j in range(n):
                a = max(a, grid[j][i])
            yz += a
        return xy + xz + yz

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[3,4]]
        o = 17
        self.assertEqual(s.projectionArea(i), o)

    def test_two(self):
        s = Solution()
        i = [[2]]
        o = 5
        self.assertEqual(s.projectionArea(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0],[0,2]]
        o = 8
        self.assertEqual(s.projectionArea(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)