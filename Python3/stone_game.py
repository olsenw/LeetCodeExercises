# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob play a game with piles of stones. There are an even number of
    piles arranged in a row, and each pile has a positive integer number of
    stones piles[i].

    The objective of the game is to end with the most stones. The total number
    of stones across all the piles is odd, so there are no ties.

    Alice and Bob take turns, with Alice starting first. Each turn, a player
    takes the entire pile of stones either from the beginning or from the end of
    the row. This continues until there are no more piles left, at which point
    the person with the most stones wins.

    Assuming Alice and Bob play optimally, return true if Alice wins the game,
    or false if Bob wins.
    '''
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(i,j):
            if i > j:
                return 0
            return max(piles[i] - dp(i+1,j), piles[j] - dp(i,j-1))
        score = dp(0, len(piles) - 1)
        return score > 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,3,4,5]
        o = True
        self.assertEqual(s.stoneGame(i), o)

    def test_two(self):
        s = Solution()
        i = [3,7,2,3]
        o = True
        self.assertEqual(s.stoneGame(i), o)

    def test_three(self):
        s = Solution()
        i = [7,7,12,16,41,48,41,48,11,9,34,2,44,30,27,12,11,39,31,8,23,11,47,25,15,23,4,17,11,50,16,50,38,34,48,27,16,24,22,48,50,10,26,27,9,43,13,42,46,24]
        o = True
        self.assertEqual(s.stoneGame(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)