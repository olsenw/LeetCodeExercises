# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    A XOR triplet is defined as the XOR of three elements
    nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

    Return the number of unique XOR triplet values from all possible triplets
    (i,j,k).
    '''
    # brute force
    def uniqueXorTriplets_tle(self, nums: List[int]) -> int:
        s = set()
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                a = nums[i] ^ nums[j]
                for k in range(j, n):
                    s.add(a ^ nums[k])
        return len(s)

    # Based on Leetcode editorial
    # https://leetcode.com/problems/number-of-unique-xor-triplets-ii/editorial/?envType=daily-question&envId=2026-07-24
    # gave up to quickly (this works because there can only be max(nums) possible xors)
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        for i in range(n):
            for j in range(i, n):
                s.add(nums[i] ^ nums[j])
        a = set()
        for x in nums:
            for y in s:
                a.add(x^y)
        return len(a)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3]
        o = 2
        self.assertEqual(s.uniqueXorTriplets(i), o)

    def test_two(self):
        s = Solution()
        i = [6,7,8,9]
        o = 4
        self.assertEqual(s.uniqueXorTriplets(i), o)

    def test_three(self):
        s = Solution()
        i = [1] * 1500
        o = 1
        self.assertEqual(s.uniqueXorTriplets(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)