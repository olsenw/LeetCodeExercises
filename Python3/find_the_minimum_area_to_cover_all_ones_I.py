# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D binary array grid. Find a rectangle with horizontal and vertical
    sides with the smallest area such that all the 1's in grid lie inside this
    rectangle.

    Return the minimum possible area of the rectangle.
    '''
    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        up, down = m, -1
        left, right = n, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    up = min(up, i)
                    down = max(down, i)
                    left = min(left, j)
                    right = max(right, j)
        if up == m:
            return 0
        return (down - up + 1) * (right - left + 1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,0],[1,0,1]]
        o = 6
        self.assertEqual(s.minimumArea(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0],[0,0]]
        o = 1
        self.assertEqual(s.minimumArea(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)