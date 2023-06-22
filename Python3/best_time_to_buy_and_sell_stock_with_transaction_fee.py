# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array prices where prices[i] is the price of a given stock on the
    ith day, and an integer fee representing a transaction fee.

    Find the maximum profit that can be achieved. There is no limit on the
    number of transactions, but the fee has to be paid each time.

    Note: it is impossible to engage in multiple transactions simultaneously
    (ie stock must be sold before being purchased).
    '''
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def buy(day):
            if day == len(prices):
                return 0
            return max(buy(day+1), sell(day+1) - prices[day])
        @cache
        def sell(day):
            if day == len(prices):
                return 0
            return max(sell(day+1), buy(day + 1) + prices[day] - fee)
        return buy(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2,8,4,9]
        j = 2
        o = 8
        self.assertEqual(s.maxProfit(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,3,7,5,10,3]
        j = 3
        o = 6
        self.assertEqual(s.maxProfit(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)