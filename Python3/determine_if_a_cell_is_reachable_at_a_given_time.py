# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given four integers sx, sy, fx, fy, and a non-negative integer t.

    In an infinite 2D grid, start at the cell (sx, sy). Each second, move to an
    adjacent cell.

    Return true if it is possible to reach the cell (fx, fy) after exactly t
    seconds, or false otherwise.

    A cell's adjacent cells are the 8 cells around it that share at least one
    corner with it. A cell can be visited multiple times.
    '''
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        height = fy - sy
        width = fx - sx
        if abs(width) < abs(height):
            return t >= abs(height)
        elif width == 0 == height:
            return t != 1
        else:
            return t >= abs(width)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2, 4, 7, 7, 6
        o = True
        self.assertEqual(s.isReachableAtTime(*i), o)

    def test_two(self):
        s = Solution()
        i = 3, 1, 7, 3, 3
        o = False
        self.assertEqual(s.isReachableAtTime(*i), o)

    def test_three(self):
        s = Solution()
        i = 1, 1, 1, 1, 1
        o = False
        self.assertEqual(s.isReachableAtTime(*i), o)

    def test_four(self):
        s = Solution()
        i = 1, 1, 1, 10, 9
        o = False
        self.assertEqual(s.isReachableAtTime(*i), o)

    def test_five(self):
        s = Solution()
        i = 1, 1, 10, 1, 9
        o = False
        self.assertEqual(s.isReachableAtTime(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)