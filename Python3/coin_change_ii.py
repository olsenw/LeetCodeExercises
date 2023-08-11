# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    given an integer array coins representing coins of different denominations
    and an integer amount representing a total amount of money.

    Return the number of combinations that make up that amount. If that amount
    of money cannot be made up by any combination of the coins, return 0.

    It may be assumed that there is an infinite number of each kind of coin.

    The answer is guaranteed to fit into a signed 32-bit integer.
    '''
    def change_double_counts(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        @cache
        def dp(remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            answer = 0
            for c in coins:
                answer += dp(remain - c)
            return answer
        return dp(amount)

    def change_over_counting(self, amount: int, coins: List[int]) -> int:
        # number of coins  \/  amount >
        dp = [[0] * (amount + 1) for _ in range(amount + 1)]
        dp[0][0] = 1
        for c in coins:
            if c <= amount:
                dp[1][c] = 1
        # number of coins
        for i in range(2,amount+1):
            # target amount
            for j in range(amount+1):
                for c in coins:
                    if j - c > 0:
                        dp[i][j] += dp[i-1][j-c]
        return sum(dp[i][amount] for i in range(amount+1))

    # based on top-down LeetCode solution
    # https://leetcode.com/problems/coin-change-ii/editorial/
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        # i is coin being considered, j is amount left to obtain
        def dp(i, j):
            if j < 0:
                return 0
            if i == len(coins):
                return 0
            if j == 0:
                return 1
            # take coin
            a = dp(i, j - coins[i])
            # leave coin
            b = dp(i + 1, j)
            return a + b
        return dp(0, amount)

class UnitTesting(unittest.TestCase):
    # def test_one(self):
    #     s = Solution()
    #     i = 5
    #     j = [1,2,5]
    #     o = 4
    #     self.assertEqual(s.change(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = [2]
        o = 0
        self.assertEqual(s.change(i,j), o)

    def test_three(self):
        s = Solution()
        i = 10
        j = [10]
        o = 1
        self.assertEqual(s.change(i,j), o)

    def test_four(self):
        s = Solution()
        j = [1,2,5]
        i = [s.change(i,j) for i in range(12)]
        o = [1,1,2,2,3,4,5,6,7,8,10,11]
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)