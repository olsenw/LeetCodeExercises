# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    return the minimum integer common to both arrays. If there is no common
    integer amongst nums1 and nums2, return -1.

    Note that an integer is said to be common to nums1 and nums2 if both arrays
    have at least one occurrence of that integer.
    '''
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        s = set(nums1)
        for n in nums2:
            if n in s:
                return n
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        j = [2,4]
        o = 2
        self.assertEqual(s.getCommon(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,6]
        j = [2,3,4,5]
        o = 2
        self.assertEqual(s.getCommon(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,6]
        j = [5,7,8,9,10]
        o = -1
        self.assertEqual(s.getCommon(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)