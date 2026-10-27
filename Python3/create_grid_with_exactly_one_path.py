# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers m and n, representing the number of rows and columns of a
    grid.

    Construct any m x n grid consisting only of the characters '.' and '#',
    where:
    * '.' represents a free cell.
    * '#' represents an obstacle cell.

    A valid path is a sequence of free cells that:
    * Starts at the top-left cell (0,0).
    * Ends at the bottom-right cell (m - 1, n - 1).
    * Moves only:
      * Right, from (i,j) to (i,j + 1), or
      * Down, from (i,j) to (i + 1,j).

    Return any grid such that there is exactly on valid path from the top-left
    cell to the bottom-right cell.
    '''
    def createGrid(self, m: int, n: int) -> list[str]:
        answer = ["." * n]
        a = "#" * (n-1) + '.'
        for _ in range(m-1):
            answer.append(a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = 3
        o = ["...","##."]
        self.assertEqual(s.createGrid(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 3
        o = ["...","##.","##."]
        self.assertEqual(s.createGrid(i,j), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = 4
        o = ["...."]
        self.assertEqual(s.createGrid(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)