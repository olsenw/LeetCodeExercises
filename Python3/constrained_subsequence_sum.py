# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k, return the maximum sum of a
    non-empty subsequence of that array such that for every two consecutive
    integers in the subsequence, nums[i] and nums[j], where i < j, the condition
    j - i <= k is satisfied.

    A subsequence of an array is obtained by deleting some number of elements
    (can be zero) from the array, leaving the remaining elements in their
    original order.
    '''
    # memory limit exceeded
    def constrainedSubsetSum_memory_exceeded(self, nums: List[int], k: int) -> int:
        @cache
        def dp(index, last):
            if index == len(nums):
                return 0
            a = 0
            if index - last <= k:
                a = nums[index] + dp(index + 1, index)
            b = dp(index + 1, last)
            return max(a,b)
        # return max(nums[i] + dp(i + 1, i) for i in range(len(nums)))
        answer = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            answer = max(answer, nums[i] + dp(i + 1, i))
        return answer

    # time limit exceeded
    def constrainedSubsetSum_time_exceeded(self, nums: List[int], k: int) -> int:
        @cache
        def dp(index):
            if index >= len(nums):
                return 0
            # return nums[index] + max((dp(j) for j in range(index + 1, k + index + 1)), default=0)
            answer = 0
            for j in range(index + 1, k + index + 1):
                answer = max(answer, dp(j))
            return nums[index] + answer
        # return max(dp(i) for i in range(len(nums)))
        answer = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            answer = max(answer, dp(i))
        return answer

    # based on hints
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # heap to optimize max of sequence operation
        h = [(-nums[0],0)]
        # use nums as dp array (dp[i] is best answer ending at index i)
        for i in range(1,len(nums)):
            # only consider elements starting from d[i - k]
            while h and h[0][1] < i - k:
                heapq.heappop(h)
            # best answer ending at index i
            nums[i] += max(0, -h[0][0])
            # used for tracking max in d[i-k] to dp[i-1]
            heapq.heappush(h, (-nums[i],i))
        return max(nums)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,2,-10,5,20]
        j = 2
        o = 37
        self.assertEqual(s.constrainedSubsetSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [-1,-2,-3]
        j = 1
        o = -1
        self.assertEqual(s.constrainedSubsetSum(i,j), o)

    def test_three(self):
        s = Solution()
        i = [10,-2,-10,-5,20]
        j = 2
        o = 23
        self.assertEqual(s.constrainedSubsetSum(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1] * (10**2)
        j = 3
        o = 100
        self.assertEqual(s.constrainedSubsetSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)