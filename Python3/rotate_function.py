# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n.

    Assume arrk to be an array obtained by rotating nums by k positions
    clock-wise. Define the rotation function F on nums as follows:
    * F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n-1) * arrk[n-1]

    Return the maximum value of F(0), F(1), ..., F(n-1).

    The test cases are generated so that the answer fits in a 32-bit integer.
    '''
    # brute force O(n^2)
    def maxRotateFunction_tle(self, nums: List[int]) -> int:
        n = len(nums)
        nums = nums + nums
        answer = float('-inf')
        for i in range(n):
            a = 0
            for j in range(n):
                a += nums[i+j] * j
            answer = max(answer, a)
        return answer

    # Based on the Leetcode editorial
    # https://leetcode.com/problems/rotate-function/editorial/?envType=daily-question&envId=2026-05-01
    # generalized 1 <= k < n, F(k) = F(k-1) + nextSum - (n * nums[n-k])
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        last = 0
        numSum = sum(nums)
        for i,j in enumerate(nums):
            last += i * j
        answer = last
        for i in range(n-1,0,-1):
            last = last + numSum - (n * nums[i])
            answer = max(answer, last)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,3,2,6]
        o = 26
        self.assertEqual(s.maxRotateFunction(i), o)

    def test_two(self):
        s = Solution()
        i = [100]
        o = 0
        self.assertEqual(s.maxRotateFunction(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)