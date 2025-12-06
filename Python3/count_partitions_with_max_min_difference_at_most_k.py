# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

from sortedcontainers import SortedList

class Solution:
    '''
    Given an integer array nums and an integer k. Partition nums into one or
    more non-empty contiguous segments such that in each segment the difference
    between its maximum and minimum elements is at most k.

    Return the total number of ways to partition nums under this condition.

    Since the answer may be too large, return it modulo 10^9 + 7.
    '''
    def countPartitions_incomplete(self, nums: List[int], k: int) -> int:
        m = 10**9 + 7
        @cache
        def dp(index:int) -> int:
            if index == 0:
                return 1
            d = []
            answer = 0
            for i in range(index, -1, -1):
                d
            return (dp(index - 1) % m + answer % m) % m
        return dp(len(nums))

    # based on Leetcode editorial
    # https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/editorial/?envType=daily-question&envId=2025-12-06
    def countPartitions(self, nums: List[int], k: int) -> int:
        m = 10**9 + 7
        n = len(nums)
        # track min and max value for a subarray
        s = SortedList()
        # track previous calculations
        dp = [0] * (n + 1)
        dp[0] = 1
        # calculate windows of valid min-max <= k
        prefix = [0] * (n + 1)
        prefix[0] = 1
        j = 0
        for i in range(n):
            s.add(nums[i])
            # ensure valid subarray
            while j < i and s[-1] - s[0] > k:
                s.remove(nums[j])
                j += 1
            # get answer at left window
            minus = prefix[j-1] if j > 0 else 0
            # note left of this window is already accounted for
            dp[i+1] = (prefix[i] - minus) % m
            # updated count of valid subarrays
            prefix[i+1] = (prefix[i] + dp[i+1]) % m
        return dp[n]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [9,4,1,3,7]
        j = 4
        o = 6
        self.assertEqual(s.countPartitions(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,3,4]
        j = 0
        o = 2
        self.assertEqual(s.countPartitions(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)