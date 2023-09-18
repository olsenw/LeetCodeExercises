# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An array arr is a mountain array if and only if:
    * arr.length >= 3
    * There exists some index i (0-indexed) with 0 < i < arr.length -1 such that
      * arr[0] < arr[1] < ... < arr[i-1] < arr[i]
      * arr[i] > arr[i+1] > ... > arr[arr.length - 1]
    
    Given an integer array arr, return the length of the longest subarray, which
    is a mountain. Return 0 if there is no such mountain subarray.
    '''
    def longestMountain(self, arr: List[int]) -> int:
        answer = 0
        for i in range(1,len(arr) - 1):
            if arr[i-1] < arr[i] > arr[i+1]:
                curr = 3
                for j in range(i - 1, 0, -1):
                    if arr[j - 1] >= arr[j]:
                        break
                    curr += 1
                for j in range(i + 1, len(arr) - 1):
                    if arr[j] <= arr[j+1]:
                        break
                    curr += 1
                answer = max(curr, answer)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,4,7,3,2,5]
        o = 5
        self.assertEqual(s.longestMountain(i), o)

    def test_two(self):
        s = Solution()
        i = [2,2,2]
        o = 0
        self.assertEqual(s.longestMountain(i), o)

    def test_three(self):
        s = Solution()
        i = [0,1,0]
        o = 3
        self.assertEqual(s.longestMountain(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)