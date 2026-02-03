# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of length n.

    An array is tronic if there exist indices 0 < p < q < n - 1 such that:
    * nums[0..p] is strictly increasing
    * nums[p..q] is strictly decreasing
    * nums[q..n-1] is strictly increasing

    Return true if nums is tronic, otherwise return false.
    '''
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        j = True
        i = 0
        while i < n and nums[i] < nums[i+1]:
            i += 1
            j = False
        if j or i == n:
            return False
        j = True
        while i < n and nums[i] > nums[i+1]:
            i += 1
            j = False
        if i == n:
            return False
        j = True
        while i < n and nums[i] < nums[i+1]:
            i += 1
            j = False
        return j == False and i == n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,5,4,2,6]
        o = True
        self.assertEqual(s.isTrionic(i), o)

    def test_two(self):
        s = Solution()
        i = [2,1,3]
        o = False
        self.assertEqual(s.isTrionic(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)