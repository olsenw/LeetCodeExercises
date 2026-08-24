# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice and Bob take turns playing a game, with Alice starting first.

    There are n stones arranged in a row. On each player's turn, while the
    number of stones is more than one, they will do the following:
    1. Choose an integer x > 1, and remove the leftmost x stones from the row.
    2. Add the sum of the removed stones' values to the player's score.
    3. Place a new stone, whose value is equal to that sum, on the left side of
       the row.
    
    The game stops when only one stone is left in the row.

    The score difference between Alice and Bob is (Alice's score - Bob's score).
    Alice's goal is to maximize the score difference, and Bob's goal is to
    minimize the score difference.

    Given an integer array stones of length n where stones[i] represents the
    value of the ith stone from the left, return the score difference between
    Alice and bob if they both play optimally.
    '''
    # based on hints, but incomplete
    def stoneGameVIII_incomplete(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0]
        for s in stones:
            prefix.append(prefix[-1] + s)
        @cache
        def dp(i:int) -> int:
            if i == n - 1:
                return stones[-1]
            a = float('-inf')
            for j in range(i+1,n):
                a = max(a, prefix[j+1] - prefix[i] - dp(j))
            return a
        return dp(1)

    # Based on Leetcode editorial
    # https://leetcode.com/problems/stone-game-viii/editorial/?envType=daily-question&envId=2026-08-24
    # key here is the problem can be recontextualized as prefix sum and selecting indices
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        # prefix array for efficient computation of sums
        prefix = list(accumulate(stones))
        dp = [0] * n
        # corner case when only last element is left in stones
        dp[n - 1] = prefix[n-1]
        # dp in reverse
        for i in range(n-2,0,-1):
            # Player skips index i
            # Player takes index i
            dp[i] = max(dp[i+1], prefix[i] - dp[i+1])
        # best possible for Alice
        # note it is Index one because Alice cannot choose index 0 on first turn
        return dp[1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-1,2,-3,4,-5]
        o = 5
        self.assertEqual(s.stoneGameVIII(i), o)

    def test_two(self):
        s = Solution()
        i = [7,-6,5,10,5,-2,-6]
        o = 13
        self.assertEqual(s.stoneGameVIII(i), o)

    def test_three(self):
        s = Solution()
        i = [-10,-12]
        o = -22
        self.assertEqual(s.stoneGameVIII(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)