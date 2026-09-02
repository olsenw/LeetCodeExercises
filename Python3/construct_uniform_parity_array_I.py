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

    For each index i, chose exactly one of the following (in any order):
    * nums2[i] = nums1[i]
    * nums2[i] = nums1[i] - nums1[j], for an index j != i

    Return true if it is possible to construct such an array, otherwise, return
    false.
    '''
    def uniformArray_incomplete(self, nums1: list[int]) -> bool:
        e,o = 0,0
        for n in nums1:
            if n % 2:
                o += 1
            else:
                e += 1
        if e == 0 or o == 0:
            return True
        return

    # this is a trick question, because it is always true
    def uniformArray(self, nums1: list[int]) -> bool:
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3]
        o = True
        self.assertEqual(s.uniformArray(i), o)

    def test_two(self):
        s = Solution()
        i = [4,6]
        o = True
        self.assertEqual(s.uniformArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)