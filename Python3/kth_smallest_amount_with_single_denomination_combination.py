# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array coins representing coins of different denominations
    and an integer k.

    There are an infinite number of coins of each denomination. However, it is
    not possible to combine coins of different denominations.

    Return the kth smallest amount that can be made using these coins.
    '''
    # Brute force O(k log(len(coins)))
    # also incorrect... because it is possible to have repeat values
    def findKthSmallest_brute(self, coins: List[int], k: int) -> int:
        coins = [(c,c) for c in coins]
        heapq.heapify(coins)
        for _ in range(k):
            d,c = coins[0]
            heapq.heapreplace(coins, (d + c, c))
        return coins[0][0]

    # based on Leetcode editorial
    # https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/editorial/?envType=daily-question&envId=2026-08-21
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        n = len(coins)
        m = 1 << n
        # bounds for the binary search
        left = k
        right = coins[0] * k + 1
        bits = [0] * m
        leastCommonMultiple = [0] * m
        # find the least common multiple for each combination of coins
        for mask in range(1,m):
            lcm = 1
            for i,c in enumerate(coins):
                if mask >> i & 1:
                    lcm = lcm // math.gcd(lcm, c) * c
                    bits[mask] += 1
            leastCommonMultiple[mask] = lcm
        # apply inclusion-exclusion principle
        # calculate number of integers in interval [1,x] divisible by coin
        # this is non-decreasing
        def count(x:int) -> int:
            answer = 0
            for mask in range(1,m):
                if leastCommonMultiple[mask] <= x:
                    # size of subset odd (need to add x / lcm)
                    # fix under count of multiples
                    if bits[mask] & 1:
                        answer += x // leastCommonMultiple[mask]
                    # size of subset even (need to subtract x / lcm)
                    # fix over count of multiples
                    else:
                        answer -= x // leastCommonMultiple[mask]
            return answer
        # binary search
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,6,9]
        j = 3
        o = 9
        self.assertEqual(s.findKthSmallest(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,2]
        j = 7
        o = 12
        self.assertEqual(s.findKthSmallest(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3,6,9]
        j = 999999999
        o = 2999999997
        self.assertEqual(s.findKthSmallest(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)