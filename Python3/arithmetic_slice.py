# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    An integer array is called arithmetic if it consists of at least
    three elements and if the difference between any two consecutive
    elements is the same. (Examples: [1,3,5,7,9] or [7,7,7,7])

    Given an integer array nums, return the number of arithmetic
    subarrays of nums.

    A subarray is a contiguous subsequence of the array.
    '''
    # based on discussion post by hf_z
    # https://leetcode.com/problems/arithmetic-slices/discuss/215861/Detailed-Explanation%3A-Two-DP-Solutions
    # used dp array to count number of valid answers at given index
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
        1, 2, 3, 4, 5
        0  0  1  2  3
              |  |  | (3,4,5), (2,3,4,5), (1,2,3,4,5)
              |  |             (2,3,4),   (1,2,3,4)
              |                           (1,2,3)
        '''
        # base case
        if len(nums) < 3:
            return 0
        # dp array initialized to zero
        dp = [0] * len(nums)
        # start at index 2 as impossible for 0,1 to be valid subslice
        for i in range(2, len(nums)):
            # validate three numbers are same apart
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                # this sequence is valid (+1)
                # if last sequence was valid another overlapping sequence (dp[i-1])
                dp[i] = dp[i-1] + 1
        # how many possible subarrays are there
        return sum(dp)

    # memoized version
    def numberOfArithmeticSlices_faster(self, nums: List[int]) -> int:
        total = 0
        current = 0
        for i in range(2,len(nums)):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                current += 1
            else:
                current = 0
            total += current
        return total

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = 3
        self.assertEqual(s.numberOfArithmeticSlices(i), o)
        self.assertEqual(s.numberOfArithmeticSlices_faster(i), o)

    def test_two(self):
        s = Solution()
        i = [1]
        o = 0
        self.assertEqual(s.numberOfArithmeticSlices(i), o)
        self.assertEqual(s.numberOfArithmeticSlices_faster(i), o)

    def test_three(self):
        s = Solution()
        i = [1,3,5,7,9]
        o = 6
        self.assertEqual(s.numberOfArithmeticSlices(i), o)
        self.assertEqual(s.numberOfArithmeticSlices_faster(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)