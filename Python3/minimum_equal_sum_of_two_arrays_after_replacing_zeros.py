# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two arrays nums1 and nums2 consisting of positive integers.

    Replace all the 0's in both arrays with strictly positive integers such that
    the sum of elements of both arrays becomes equal.

    Return the minimum equal sum that can be obtained , or -1 if it is
    impossible.
    '''
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        a,b = sum(nums1), nums1.count(0)
        x,y = sum(nums2), nums2.count(0)
        if a + b == x + y:
            return a + b
        elif a + b <= x + y:
            return x + y if b > 0 else -1
        else:
            return a + b if y > 0 else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,2,0,1,0]
        j = [6,5,0]
        o = 12
        self.assertEqual(s.minSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,0,2,0]
        j = [1,4]
        o = -1
        self.assertEqual(s.minSum(i,j), o)

    def test_three(self):
        s = Solution()
        i = [0,16,28,12,10,15,25,24,6,0,0]
        j = [20,15,19,5,6,29,25,8,12]
        o = 139
        self.assertEqual(s.minSum(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,2,3,2]
        j = [1,4,3]
        o = 8
        self.assertEqual(s.minSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)