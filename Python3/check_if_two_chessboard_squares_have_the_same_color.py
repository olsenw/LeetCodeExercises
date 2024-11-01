# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings, coordinate1 and coordinate2, representing the coordinates
    of a square on an 8 x 8 chessboard.

    Picture of a chessboard for reference (O is white, # is black)
    8 O#O#O#O#
    7 #O#O#O#O
    6 O#O#O#O#
    5 #O#O#O#O
    4 O#O#O#O#
    3 #O#O#O#O
    2 O#O#O#O#
    1 #O#O#O#O
      abcdefgh
    
    Return True if these two squares have the same color and false otherwise.

    The coordinate will always represent a valid chessboard square. The
    coordinate will always have the letter first (indicating its column), and
    the number second (indicating its row).
    '''
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        board = {
            'a': "#O#O#O#O",
            'b': "O#O#O#O#",
            'c': "#O#O#O#O",
            'd': "O#O#O#O#",
            'e': "#O#O#O#O",
            'f': "O#O#O#O#",
            'g': "#O#O#O#O",
            'h': "O#O#O#O#",
        }
        return board[coordinate1[0]][ord(coordinate1[1]) - 49] == board[coordinate2[0]][ord(coordinate2[1]) - 49]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "a1", "c3"
        o = True
        self.assertEqual(s.checkTwoChessboards(*i), o)

    def test_two(self):
        s = Solution()
        i = "a1", "h3"
        o = False
        self.assertEqual(s.checkTwoChessboards(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)