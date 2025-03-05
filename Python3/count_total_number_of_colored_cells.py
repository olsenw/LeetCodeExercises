# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There exists an infinitely large two-dimensional grid of uncolored unit
    cells. Given a positive integer n, indicating that the following routine
    must be done for n minutes:
    * At the first minute, color any arbitrary unit cell blue.
    * Every minute thereafter, color blue every uncolored cell that touches a
      blue cell.
    
    Return the number of colored cells at the end of n minutes.
    '''
    # attempts to solve the wrong problem of counting edges
    def coloredCells_wrong_edges(self, n: int) -> int:
        if n == 1:
            return n
        return (n-1) * 2 + 12

    def coloredCells(self, n: int) -> int:
        return (n * n) + (n-1) * (n-1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.coloredCells(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 5
        self.assertEqual(s.coloredCells(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = 13
        self.assertEqual(s.coloredCells(i), o)

    def test_four(self):
        s = Solution()
        i = 4
        o = 25
        self.assertEqual(s.coloredCells(i), o)

    def test_five(self):
        s = Solution()
        i = 5
        o = 41
        self.assertEqual(s.coloredCells(i), o)

    def test_six(self):
        s = Solution()
        i = 5356
        o = 57362761
        self.assertEqual(s.coloredCells(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)