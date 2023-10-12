# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
   def __init__(self, arr) -> None:
       self.arr = arr
   def get(self, index: int) -> int:
       return self.arr[index]
   def length(self) -> int:
       return len(self.arr)

class Solution:
    '''
    A array arr is a mountain array if and only if:
    * arr.length >= 3
    * There exists some i with 0 < i < arr.length - 1 such that:
      * arr[0] < arr[1] < ... < arr[i-1] < arr[i]
      * arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    
    Given a mountain array mountainArr, return the minimum index such that
    mountainArr.get(index) == target. If such an index does not exist, return
    -1.

    The mountain array cannot be accessed directly. It can only be accessed via
    a MountainArray interface:
    * MountainArray.get(k) returns the element of the array at index k
      (0-indexed).
    * MountainArray.length() returns the length of the array.

    Submissions that make more than 100 calls to MountainArray.get will be
    judged as a Wrong Answer.
    '''
    # based on editorial
    # https://leetcode.com/problems/find-in-mountain-array/editorial/?envType=daily-question&envId=2023-10-12
    # kept messing up the binary search
    # does not do early stop or cache
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        i,j = 1, n-2
        # find the peak
        while i < j:
            k = (j - i) // 2 + i
            l,r = mountain_arr.get(k), mountain_arr.get(k + 1)
            if l < r:
                i = k + 1
            else:
                j = k
        if mountain_arr.get(i) == target:
            return i
        peak = i
        # search target on left side of mountain
        i,j = 0, peak
        while i < j:
            k = (j - i) // 2 + i
            v = mountain_arr.get(k)
            if v < target:
                i = k + 1
            else:
                j = k
        if mountain_arr.get(i) == target:
            return i
        # search target on right side of mountain
        i,j = peak, n-1
        while i < j:
            k = (j - i) // 2 + i
            v = mountain_arr.get(k)
            if v > target:
                i = k + 1
            else:
                j = k
        if mountain_arr.get(i) == target:
            return i
        return -1

class UnitTesting(unittest.TestCase):
    # tested online due to interactive nature of problem

    def test_one(self):
        s = Solution()
        i = MountainArray([1,2,3,4,5])
        j = 3
        o = 2
        self.assertEqual(s.findInMountainArray(j,i), o)

    def test_two(self):
        s = Solution()
        i = MountainArray([0,1,2,4,2,1])
        j = 3
        o = -1
        self.assertEqual(s.findInMountainArray(j,i), o)

    def test_three(self):
        s = Solution()
        i = MountainArray([1,2,4,2,1,0])
        j = 3
        o = -1
        self.assertEqual(s.findInMountainArray(j,i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)