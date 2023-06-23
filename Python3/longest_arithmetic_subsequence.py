# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter, defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums of integers, return the length of the longest arithmetic
    subsequence in nums.

    Note that:
    * A subsequence is an array that can be derived from another array by
      deleting some or no elements without changing the order of the remaining
      elements.
    * A sequence seq is arithmetic if seq[i+1] - seq[i] are all the same value
      for 0 <= i < seq.length - 1.
    '''
    def longestArithSeqLength_wrong(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return 2
        @cache
        def dp(i, a):
            if i == len(nums):
                return 1
            best = 0
            for j in range(i+1,len(nums)):
                if nums[j] - nums[i] == a:
                    best = max(best, 1 + dp(j, a))
            return max(best, dp(i+1,a))
        small, large = min(nums), max(nums)
        return max(dp(0,i) for i in range(small - large, large - small))

    # based on leetcode solution
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for right in range(len(nums)):
            for left in range(0, right):
                dp[(right, nums[right] - nums[left])] = dp.get((left, nums[right] - nums[left]), 1) + 1
        return max(dp.values())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,6,9,12]
        o = 4
        self.assertEqual(s.longestArithSeqLength(i), o)

    def test_two(self):
        s = Solution()
        i = [9,4,7,2,10]
        o = 3
        self.assertEqual(s.longestArithSeqLength(i), o)

    def test_three(self):
        s = Solution()
        i = [20,1,15,3,10,5,8]
        o = 4
        self.assertEqual(s.longestArithSeqLength(i), o)

    def test_four(self):
        s = Solution()
        i = [2,8]
        o = 2
        self.assertEqual(s.longestArithSeqLength(i), o)

    def test_five(self):
        s = Solution()
        i = [2,3,8]
        o = 2
        self.assertEqual(s.longestArithSeqLength(i), o)

    def test_six(self):
        s = Solution()
        i = [83,20,17,43,52,78,68,45]
        o = 2
        self.assertEqual(s.longestArithSeqLength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)