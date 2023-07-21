# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, return the number of longest increasing
    subsequences.

    Notice that the sequence has to be strictly increasing.
    '''
    # O(n^2) does not solve problem... only finds the longest subsequence
    def findNumberOfLIS_incomplete(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            dp[i] = 1 + max((dp[k] for k in range(i) if nums[k] < nums[i]), default=0)
            # k = list(dp[k] for k in range(i) if nums[k] < nums[i])
            # j = max(k, default=0)
            # dp[i] = 1 + j
        return dp.count(max(dp))

    # based on leetcode solution
    # https://leetcode.com/problems/number-of-longest-increasing-subsequence/editorial/
    # similar to above except also tracking number with that length
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        count = [1] * n
        length = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        m = max(length)
        return sum(count[i] for i in range(n) if length[i] == m)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,5,4,7]
        o = 2
        self.assertEqual(s.findNumberOfLIS(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2,2,2,2]
        o = 5
        self.assertEqual(s.findNumberOfLIS(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)