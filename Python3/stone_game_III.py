# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob continue their games with piles of stones. There are several
    stones arranged in a row, and each stone has an associated value which is an
    integer given in the array stoneValue.

    Alice and Bob take turns, with Alice starting first. On each player's, that
    player can take 1,2, or 3 stones from the first remaining stones in the row.

    The score of each player is the sum of the value of the stones taken. The
    score of each player is 0 initially.

    The objective of the game is to end with the highest score and the winner is
    the player with the highest score and there could be a tie. The game
    continues until all the stones have been taken.

    Assume Alice and Bob play optimally.

    Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they
    will end the game with the same score.
    '''
    # fails
    # basically copied from last night
    def stoneGameIII_fails(self, stoneValue: List[int]) -> str:
        def dp(turn, i):
            answer = 50000001 if turn == 1 else -50000001
            s = 0
            for j in range(3):
                if i + j == len(stoneValue):
                    break
                s += stoneValue[i+j]
                if turn == 0:
                    answer = max(answer, s + dp(1, i+j+1))
                else:
                    answer = min(answer, s + dp(0, i+j+1))
            return answer
        s = dp(0,0)
        if s == 0:
            return "Tie"
        elif s < 0:
            return "Bob"
        else:
            return "Alice"

    # based on leetcode bottom up solution
    # https://leetcode.com/problems/stone-game-iii/editorial/
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        @cache
        def dp(i):
            # base case no stones to take
            if i == n:
                return 0
            # take one, two or three stones
            a = stoneValue[i] - dp(i+1)
            if i + 2 <= n:
                a = max(a, stoneValue[i] + stoneValue[i+1] - dp(i+2))
            if i + 3 <= n:
                a = max(a, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp(i+3))
            return a
        s = dp(0)
        if s == 0:
            return "Tie"
        elif s < 0:
            return "Bob"
        else:
            return "Alice"

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,7]
        o = "Bob"
        self.assertEqual(s.stoneGameIII(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,-9]
        o = "Alice"
        self.assertEqual(s.stoneGameIII(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,6]
        o = "Tie"
        self.assertEqual(s.stoneGameIII(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)