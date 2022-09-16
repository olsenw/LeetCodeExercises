# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from functools import cache

class Solution:
    '''
    Given two integer arrays nums and multipliers of size n and m
    respectively, where n >= m. The arrays are 1-indexed.

    Begin with a score of zero. Perform exactly m operations. On the ith
    operation (1-indexed):
    * Choose one integer x from either the start or the end of the array
      nums
    * Add multipliers[i] * x to the score
    * Remove x from array nums

    Return the maximum score after performing m operations.
    '''
    def maximumScore_fails(self, nums: List[int], multipliers: List[int]) -> int:
        @cache
        def dp(i,j):
            k = i + len(nums) - j - 1
            if k == len(multipliers) - 1:
                return max(nums[i], nums[j]) * multipliers[k]
            a = nums[i] * multipliers[k] + dp(i+1,j)
            b = nums[j] * multipliers[k] + dp(i,j-1)
            return max(a,b)
        return dp(0,len(nums)-1)

    # test cases 32/50 (time limit exceeded)
    def maximumScore_tle(self, nums: List[int], multipliers: List[int]) -> int:
        @cache
        def dp(i,j,k):
            if k == len(multipliers):
                return 0
            a = nums[i] * multipliers[k] + dp(i+1,j,k+1)
            b = nums[j] * multipliers[k] + dp(i,j-1,k+1)
            return max(a,b)
        return dp(0,len(nums)-1,0)

    # test cases 38/50 (memory limit exceeded)
    # from leetcode solutions
    def maximumScore_mle(self, nums: List[int], multipliers: List[int]) -> int:
        m, n = len(multipliers), len(nums)
        @cache
        def dp(left, ops):
            if ops == m:
                return 0
            a = nums[left] * multipliers[ops] + dp(left+1,ops+1)
            b = nums[(n - 1) - (ops - left)] * multipliers[ops] + dp(left,ops+1)
            return max(a,b)
        return dp(0,0)

    # passes but slow
    # from leetcode solutions
    def maximumScore_iterative(self, nums: List[int], multipliers: List[int]) -> int:
        m, n = len(multipliers), len(nums)
        dp = [[0] * (m+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(i,-1,-1):
                # a = multipliers[i] * nums[j] + dp[i+1][j+1]
                # b = multipliers[i] * nums[(n - 1) - (i - j)]+ dp[i+1][j]
                # dp[i][j] = max(a,b)
                dp[i][j] = max(
                    multipliers[i] * nums[j] + dp[i+1][j+1],
                    multipliers[i] * nums[(n - 1) - (i - j)]+ dp[i+1][j]
                )
        return dp[0][0]

    '''
    There is a spaced optimized version as well
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        j = [3,2,1]
        o = 14
        self.assertEqual(s.maximumScore(i,j), o)

    def test_two(self):
        s = Solution()
        i = [-5,-3,-3,-2,7,1]
        j = [-10,-5,3,4,6]
        o = 102
        self.assertEqual(s.maximumScore(i,j), o)

    def test_three(self):
        s = Solution()
        i = [555,526,732,182,43,-537,-434,-233,-947,968,-250,-10,470,-867,-809,-987,120,607,-700,25,-349,-657,349,-75,-936,-473,615,691,-261,-517,-867,527,782,939,-465,12,988,-78,-990,504,-358,491,805,756,-218,513,-928,579,678,10]
        j = [783,911,820,37,466,-251,286,-74,-899,586,792,-643,-969,-267,121,-656,381,871,762,-355,721,753,-521]
        o = 6861161
        self.assertEqual(s.maximumScore(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)