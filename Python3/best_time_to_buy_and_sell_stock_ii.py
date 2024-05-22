# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array prices where prices[i] is the price of a given stock
    on the ith day.

    On each day, it is possible to buy and/or sell the stock. Only one share of
    a given stock can be held at a time. However it is possible to buy and then
    sell the stock on the same day.

    Find and return maximum profit that can be achieved.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def buy(i):
            if i == len(prices):
                return 0
            return max(buy(i+1),-prices[i] + sell(i+1))
        @cache
        def sell(i):
            if i == len(prices):
                return 0
            return max(sell(i+1), prices[i] + buy(i+1))
        return buy(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [7,1,5,3,6,4]
        o = 7
        self.assertEqual(s.maxProfit(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 4
        self.assertEqual(s.maxProfit(i), o)

    def test_three(self):
        s = Solution()
        i = [7,6,4,3,1]
        o = 0
        self.assertEqual(s.maxProfit(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)