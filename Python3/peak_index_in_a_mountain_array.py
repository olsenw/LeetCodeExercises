# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An array arr is a mountain if the following properties hold:
    * arr.length >= 3
    * There exists some i with 0 < i < arr.length - 1 such that
      arr[0] < arr[1] < ... < arr[i] < ... < arr[-2] < arr[-1]
    
    Given a mountain array, return the index of the peak of the mountain.

    Solve it in O(log(arr.length)) time complexity.
    '''
    # abuses the fact that input array has to be mountain
    # O(len(arr)) time...
    def peakIndexInMountainArray_max(self, arr: List[int]) -> int:
        return max(range(len(arr)), key=lambda x:arr[x])

    # O(len(arr)) time...
    def peakIndexInMountainArray_early(self, arr: List[int]) -> int:
        for i in range(1, len(arr) - 1):
            if arr[i+1] < arr[i]:
                return i
        return 0

    # binary search
    # O(log(len(arr))) time...
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i,j = 0, len(arr) - 2
        while i < j:
            m = (i + j) // 2
            if arr[m] >= arr[m+1]:
                j = m
            else:
                i = i + 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,1,0]
        o = 1
        self.assertEqual(s.peakIndexInMountainArray(i), o)

    def test_two(self):
        s = Solution()
        i = [0,2,1,0]
        o = 1
        self.assertEqual(s.peakIndexInMountainArray(i), o)

    def test_three(self):
        s = Solution()
        i = [0,10,5,2]
        o = 1
        self.assertEqual(s.peakIndexInMountainArray(i), o)

    def test_four(self):
        s = Solution()
        i = [0,1,2,3,5,2,0]
        o = 4
        self.assertEqual(s.peakIndexInMountainArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)