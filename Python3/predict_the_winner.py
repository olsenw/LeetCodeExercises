# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. Two players are playing a game with this array:
    player 1 and player 2.

    Player 1 and player 2 take turns, with player 1 starting first. Both players
    start the game with a score of 0. At each turn, the player takes one of the
    numbers from either end of the array (ie nums[0] or nums[nums.length - 1])
    which reduces the size of the size of the array by 1. The player adds the
    chosen number to their score. The game ends when there are no more elements
    in the array.

    Return true if Player 1 can win the game. If the scores of both players are
    # equal, then player 1 is still the winner, and therefore the answer is
    true. It is assumed that both players are playing optimally.
    '''
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def dp(i,j):
            if i > j:
                return 0
            return max(nums[i] - dp(i+1,j), nums[j] - dp(i,j-1))
        return dp(0,len(nums) - 1) >= 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,5,2]
        o = False
        self.assertEqual(s.PredictTheWinner(i), o)

    def test_two(self):
        s = Solution()
        i = [1,5,233,7]
        o = True
        self.assertEqual(s.PredictTheWinner(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)