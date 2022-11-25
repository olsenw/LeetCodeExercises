# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of integers arr, find the sum of min(b), where b ranges over
    every (contiguous) subarray of arr. Since the answer may be large, return
    the answer modulo 10^9 + 7.
    '''
    # O(n^3) time
    def sumSubarrayMins_brute(self, arr: List[int]) -> int:
        m = 10**9 + 7
        n = len(arr)
        s = 0
        for w in range(1,n+1):
            for i in range(n-w+1):
                # print(arr[i:i+w])
                s = ((s % m) + (min(arr[i:i+w]) % m)) % m
        return s

    def sumSubarrayMins_brute_alt(self, arr: List[int]) -> int:
        m = 10**9 + 7
        n = len(arr)
        @cache
        def dp(i,j):
            if i == j:
                return arr[i]
            return min(dp(i,j-1), arr[j])
        s = 0
        for w in range(1,n+1):
            for i in range(n-w+1):
                # print(arr[i:i+w])
                s = ((s % m) + (dp(i,i+w-1) % m)) % m
        return s

    # based on leetcode monotonic stack solution
    # https://leetcode.com/problems/sum-of-subarray-minimums/solution/
    # O(n) time O(n) space
    def sumSubarrayMins(self, arr: List[int]) -> int:
        m = 10**9 + 7
        n = len(arr)
        stack = []
        sm = 0
        for i in range(n + 1):
            # when i reaches the array length, all elements have been seen and 
            # need to be removed
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                # >= prevents double counting
                # rb accounts for equal of smaller elements
                # lb accounts for only smaller elements
                mid = stack.pop()
                lb = -1 if not stack else stack[-1]
                rb = i
                # c is number subarrays where mid is the min element
                c = (mid - lb) * (rb - mid)
                sm += c * arr[mid]
            stack.append(i)
        return sm % m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,2,4]
        o = 17
        self.assertEqual(s.sumSubarrayMins(i), o)

    def test_two(self):
        s = Solution()
        i = [11,81,94,43,3]
        o = 444
        self.assertEqual(s.sumSubarrayMins(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)