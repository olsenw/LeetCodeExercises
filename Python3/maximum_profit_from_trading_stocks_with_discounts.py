# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, representing the number of employees in a company. Each
    employee is assigned a unique ID from 1 to n, and employee 1 is the CEO.
    Also given are two 1-based integer arrays, present and future, each of
    length n, where:
    * present[i] represents the current price at which the ith employee can buy
      a stock today.
    * future[i] represents the expected price at which the ith employee can sell
      the stock tomorrow.
    
    The company's hierarchy is represented by a 2D integer array hierarchy,
    where hierarchy[i] = [ui, vi] means that employee ui is the direct boss of
    employee vi.

    Additionally, there is an integer budget representing the total funds
    available for investment.

    However, the company has a discount policy: if an employee's direct boss
    purchases their own stock, then the employee can buy their stock at half the
    original price (floor(present[v] / 2)).

    Return the maximum profit that can be achieved without exceeding the given
    budget.

    Note:
    * Each stock can be purchased at most once.
    * It is not possible to used the profit from future stock prices to fund
      additional investments and must purchase only from budget.
    '''
    # does not figure out final answer for given budget
    def maxProfit_incomplete(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        graph = {i:[] for i in range(1, n+1)}
        for i,j in hierarchy:
            graph[i].append(j)
        maxProfit = [0] * n
        maxProfitDiscount = [0] * n
        def dfs(i:int) -> int:
            profit = future[i-1] - present[i-1]
            discount = future[i-1] - (present[i-1] // 2)
            bestBuy = 0
            bestPass = 0
            for j in graph[i]:
                dfs(j)
                bestBuy += maxProfitDiscount[j-1]
                bestPass += maxProfit[j-1]
            maxProfit[i-1] = max(bestPass, profit + bestBuy)
            maxProfitDiscount[i-1] = max(bestPass, discount + bestBuy)
        dfs(1)
        return maxProfit

    # based on leetcode editorial
    # https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/editorial/?envType=daily-question&envId=2025-12-16
    # derivation of the knapsack problem
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        graph = [[] for _ in range(n)]
        for i,j in hierarchy:
            graph[i-1].append(j-1)
        def dfs(u:int):
            cost = present[u]
            dCost = present[u] // 2

            # dp[u][state][budget]
            # state = 0 do not purchase parent, state = 1 must purchase parent
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)

            # subprofit[state][budget]
            # state = 0 discount unavailable, sate = 1 discount available
            subProfit0 = [0] * (budget + 1)
            subProfit1 = [0] * (budget + 1)
            uSize = cost

            for v in graph[u]:
                child_dp0, child_dp1, vSize = dfs(v)
                uSize += vSize
                for i in range(budget, -1, -1):
                    for sub in range(min(vSize, i) + 1):
                        if i - sub >= 0:
                            subProfit0[i] = max(
                                subProfit0[i],
                                subProfit0[i - sub] + child_dp0[sub]
                            )
                            subProfit1[i] = max(
                                subProfit1[i],
                                subProfit1[i - sub] + child_dp1[sub]
                            )
            
            for i in range(budget + 1):
                dp0[i] = subProfit0[i]
                dp1[i] = subProfit0[i]
                if i >= dCost:
                    dp1[i] = max(
                        subProfit0[i],
                        subProfit1[i - dCost] + future[u] - dCost
                    )
                if i >= cost:
                    dp0[i] = max(
                        subProfit0[i],
                        subProfit1[i - cost] + future[u] - cost
                    )
            
            return dp0, dp1, uSize
        
        return dfs(0)[0][budget]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = [1,2]
        k = [4,3]
        l = [[1,2]]
        m = 3
        o = 5
        self.assertEqual(s.maxProfit(i,j,k,l,m), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [3,4]
        k = [5,8]
        l = [[1,2]]
        m = 4
        o = 4
        self.assertEqual(s.maxProfit(i,j,k,l,m), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = [4,6,8]
        k = [7,9,11]
        l = [[1,2],[1,3]]
        m = 10
        o = 10
        self.assertEqual(s.maxProfit(i,j,k,l,m), o)

    def test_four(self):
        s = Solution()
        i = 3
        j = [5,2,3]
        k = [8,5,6]
        l = [[1,2],[2,3]]
        m = 7
        o = 12
        self.assertEqual(s.maxProfit(i,j,k,l,m), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)