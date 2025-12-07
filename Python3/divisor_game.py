# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob take turns playing a game, with Alice stating first.

    Initially, there is a number n on the chalkboard. On each player's turn,
    that player makes a move consisting of:
    * Choosing any integer x with 0 < x < n and n % x == 0.
    * Replacing the number n on the chalkboard with n - x.

    Also, if a player cannot make a move, they lose the game.

    Return true if and only if Alice wins the game, assuming both players play
    optimally.
    '''
    def divisorGame_dp(self, n: int) -> bool:
        @cache
        def alice(n:int) -> bool:
            for i in range(1, n):
                if n % i == 0 and bob(n - i) == False:
                    return True
            return False
        @cache
        def bob(n:int) -> bool:
            for i in range(1, n):
                if n % i == 0 and alice(n - i) == False:
                    return True
            return False
        return alice(n)

    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        o = True
        self.assertEqual(s.divisorGame(i), o)

    def test_two(self):
        s = Solution()
        i = 3
        o = False
        self.assertEqual(s.divisorGame(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)