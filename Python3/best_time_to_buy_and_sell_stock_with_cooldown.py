# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array prices where prices[i] is the price of a given stock on the
    ith day.
    
    Find the maximum profit that can be achieved. It is possible to make
    multiple transactions (ie buy on and sell one share of stock multiple times)
    with the following restrictions:
    * After selling stock it is not possible to buy stock on the next day (ie
      cooldown one day.)
    
    Note: Multiple transactions cannot by done simultaneously (ie must sell the
    stock before buying again).
    '''
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def buy(i):
            if i >= len(prices):
                return 0
            a = buy(i+1)
            b = sell(i+1) - prices[i]
            return max(a,b)
        @cache
        def sell(i):
            if i >= len(prices):
                return 0
            a = sell(i+1)
            b = buy(i+2) + prices[i]
            return max(a,b)
        return buy(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,0,2]
        o = 3
        self.assertEqual(s.maxProfit(i), o)

    def test_two(self):
        s = Solution()
        i = [1]
        o = 0
        self.assertEqual(s.maxProfit(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)