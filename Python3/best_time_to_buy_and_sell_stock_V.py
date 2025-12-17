# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array prices where prices[i] is the price of a stock in
    dollars on the ith day, and an integer k.

    It is possible to make at most k transactions, where each transaction can be
    either of the following:
    * Normal transactions: Buy on day i, then sell on a later day j where i < j.
      The profit of the transaction is prices[j] - prices[i].
    * Short selling transactions: Sell on day i, then buy back on a later day j
      where i < j. The profit of the transaction is prices[i] - prices[j].

    Note that a transaction must be completed before starting another.
    Additionally, it is not possible to buy or sell on the same day as buying or
    selling back as part of a previous transaction.

    Return the maximum total profit that can be earned by making at most k
    transactions.
    '''
    # note can fix memory error by clearing cache after run
    def maximumProfit_memory(self, prices: List[int], k: int) -> int:
        n = len(prices)
        # i: index of price being considered
        # k: remaining transactions
        @cache
        def buy(i:int, k:int) -> int:
            if k == 0 or i == n - 1:
                return 0
            # option to buy
            a = -prices[i] + sell(i+1, k-1)
            # option to skip and not buy
            b = max(buy(i+1, k), short(i+1, k))
            return max(a,b)
        @cache
        def sell(i:int, k:int) -> int:
            if i == n - 1:
                return prices[i]
            # option to sell
            a = prices[i] + max(buy(i+1, k), short(i+1, k))
            # option to sell later
            b = sell(i+1, k)
            return max(a, b)
        @cache
        def short(i:int, k:int) -> int:
            if k == 0 or i == n - 1:
                return 0
            # option to short
            a = prices[i] + recover(i+1, k-1)
            # option to skip and not short
            b = max(buy(i+1,k), short(i+1,k))
            return max(a,b)
        @cache
        def recover(i:int, k:int) -> int:
            if i == n - 1:
                return -prices[i]
            # option to recover short
            a = -prices[i] + max(buy(i+1, k), short(i+1, k))
            # option to recover later
            b = recover(i+1, k)
            return max(a,b)
        answer = max(buy(0,k), short(0,k))
        buy.cache_clear()
        sell.cache_clear()
        short.cache_clear()
        recover.cache_clear()
        return answer

    # note can fix memory error by clearing cache after run
    def maximumProfit_memory2(self, prices: List[int], k: int) -> int:
        n = len(prices)
        # index: index in prices
        # k: remaining transactions
        # transactionType: true -> buy, false -> short
        @cache
        def dp(index:int, k:int, transactionType:bool, transactionRunning:bool) -> int:
            if transactionRunning:
                profit = 1 if transactionType else -1
                if index == n-1:
                    return profit * prices[index]
                a = profit * prices[index] + max(dp(index+1, k, True, False), dp(index+1, k, False, False))
                b = dp(index+1, k, transactionType, transactionRunning)
                return max(a,b)
            else:
                profit = -1 if transactionType else 1
                if k == 0 or index == n - 1:
                    return 0
                a = profit * prices[index] + dp(index+1, k-1, transactionType, True)
                b = dp(index+1, k, transactionType, transactionRunning)
                return max(a,b)
        answer = max(dp(0,k,True,False), dp(0,k,False,False))
        # this fixes memory error
        dp.cache_clear()
        return answer

    # based on LeetCode editorial
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/editorial/?envType=daily-question&envId=2025-12-17
    # note can fix memory error by clearing cache after run
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        # i: index
        # j: number of completed transactions
        # state: 0 -> not holding stock, 1 -> bought stock, 2 -> shorted stock
        @cache
        def dfs(i:int, j:int, state:int) -> int:
            if j == 0:
                return 0
            if i == 0:
                # note that buy / short are inverted
                # moving right to left in prices
                if state == 0:
                    return 0
                elif state == 1:
                    return -prices[0]
                else:
                    return prices[0]
            p = prices[i]
            if state == 0:
                return max(
                    dfs(i-1, j, 0),
                    dfs(i-1, j, 1) + p,
                    dfs(i-1, j, 2) - p
                )
            elif state == 1:
                return max(
                    dfs(i-1, j, 1),
                    dfs(i-1, j-1, 0) - p
                )
            else:
                return max(
                    dfs(i-1, j, 2),
                    dfs(i-1, j-1, 0) + p
                )
        answer = dfs(n-1,k,0)
        # needed to prevent memory exception
        dfs.cache_clear()
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,7,9,8,2]
        j = 2
        o = 14
        self.assertEqual(s.maximumProfit(i,j), o)

    def test_two(self):
        s = Solution()
        i = [12,16,19,19,8,1,19,13,9]
        j = 3
        o = 36
        self.assertEqual(s.maximumProfit(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)