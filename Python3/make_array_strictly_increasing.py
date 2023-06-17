# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from bisect import bisect, bisect_left
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integer arrays arr1 and arr2, return the minimum number of
    operations (possibly zero) needed to make arr1 strictly increasing.

    In one operation, choose two indices
    0 <= i < arr1.length and 0 <= j < arr2.length and make an assignment
    arr1[i] = arr2[j].

    If there is no way to make arr1 strictly increasing, return -1.
    '''
    # hint for this problem is technically wrong... 
    # the second dp variable is not index in arr2, but last value looked at.
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # if all(arr1[i - 1] < arr1[i] for i in range(1, len(arr1))):
            # return 0
        err = len(arr2) + 1
        arr2 = list(sorted(set(arr2)))
        # index in arr1 and value of last element
        @cache
        def dp(i,prev):
            if i == len(arr1):
                return 0
            k = bisect_left(arr2, prev + 1)
            # must change this number in arr
            if arr1[i] <= prev:
                # if unable to change return impossible large number
                return dp(i + 1, arr2[k]) + 1 if k < len(arr2) else err
            # can keep or change this number
            return min(dp(i+1, arr1[i]), dp(i + 1, arr2[k]) + 1 if k < len(arr2) else err)
        answer = dp(0, -1)
        return answer if answer < err else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,5,3,6,7]
        j = [1,3,2,4]
        o = 1
        self.assertEqual(s.makeArrayIncreasing(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,5,3,6,7]
        j = [4,3,1]
        o = 2
        self.assertEqual(s.makeArrayIncreasing(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,5,3,6,7]
        j = [1,6,3,3]
        o = -1
        self.assertEqual(s.makeArrayIncreasing(i,j), o)

    def test_four(self):
        s = Solution()
        i = [4,5,6,3]
        j = [0,1,2]
        o = 3
        self.assertEqual(s.makeArrayIncreasing(i,j), o)

    def test_five(self):
        s = Solution()
        i = [5,4,3,2,1]
        j = [1,2,3,4,5]
        o = 4
        self.assertEqual(s.makeArrayIncreasing(i,j), o)

    def test_six(self):
        s = Solution()
        i = [90,8,7,6]
        j = [10,20,30,40,50]
        o = 4
        self.assertEqual(s.makeArrayIncreasing(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)