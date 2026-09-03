# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums1 of n distinct integers.

    Construct another array nums2 of length n such that the elements in nums2
    are either all odd or all even.

    For each index i, choose exactly one of the following (in any order):
    * nums2[i] = nums1[i]
    * nums2[i] = nums1[i] - nums1[j], for an index j != i, such that
      nums1[i] - nums[j] >= 1
    
    Return true if it is possible to construct such an array, otherwise return
    false.
    '''
    def uniformArray_passes(self, nums1: list[int]) -> bool:
        nums1.sort()
        isOdd = nums1[0] % 2
        if isOdd:
            return True
        return all(i % 2 == 0 for i in nums1)

    # much faster (relatively speaking)
    def uniformArray(self, nums1: list[int]) -> bool:
        return True if min(nums1) % 2 else all(i % 2 == 0 for i in nums1)
    

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4,7]
        o = True
        self.assertEqual(s.uniformArray(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3]
        o = False
        self.assertEqual(s.uniformArray(i), o)

    def test_three(self):
        s = Solution()
        i = [4,6]
        o = True
        self.assertEqual(s.uniformArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)