# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import bisect

class Solution:
    '''
    Given an array of integers nums sorted in non-decreasing order, find
    the starting and ending positions of a given target value.

    If target value is not found in the array, return [-1, -1].

    Write an algorithm with O(log n) runtime complexity.
    '''
    # preforms two binary searches using bisect library
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = bisect.bisect_left(nums, target)
        if i < len(nums) and nums[i] == target:
            return [i, bisect.bisect(nums, target, i) - 1]
        else:
            return [-1, -1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,7,7,8,8,10]
        j = 8
        o = [3,4]
        self.assertEqual(s.searchRange(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5,7,7,8,8,10]
        j = 6
        o = [-1,-1]
        self.assertEqual(s.searchRange(i,j), o)

    def test_three(self):
        s = Solution()
        i = []
        j = 0
        o = [-1,-1]
        self.assertEqual(s.searchRange(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)