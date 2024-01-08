# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given coordinates, a string that represents the coordinates of a square of
    the chessboard.

    Return true if the square is white and false if the square is black.

    The coordinate will always represent a valid chessboard square. The
    coordinate will always have the letter first, and the number second.
    '''
    def squareIsWhite(self, coordinates: str) -> bool:
        a,b = ord(coordinates[0]) - ord('a'), int(coordinates[1:])
        if a % 2:
            return b % 2 == 1
        else:
            return b % 2 == 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "a1"
        o = False
        self.assertEqual(s.squareIsWhite(i), o)

    def test_two(self):
        s = Solution()
        i = "h3"
        o = True
        self.assertEqual(s.squareIsWhite(i), o)

    def test_three(self):
        s = Solution()
        i = "c7"
        o = False
        self.assertEqual(s.squareIsWhite(i), o)


if __name__ == '__main__':
    unittest.main(verbosity=2)