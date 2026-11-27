# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array items, where items[i] = [factori, pricei]
    represents the ith item. Also given an integer budget.

    There are unlimited copies of each item available for purchase. It is
    possible to buy any number of copies of any items such that the total cost
    of the purchased copies is at most budget.

    After buying items, free items are received according to the following
    rules:
    * For each item i that at least one copy was bought, a free copy of every j
      such that j != i and factori divides factorj is received.
    * Buying multiple copies of the same item i does not give additional free
      copies through item i.
    * The same item j can be received multiple times for free if it is received
      from purchases of different item types.
    
    Return the maximum total number of item copies that can be obtained,
    including both purchased copies and free copies, while spending at most
    budget on purchased items.
    '''
    def maximumSaleItems_tle(self, items: List[List[int]], budget: int) -> int:
        items.sort()
        n = len(items)
        free = [0] * n
        for i in range(n):
            # for j in range(i+1,n):
            for j in range(n):
                if i == j:
                    continue
                free[i] += items[j][0] % items[i][0] == 0
        @cache
        def dp(i:int, budget:int) -> int:
            if i == n:
                return 0
            a = 0
            b = 0
            c = 0
            f = 0
            while b <= budget:
                a = max(a, f + c + dp(i+1, budget - b))
                b += items[i][1]
                c += 1
                f = free[i]
            return a
        return dp(0, budget)

    # double counting, do not get duplicate free items for independent items
    def maximumSaleItems_fails(self, items: List[List[int]], budget: int) -> int:
        items = Counter((i,j) for i,j in items)
        free = Counter()
        for i in items:
            for j in items:
                if i == j:
                    free[i] += (items[i]-1) * (items[j]-1)
                elif j[0] % i[0] == 0:
                    free[i] += items[i] * items[j]
        bag = sorted(items)
        @cache
        def dp(i:int, budget:int) -> int:
            a = 0
            b = 0
            f = 0
            if i == len(bag):
                return 0
            while b * bag[i][1] <= budget:
                # budget -= b * bag[i][1]
                a = max(a, f + b + dp(i+1, budget - b * bag[i][1]))
                f = free[bag[i]] * items[bag[i]]
                # budget += b * bag[i][1]
                b += 1
            return a
        return dp(0, budget)

    # based on leetcode editorial
    # https://leetcode.com/problems/maximum-number-of-items-from-sale-i/solutions/8621145/maximum-number-of-items-from-sale-i-by-l-at8c/?envType=daily-question&envId=2026-11-27
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # for a given budget the maximum number items acquirable
        f = [0] * (budget + 1)
        # find the cheapest item
        m = min(price for _,price in items)
        # for each item decide if take one (plus free items)
        for factor, price in items:
            # find the number of free items
            cnt = sum(
                1 for fact,_ in items if fact % factor == 0
            )
            # for each item decide if buying one
            for j in range(budget, price - 1, -1):
                if f[j - price] + cnt > f[j]:
                    f[j] = f[j - price] + cnt
        # find best selection of single purchase items + free items
        # fill in multiple copies of cheapest item
        return max(
            f[j] + (budget - j) // m for j in range(budget + 1)
        )

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[6,2],[2,6],[3,4]]
        j = 9
        o = 4
        self.assertEqual(s.maximumSaleItems(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[2,4],[3,2],[4,1],[6,4],[12,4]]
        j = 8
        o = 10
        self.assertEqual(s.maximumSaleItems(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[2,6],[6,2]]
        j = 9
        o = 4
        self.assertEqual(s.maximumSaleItems(i,j), o)

    def test_four(self):
        s = Solution()
        i = [[1000,1],[1000,1]]
        j = 2
        o = 4
        self.assertEqual(s.maximumSaleItems(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)