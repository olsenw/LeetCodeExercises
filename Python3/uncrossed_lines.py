# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays nums1 and nums2. The arrays are written on a two
    separate horizontal lines, in the order given.

    It is possible to draw connecting lines (straight lines) between two numbers
    such that:
    * nums1[i] == nums2[j]
    * the line drawn does not intersect any other connecting (non-horizontal)
      line
    
    Note that a connecting line cannot intersect even at the endpoints (ie each
    number can only belong to one connecting line).

    Return the maximum number of connecting lines that can be drawn.
    '''
    # time limit exceeded (59 / 74 test cases)
    def maxUncrossedLines_tle(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(a,b,c,d):
            best = 0
            for i in range(a,b+1):
                for j in range(c,d+1):
                    if nums1[i] == nums2[j]:
                        best = max(best, dp(a,i-1,c,j-1) + dp(i+1,b,j+1,d) + 1)
            return best
        return dp(0, len(nums1) - 1, 0, len(nums2) - 1)

    # slow
    # would probably have issues with larger inputs
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i,j):
            best = 0
            for x in range(i, len(nums1)):
                for y in range(j, len(nums2)):
                    if nums1[x] == nums2[y]:
                        best = max(best, 1 + dp(x+1,y+1))
            return best
        return dp(0,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4,2]
        j = [1,2,4]
        o = 2
        self.assertEqual(s.maxUncrossedLines(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,5,1,2,5]
        j = [10,5,2,1,5,2]
        o = 3
        self.assertEqual(s.maxUncrossedLines(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,3,7,1,7,5]
        j = [1,9,2,5,1]
        o = 2
        self.assertEqual(s.maxUncrossedLines(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)