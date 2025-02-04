# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers nums, return the maximum possible sum of
    an ascending subarray in nums.

    A subarray is defined as a contiguous sequence of numbers in an array.

    A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i
    where l <= i < r, numsi < numsi+1. Not that a subarray of size 1 is
    ascending.
    '''
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = 0
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curr += nums[i]
            else:
                answer = max(answer, curr)
                curr = nums[i]
        return max(answer, curr)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,20,30,5,10,50]
        o = 65
        self.assertEqual(s.maxAscendingSum(i), o)

    def test_two(self):
        s = Solution()
        i = [10,20,30,40,50]
        o = 150
        self.assertEqual(s.maxAscendingSum(i), o)

    def test_three(self):
        s = Solution()
        i = [12,17,15,13,10,11,12]
        o = 33
        self.assertEqual(s.maxAscendingSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)