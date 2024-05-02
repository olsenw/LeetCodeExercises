# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums that does not contain any zeros, find the
    largest positive integer k such that -k also exists in the array.

    Return the positive integer k. If there is no such integer, return -1.
    '''
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0, len(nums) - 1
        while i < j:
            if nums[i] >= 0:
                break
            k = -nums[i]
            while i < j and nums[j] > k:
                j -= 1
            if nums[j] == k:
                return k
            i += 1
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-1,2,-3,3]
        o = 3
        self.assertEqual(s.findMaxK(i), o)

    def test_two(self):
        s = Solution()
        i = [-1,10,6,7,-7,1]
        o = 7
        self.assertEqual(s.findMaxK(i), o)

    def test_three(self):
        s = Solution()
        i = [-10,8,6,7,-2,-3]
        o = -1
        self.assertEqual(s.findMaxK(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)