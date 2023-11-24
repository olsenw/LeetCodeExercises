# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are 3n piles of coins of varying size, used by three people to play a
    game. Coins will be removed from the pile as follows:
    * In each step, any 3 piles of coins are chosen (not necessarily
      consecutive).
    * Of the three choices player A will take the pile with the maximum number
      of coins.
    * Player B will pick the nex pile with the maximum number of coins.
    * Player C gets the last pile of coins.
    * Repeat until there are no more coins.

    Given an array of integers piles where piles[i] is the number of coins in
    the ith pile.

    Return the maximum number of coins that player B can have.
    '''
    def maxCoins_passes(self, piles: List[int]) -> int:
        piles.sort()
        i,j = 0, len(piles) - 1
        answer = 0
        while i < j:
            answer += piles[j-1]
            j -= 2
            i += 1
        return answer

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = len(piles) - 2
        answer = 0
        for _ in range(len(piles) // 3):
            answer += piles[i]
            i -= 2
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,4,1,2,7,8]
        o = 9
        self.assertEqual(s.maxCoins(i), o)

    def test_two(self):
        s = Solution()
        i = [2,4,5]
        o = 4
        self.assertEqual(s.maxCoins(i), o)

    def test_three(self):
        s = Solution()
        i = [9,8,7,6,5,1,2,3,4]
        o = 18
        self.assertEqual(s.maxCoins(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)