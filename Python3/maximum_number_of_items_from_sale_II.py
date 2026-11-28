# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
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
    * Each purchased copy of item i can give at most one free copy of another
      item j.
    * The free item must satisfy i != j and factori divides factorj.
    * For each ordered pair (i,j), it is possible to receive at most one copy of
      item j from purchases of item i, regardless of how many copies of item i
      are purchased.
    * The same item j can be received multiple times for free if it is received
      from purchases of different item types.

    Return the maximum total number of item copes that can be obtained,
    including both purchased copies and free copies, while spending at most
    budget on purchased items.
    '''
    def maximumSaleItems_incomplete(self, items: List[List[int]], budget: int) -> int:
        c = Counter((j,i) for i,j in items)
        m = min(i for i,_ in c)
        gains = {i:0 for i in c}
        for i in c:
            for j in c:
                if i == j:
                    gains[i] += c[i]*c[i] - 2*c[i] + 1
                elif j[1] % i[1] == 0:
                    gains[i] += c[i] * c[j]
        return

    # based on hints
    def maximumSaleItems_tle(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        gain = [0] * n
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                gain[i] += items[j][0] % items[i][0] == 0
        answer = 0
        m = min(j for _,j in items)
        heap = [(items[i][1], gain[i]) for i in range(n) if gain[i] > 0]
        heapq.heapify(heap)
        while heap and heap[0][0] <= budget:
            cost,remain = heapq.heappop(heap)
            if 2 * m <= cost:
                break
            budget -= cost
            remain -= 1
            answer += 2
            if remain > 0:
                heapq.heappush(heap, (cost,remain))
        return answer + (budget // m)

    # figuring out gains can be O(n^2) if enough unique items
    def maximumSaleItems_tle(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        c = Counter((i,j) for i,j in items)
        gain = Counter()
        for i in c:
            for j in c:
                if i == j:
                    gain[i] += c[i] * (c[i]-1)
                elif j[0] % i[0] == 0:
                    gain[i] += c[i] * c[j]
        answer = 0
        m = min(j for _,j in c)
        costs = Counter()
        for i in gain:
            costs[i[1]] += gain[i]
        heap = [(i, costs[i]) for i in costs if costs[i] > 0]
        heapq.heapify(heap)
        while heap and heap[0][0] <= budget:
            cost,remain = heapq.heappop(heap)
            if 2 * m <= cost:
                break
            buy = min(budget // cost, remain)
            budget -= cost * buy
            remain -= buy
            answer += 2 * buy
            if remain > 0:
                heapq.heappush(heap, (cost,remain))
        return answer + (budget // m)

    # based on leetcode editorial
    # https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/editorial/?envType=daily-question&envId=2026-11-28
    # very similar buy logic
    # 
    # very different ways of tracking how many free items can be gained
    # using problem constraints, limit frequency counting to O(n)
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # sort items by price
        items.sort(key=lambda x:x[1])
        # find largest factor in items 
        mx = max(factor for factor,_ in items)
        # find the frequency of each factor
        freq = [0] * (mx+1)
        for factor,_ in items:
            freq[factor] += 1
        # find the maximum number of free items that can be obtained for a frequency
        for i in range(1, mx+1):
            if freq[i] > 0:
                # counting by multiples (factor[j] % factor[i] == 0)
                for j in range(i*2,mx+1,i):
                    freq[i] += freq[j]
        # find the smallest price
        mn = items[0][1]
        # greedy buy items
        answer = 0
        for factor,price in items:
            # getting the item + free item is more expensive than two min price items
            if price > 2 * mn:
                break
            # possible number of free items
            cnt = freq[factor] - 1
            # how many items should be bought
            take = min(cnt, budget // price)
            answer += take * 2
            budget -= take * price
        # spend remaining budget on smallest item
        answer += budget // mn
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,6],[2,4],[3,5]]
        j = 19
        o = 5
        self.assertEqual(s.maximumSaleItems(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]]
        j = 35
        o = 7
        self.assertEqual(s.maximumSaleItems(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[5,2],[1,3],[1,3],[1,3],[1,3]]
        j = 100
        o = 58
        self.assertEqual(s.maximumSaleItems(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)