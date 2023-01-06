# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    def maxIceCream_sort(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        while i < len(costs) and coins >= costs[i]:
            coins -= costs[i]
            i += 1
        return i

    # basically the same as above, just doing sort with stack
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        h = []
        for c in costs:
            if c <= coins:
                coins -= c
                heapq.heappush(h, -c)
            elif h and c < -h[0]:
                coins = coins - h[0] - c
                heapq.heapreplace(h, -c)
        return len(h)

    '''
    Something called a counting sort will solve this faster
    see leetcode solution for details
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2,4,1]
        j = 7
        o = 4
        self.assertEqual(s.maxIceCream(i, j), o)

    def test_two(self):
        s = Solution()
        i = [10,6,8,7,7,8]
        j = 5
        o = 0
        self.assertEqual(s.maxIceCream(i, j), o)

    def test_three(self):
        s = Solution()
        i = [1,6,3,1,2,5]
        j = 20
        o = 6
        self.assertEqual(s.maxIceCream(i, j), o)

    def test_four(self):
        s = Solution()
        i = [2,2,3,4,1,1,1,1]
        j = 4
        o = 4
        self.assertEqual(s.maxIceCream(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)