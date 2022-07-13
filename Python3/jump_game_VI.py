# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List
import heapq

class Solution:
    '''
    Given a 0-indexed integer array nums and an integer k.

    The game begins at index 0. In one move, it is possible to jump at
    most k steps forward without going outside the boundaries of the
    array. That is, it is possible jump from index i to any index in the
    range [i+1, min(len(nums) - 1, i + k)] inclusive.

    The goal is to reach the last index of the array (index
    len(nums) - 1). The score is the sum of all nums[j] for each index j
    visited in the array.

    Return the maximum score possible.
    '''
    def maxResult(self, nums: List[int], k: int) -> int:
        '''Correct but too slow'''
        # @cache
        # def dp(i):
        #     if i == len(nums) - 1:
        #         return nums[i]
        #     m = -2147483648
        #     for j in range(i+1, min(i+k+1, len(nums))):
        #         m = max(m, nums[i] + dp(j))
        #     return m
        #     # if i < len(nums)-1:
        #     #     return nums[i] + max(dp(j) for j in range(i+1, min(i+k+1, len(nums))))
        #     # return nums[i]
        # return dp(0)
        '''O(n^2) time'''
        # for i in range(len(nums) - 2, -1, -1):
        #     nums[i] += max(nums[i+1:i+k+1])
        # return nums[0]
        '''heap accepted'''
        h = [(-nums[0], 0)]
        for i in range(1, len(nums)):
            while h[0][1] < max(0, i - k):
                heapq.heappop(h)
            nums[i] += -h[0][0]
            heapq.heappush(h, (-nums[i], i))
        return nums[-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,-1,-2,4,-7,3]
        j = 2
        o = 7
        self.assertEqual(s.maxResult(i,j), o)

    def test_two(self):
        s = Solution()
        i = [10,-5,-2,4,0,3]
        j = 3
        o = 17
        self.assertEqual(s.maxResult(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,-5,-20,4,-1,3,-6,-3]
        j = 2
        o = 0
        self.assertEqual(s.maxResult(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)