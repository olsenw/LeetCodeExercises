# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n pieces arranged in a line, and each piece is colored either by
    'A' or by 'B'. Given a string colors of length n where colors[i] is the
    color of the ith piece.

    Alice and Bob are playing a game where they take alternating turns removing
    pieces from the line. In this game, Alice moves first.
    * Alice is only allowed to remove a piece colored 'A' if both its neighbors
      are also colored 'A'. She is not allowed to remove pieces that are colored
      'B'.
    * Bob is only allowed to remove a piece colored 'B' if both its neighbors
      are also colored 'B'. He is not allowed to remove pieces that are colored
      'A'.
    * Alice and Bob cannot remove pieces from the edge of the line.
    * If a player cannot make a move on their turn, that player loses and the
      other player wins.
    
    Assuming Alice and Bob play optimally, return true if Alice wins, or return
    false if Bob wins.
    '''
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) < 3:
            return False
        a,b = 0,0
        for i in range(1, len(colors) - 1):
            if colors[i-1] == 'A' and colors[i] == 'A' and colors[i+1] == 'A':
                a += 1
            if colors[i-1] == 'B' and colors[i] == 'B' and colors[i+1] == 'B':
                b += 1
        return a > b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "AAABABB"
        o = True
        self.assertEqual(s.winnerOfGame(i), o)

    def test_two(self):
        s = Solution()
        i = "AA"
        o = False
        self.assertEqual(s.winnerOfGame(i), o)

    def test_three(self):
        s = Solution()
        i = "ABBBBBBBAAA"
        o = False
        self.assertEqual(s.winnerOfGame(i), o)

    def test_four(self):
        s = Solution()
        i = "BB"
        o = False
        self.assertEqual(s.winnerOfGame(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)