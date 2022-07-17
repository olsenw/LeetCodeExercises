# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List
from functools import cache

class Solution:
    '''
    For an integer array nums, an inverse pair is a pair of integers
    [i,j] where o <= i < j < nums.length and nums[i] > nums[j].

    Given two integers n and k return the number of different arrays
    consisting of numbers from 1 to n such that there are exactly k
    inverse pairs. Since the answer can be huge, return it modulo
    10^9+7.
    '''
    # time limit exceeded
    # based on leetcode solution 2 (recursion with memoization)
    # O(n k min(n,k)) time
    # O(n k) space
    def kInversePairs_memoization(self, n: int, k: int) -> int:
        # memoization
        @cache
        def r(n, k):
            # base: empty array so no possible sequences
            if n == 0: return 0
            # base: no inverse pairs (sequential order only)
            if k == 0: return 1
            # sum up smaller cases
            return sum(r(n-1,k-i) for i in range(0,min(k,n-1)+1))
        return r(n,k)

    # based on leetcode solution 6 (once again memoization)
    # O(n k) time
    # O(n k) space
    # similar to above but makes use of a cumulative sum
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def r(n,k):
            if n == 0: return 0
            if k == 0: return 1
            return r(n, k-1) + r(n-1, k) - (r(n-1, k-n) if k >= n else 0)
        return (r(n,k) - (r(n, k-1) if k else 0)) % (10**9 + 7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = 0
        o = 1
        self.assertEqual(s.kInversePairs(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 1
        o = 2
        self.assertEqual(s.kInversePairs(i,j), o)

    def test_three(self):
        s = Solution()
        i = 40
        j = 40
        o = 41237402
        self.assertEqual(s.kInversePairs(i,j), o)

    # unable (exceeds max recursion depth)
    # def test_four(self):
    #     s = Solution()
    #     i = 1000
    #     j = 1000
    #     o = 663677020
    #     self.assertEqual(s.kInversePairs(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)