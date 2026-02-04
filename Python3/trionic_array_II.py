# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n.

    A tronic subarray is a contiguous subarray nums[l..r] (with 0 <= l < r < n)
    for which there exist indices l < p < q < r such that:
    * nums[l..p] is strictly increasing
    * nums[p..q] is strictly decreasing
    * nums[q..r] is strictly increasing

    Return the maximum sum of any tronic subarray in nums.
    '''
    # based on hints
    def maxSumTrionic_fails(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[k][i] is the max sum of subarray ending at i after k of the phases
        dp = [[0]*n for _ in range(4)]
        # dp = [[-float('inf')]*n for _ in range(4)]
        # hint 2
        for i in range(1, n):
            # hint 4
            if nums[i] > nums[i-1]:
                dp[1][i] = max(dp[1][i-1]+nums[i], dp[0][i-1]+nums[i])
                dp[3][i] = max(dp[3][i-1]+nums[i], dp[2][i-1]+nums[i])
                # hint 6 phase 4 (the 2nd increasing)
                dp[0][i] = dp[0][i-1]+nums[i]
            # hint 5
            elif nums[i] < nums[i-1]:
                dp[2][i] = max(dp[2][i-1]+nums[i], dp[1][i-1]+nums[i])
        return max(dp[3])

    # based on editorial
    # https://leetcode.com/problems/trionic-array-ii/editorial/?envType=daily-question&envId=2026-02-04
    # core idea is the middle segment (decreasing) will always be present
    # find valid middle segment, then find max sum to left and right
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        answer = float('-inf')
        i = 0
        while i < n:
            j = i + 1
            result = 0
            # first segment (increasing)
            while j < n and nums[j-1] < nums[j]:
                j += 1
            p = j - 1
            # early bail (segment not increasing)
            if p == i:
                i += 1
                continue
            # second segment (decreasing)
            result += nums[p] + nums[p-1]
            while j < n and nums[j-1] > nums[j]:
                result += nums[j]
                j += 1
            q = j - 1
            # early bail (segment not decreasing, impossible end point [no third segment])
            if q == p or q == n - 1 or (j < n and nums[j] <= nums[q]):
                i = q
                continue
            # third segment (increasing)
            result += nums[q+1]
            # find maximum sum of third segment
            maxSum = 0
            currSum = 0
            k = q + 2
            while k < n and nums[k] > nums[k-1]:
                currSum += nums[k]
                maxSum = max(maxSum, currSum)
                k += 1
            result += maxSum
            # find maximum sum of first segment
            maxSum = 0
            currSum = 0
            for k in range(p-2, i-1, -1):
                currSum += nums[k]
                maxSum = max(maxSum, currSum)
            result += maxSum
            # update answer
            answer = max(answer, result)
            i = q
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,-2,-1,-3,0,2,-1]
        o = -4
        self.assertEqual(s.maxSumTrionic(i), o)

    def test_two(self):
        s = Solution()
        i = [1,4,2,7]
        o = 14
        self.assertEqual(s.maxSumTrionic(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)