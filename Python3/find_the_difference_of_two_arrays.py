# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 0-indexed integer arrays nums1 and nums2, return a list answer of
    size 2 where:
    * answer[0] is a list of all distinct integers in nums1 which are not
      present in nums2.
    * answer[1] is a list of all distinct integers in nums2 which are not
      present in nums1.
    
    Note that the integers in the lists may be returned in any order.
    '''
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1)
        b = set(nums2)
        return [list(a - b), list(b - a)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        j = [2,4,6]
        o = [[1,3],[4,6]]
        self.assertEqual(s.findDifference(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,3]
        j = [1,1,2,2]
        o = [[3],[]]
        self.assertEqual(s.findDifference(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)