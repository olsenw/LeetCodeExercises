# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an 8x8 empty chessboard with 1-indexed rows and columns.

    Given an array source = [sr,sc] representing the starting position of a
    queen, and an array target = [tr,tc] representing the target position.

    In one move, the queen travels one or more squares along a single row,
    column, or diagonal, staying within the board.

    Return the minimum number of moves for the queen to land exactly on target.
    '''
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if source == target:
            return 0
        if source[0] == target[0]:
            return 1
        if source[1] == target[1]:
            return 1
        d,r = divmod((target[1] - source[1]), (target[0] - source[0]))
        if (d == 1 and r == 0) or (d == -1 and r == 0):
            return 1
        return 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [8,1]
        j = [1,8]
        o = 1
        self.assertEqual(s.minQueenMoves(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,2]
        j = [1,3]
        o = 2
        self.assertEqual(s.minQueenMoves(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,1]
        j = [1,1]
        o = 0
        self.assertEqual(s.minQueenMoves(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)