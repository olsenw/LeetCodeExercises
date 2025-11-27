# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import sys
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums and an integer k.

    Return the maximum sum of a subarray of nums, such that the size of the
    subarray is divisible by k.
    '''
    def maxSubarraySum_fails(self, nums: List[int], k: int) -> int:
        answer = float('-inf') if k > 1 else nums[0]
        c = defaultdict(lambda : sys.maxsize)
        s = nums[0]
        for i,j in enumerate(nums[1:], 1):
            c[i % k] = min(s, c[i % k])
            s += j
            answer = max(answer, s - c[(k - i % k) % k])
        return answer

    # based on Leetcode editorial
    # https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/editorial/?envType=daily-question&envId=2025-11-27
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        answer = -sys.maxsize
        s = 0
        modSum = [sys.maxsize // 2] * k
        modSum[k - 1] = 0
        for i in range(len(nums)):
            s += nums[i]
            answer = max(answer, s - modSum[i % k])
            modSum[i % k] = min(modSum[i % k], s)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2]
        j = 1
        o = 3
        self.assertEqual(s.maxSubarraySum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [-1,-2,-3,-4,-5]
        j = 4
        o = -10
        self.assertEqual(s.maxSubarraySum(i,j), o)

    def test_three(self):
        s = Solution()
        i = [-5,1,2,-3,4]
        j = 2
        o = 4
        self.assertEqual(s.maxSubarraySum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)