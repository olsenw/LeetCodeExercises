# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of integers arr, return true if and only if it is a
    valid mountain array.

    An array is a mountain array if and only if:
    * arr.length >= 3
    * There exists some i with 0 < i < arr.length-1 such that
        1) arr[0] < arr[1] < ... < arr[i-1] < arr[i]
        2) arr[i] > arr[i+1] > ... > arr[arr.length-1]
    '''
    def validMountainArray(self, arr: List[int]) -> bool:
        # check less than 3 and intially asscending
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False
        asscending = True
        past = arr[0]
        for i in arr[1:]:
            # array currently asscending
            if asscending:
                # stopped asscending
                if i < past:
                    asscending = False
                # staggered asscention which is fail case
                elif i == past:
                    return False
            else:
                # staggered decending or re-asscending 
                if past <= i:
                    return False
            past = i
        return not asscending

    # Leetcode solution for reference (simplier...)
    # https://leetcode.com/problems/valid-mountain-array/solution/
    def validMountainArray_leetcode(self, arr: List[int]) -> bool:   
        N = len(arr)
        i = 0

        # walk up
        while i+1 < N and arr[i] < arr[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and arr[i] > arr[i+1]:
            i += 1

        return i == N-1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1]
        o = False
        self.assertEqual(s.validMountainArray(i), o)
        self.assertEqual(s.validMountainArray_leetcode(i), o)

    def test_two(self):
        s = Solution()
        i = [3,5,5]
        o = False
        self.assertEqual(s.validMountainArray(i), o)
        self.assertEqual(s.validMountainArray_leetcode(i), o)

    def test_three(self):
        s = Solution()
        i = [0,3,2,1]
        o = True
        self.assertEqual(s.validMountainArray(i), o)
        self.assertEqual(s.validMountainArray_leetcode(i), o)

    def test_four(self):
        s = Solution()
        i = [0,2,3,4,5,2,1,0]
        o = True
        self.assertEqual(s.validMountainArray(i), o)
        self.assertEqual(s.validMountainArray_leetcode(i), o)

    def test_five(self):
        s = Solution()
        i = [0,2,3,3,5,2,1,0]
        o = False
        self.assertEqual(s.validMountainArray(i), o)
        self.assertEqual(s.validMountainArray_leetcode(i), o)

    def test_six(self):
        s = Solution()
        i = [0,1,2,3,4,5,6,7,8,9]
        o = False
        self.assertEqual(s.validMountainArray(i), o)
        self.assertEqual(s.validMountainArray_leetcode(i), o)

    def test_seven(self):
        s = Solution()
        i = [9,8,7,6,5,4,3,2,1,0]
        o = False
        self.assertEqual(s.validMountainArray(i), o)
        self.assertEqual(s.validMountainArray_leetcode(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)