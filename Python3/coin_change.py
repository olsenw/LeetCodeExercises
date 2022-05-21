# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array coins representing coins of different
    denominations and an integer amount representing a total amount of
    money.

    Return the fewest number of coins needed to make up that amount. If
    that amount of money cannot be made up by any combination of the
    coins, return -1.

    It is assumed that there are an infinite number of each kind of
    coin.
    '''
    # dynamic programming top down based on leetcode solution
    # https://leetcode.com/problems/coin-change/solution/
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        change = [0] * amount
        def solve(remain):
            nonlocal change
            # invalid solution case
            if remain < 0:
                return -1
            # valid solution case (no more coins needed)
            elif remain == 0:
                return 0
            # solved subproblem case (array indexing F(1) is index 0)
            elif change[remain - 1] != 0:
                return change[remain - 1]
            m = 10**5
            for c in coins:
                r = solve(remain - c)
                if r >= 0 and r < m:
                    m = 1 + r
            # (array indexing F(1) is index 0)
            change[remain - 1] = -1 if m == 10**5 else m
            return change[remain - 1]
        return solve(amount)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,5]
        j = 11
        o = 3
        self.assertEqual(s.coinChange(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2]
        j = 3
        o = -1
        self.assertEqual(s.coinChange(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1]
        j = 0
        o = 0
        self.assertEqual(s.coinChange(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)