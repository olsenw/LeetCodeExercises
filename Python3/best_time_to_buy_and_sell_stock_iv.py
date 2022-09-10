# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array prices where prices[i] is the price of a
    given stock on the ith day, and an integer k.

    Find the maximum profit that can be achieved making at most k
    transactions.

    Note: It is not possible to engage in multiple transactions
    simultaneously (i.e. must sell stock before buying again).
    '''
    # based on discussion post by zq670067
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54114/Easy-understanding-and-can-be-easily-modified-to-different-situations-Java-Solution
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # base case for early bounce
        if k == 0 or len(prices) < 2:
            return 0
        # more transactions allowed than possible
        if k > len(prices) // 2:
            answer = 0
            for i in range(len(prices)-1):
                if prices[i+1] > prices[i]:
                    answer += prices[i+1] - prices[i]
            return answer
        # hold[i][j] max profit with j transactions for 0th to ith day 
        # (marks relationship where stock needs to be sold)
        hold = [[0] * (k+1) for _ in range(len(prices))]
        # sell[i][j] max profit with j transactions for 0th to ith day
        # (marks relationship where stock needs to be bought)
        sell = [[0] * (k+1) for _ in range(len(prices))]
        # best profit with no transactions
        hold[0][0] = -prices[0]
        for i in range(1, len(prices)):
            hold[i][0] = max(hold[i-1][0], -prices[i])
        # best profit when holding first day stock
        for j in range(1,k+1):
            hold[0][j] = -prices[0]
        # populate answers for both tables
        for i in range(1, len(prices)):
            for j in range(1,k+1):
                # due to buy sell relationship these tables base off
                # each other (which side of buy sell)
                # have a better profit previously of buy days stock
                hold[i][j] = max(sell[i-1][j]-prices[i], hold[i-1][j])
                # have a better profit previously or sell the held stock
                sell[i][j] = max(hold[i-1][j-1]+prices[i], sell[i-1][j])
        # get max profit
        return max(hold[-1][-1], sell[-1][-1])
        # n = len(prices)
        # profit = [[-1] * n for _ in range(n)]
        # # profit = [[-2147483647] * n for _ in range(n)]
        # for i in range(n):
        #     for j in range(i, n):
        #         profit[i][j] = prices[j] - prices[i]
        # print("Info")
        # print("prices:", prices)
        # print("profit:")
        # for r in profit:
        #     print('[' + ' '.join('{:4}'.format(c) for c in r) + ']')
        # return 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = [2,4,1]
        o = 2
        self.assertEqual(s.maxProfit(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [3,2,6,5,0,3]
        o = 7
        self.assertEqual(s.maxProfit(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)