# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array prices where prices[i] is the price of a given stock
    on the ith day.

    Maximize the profit by choosing a single day to buy one stock and
    choosing a different day in the future to sell that stock.

    Return the maximum profit that can be achieved from this 
    transaction. If profit cannot be achieved return 0.
    '''
    # O(n) time
    # O(n) space
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[-1]
        dp = [0] * len(prices)
        for i in reversed(range(len(prices)-1)):
            m = max(m, prices[i])
            dp[i] = max(dp[i+1], m - prices[i])
        return dp[0]

    # O(n) time
    # O(1) space (destroys the input array)
    def maxProfit_alt(self, prices: List[int]) -> int:
        m = prices[-1]
        prices[-1] = 0
        for i in reversed(range(len(prices)-1)):
            m = max(m, prices[i])
            prices[i] = max(prices[i+1], m - prices[i])
        return prices[0]

    # O(n) time
    # O(1) space
    def maxProfit_alt_alt(self, prices: List[int]) -> int:
        m = prices[-1]
        p = 0
        for i in reversed(range(len(prices)-1)):
            m = max(m, prices[i])
            p = max(p, m - prices[i])
        return p

    # O(n) time
    # O(1) space
    def maxProfit_alt_alt_alt(self, prices: List[int]) -> int:
        l = prices[0]
        p = 0
        for i in range(1, len(prices)):
            l = min(l, prices[i])
            p = max(p, prices[i] - l)
        return p

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [7,1,5,3,6,4]
        o = 5
        self.assertEqual(s.maxProfit(i), o)
        self.assertEqual(s.maxProfit_alt_alt(i), o)
        self.assertEqual(s.maxProfit_alt_alt_alt(i), o)
        self.assertEqual(s.maxProfit_alt(i), o)

    def test_two(self):
        s = Solution()
        i = [7,6,4,3,1]
        o = 0
        self.assertEqual(s.maxProfit(i), o)
        self.assertEqual(s.maxProfit_alt_alt(i), o)
        self.assertEqual(s.maxProfit_alt_alt_alt(i), o)
        self.assertEqual(s.maxProfit_alt(i), o)

    def test_three(self):
        s = Solution()
        i = [4,14,1,4,5]
        o = 10
        self.assertEqual(s.maxProfit(i), o)
        self.assertEqual(s.maxProfit_alt_alt(i), o)
        self.assertEqual(s.maxProfit_alt_alt_alt(i), o)
        self.assertEqual(s.maxProfit_alt(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)