# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays prices and strategy, where:
    * prices[i] is the price of a given stock on the ith day.
    * strategy[i] represents a trading action on the ith day, where:
        * -1 indicates buying one unit of the stock.
        * 0 indicates holding the stock.
        * 1 indicates selling one unit of stock.
    
    Also given an even integer k, and it is possible to perform at most one
    modification to strategy. A modification consists of:
    * Selecting exactly k consecutive elements in strategy.
    * Set the first k / 2 elements to 0 (hold).
    * Set the last k / 2 elements to 1 (sell).

    The profit is defined as the sum of strategy[i] * prices[i] across all days.

    Return the maximum possible profit that can be achieved.

    Note: There are no constraints on budget or stock ownership, so all buy and
    sell operations are feasible regardless of past actions.
    '''
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        h = k // 2
        profit = [0] + list(accumulate(strategy[i] * prices[i] for i in range(n)))
        window = sum(prices[h:k-1])
        # max (make no changes, first window)
        answer = profit[-1]
        for i in range(k-1, n):
            window += prices[i]
            answer = max(answer, profit[-1] - profit[i+1] + window + profit[i-k+1])
            window -= prices[i-h+1]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,2,8]
        j = [-1,0,1]
        k = 2
        o = 10
        self.assertEqual(s.maxProfit(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [5,4,3]
        j = [1,1,0]
        k = 2
        o = 9
        self.assertEqual(s.maxProfit(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [0,1,2,3,4]
        j = [-1,-1,-1,-1,-1]
        k = 4
        o = 7
        self.assertEqual(s.maxProfit(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)