# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob are playing a game where they take turns removing stones from
    a pile, with Alice going first.
    * Alice starts by removing exactly 10 stones on her first turn.
    * For each subsequent turn, each play removes exactly 1 fewer stone than the
      previous opponent.
    
    The player who cannot make a move loses the game.

    Given a positive integer n, return true if Alice wins the game and false
    otherwise.
    '''
    def canAliceWin(self, n: int) -> bool:
        alice = True
        stones = 10
        while n >= stones:
            n -= stones
            stones -= 1
            alice = not alice
        return not alice

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 12
        o = True
        self.assertEqual(s.canAliceWin(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = False
        self.assertEqual(s.canAliceWin(i), o)

    def test_three(self):
        s = Solution()
        i = 10
        o = True
        self.assertEqual(s.canAliceWin(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)