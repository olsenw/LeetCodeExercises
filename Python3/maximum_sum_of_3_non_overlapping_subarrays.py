# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k, find three non-overlapping
    subarrays of length k with maximum sum and return them.

    Return the result as a list of indices representing the starting position of
    each interval (0-indexed). If there are multiple answers, return the
    lexicographically smallest one.
    '''
    def maxSumOfThreeSubarrays_incomplete(self, nums: List[int], k: int) -> List[int]:
        def dp(i,j):
            if j - i < k:
                return 0
            if j - i == k:
                return sum(nums[i:j+1])
            return
        answer = 0
        s = sum(nums[k:2*k])
        for i in range(2*k,len(nums)-k):
            answer = max(answer, dp(0,i) + s + dp())
        return answer

    # based on Leetcode Memoization approach
    # https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/editorial/?envType=daily-question&envId=2024-12-28
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # possible subarrays
        n = len(nums) - k + 1
        # precalculate all subarray sums
        sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            sums.append(sums[-1] - nums[i-k] + nums[i])
        # maximum value for given index and remaining subarrays
        memo = [[-1] * 4 for _ in range(n)]
        def dp(index, remaining):
            if remaining == 0:
                return 0
            if index >= n:
                return -float('inf') if remaining else 0
            if memo[index][remaining] != -1:
                return memo[index][remaining]
            a = sums[index] + dp(index+k, remaining-1)
            b = dp(index+1, remaining)
            memo[index][remaining] = max(a,b)
            return memo[index][remaining]
        dp(0, 3)
        answer = []
        # build answer based on dynamic programming
        def dfs(index, remaining):
            if remaining == 0:
                return
            if index >= n:
                return
            a = sums[index] + dp(index+k, remaining-1)
            b = dp(index+1,remaining)
            if a >= b:
                answer.append(index)
                dfs(index+k, remaining-1)
            else:
                dfs(index+1, remaining)
        dfs(0,3)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1,2,6,7,5,1]
        j = 2
        o = [0,3,5]
        self.assertEqual(s.maxSumOfThreeSubarrays(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,1,2,1,2,1,2,1]
        j = 2
        o = [0,2,4]
        self.assertEqual(s.maxSumOfThreeSubarrays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)