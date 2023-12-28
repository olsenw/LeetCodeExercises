# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a fruit market with different type of exotic fruits on display.

    Given a 1-indexed array prices, where prices[i] denotes the number of coins
    needed to purchase the ith fruit.

    The fruit market has the following offer:
    * If the ith fruit is purchased at prices[i] coins, the next i fruits can
      be obtained for free.

    Note that even if fruit j can be obtained for free, it can still be
    purchased for prices[j] coins to receive a new offer.

    Return the minimum number of coins needed to acquire all the fruits.
    '''
    def minimumCoins_fails(self, prices: List[int]) -> int:
        @cache
        def dp(i):
            if i > len(prices):
                return 0
            return min((prices[i-1] + dp(j) for j in range(i+1, min(i+i, len(prices)) + 1)), default=0)
        return dp(1)

    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [10**6] * n
        dp[-1] = prices[-1]
        for i in range(n-2, -1, -1):
            j = i + 1
            # if leave bounds of array no need to pay for other fruit
            if i + j + 1 >= n:
                dp[i] = prices[i]
            # what is the minimum price of next fruit
            else:
                dp[i] = prices[i] + min(dp[k] for k in range(j, i+j+2))
        return dp[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,2]
        o = 4
        self.assertEqual(s.minimumCoins(i), o)

    def test_two(self):
        s = Solution()
        i = [1,10,1,1]
        o = 2
        self.assertEqual(s.minimumCoins(i), o)

    def test_three(self):
        s = Solution()
        i = [1,10,20,1,100]
        o = 12
        self.assertEqual(s.minimumCoins(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)