# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array arr, remove a subarray (can be empty) from arr such
    that the remaining elements in arr are non-decreasing.

    Return the length of the shortest subarray to remove.

    A subarray is a contiguous subsequence of the array.
    '''
    def findLengthOfShortestSubarray_(self, arr: List[int]) -> int:
        i,j = 0, len(arr) - 1
        a,b = 0, 10**9 + 1
        while i < len(arr) and arr[i] >= a:
            a = arr[i]
            i += 1
        while j >= 0 and arr[j] <= b:
            b = arr[j]
            j -= 1
        if i < j:
            return 0
        return
    
    def findLengthOfShortestSubarray_fails(self, arr: List[int]) -> int:
        i,j = 0, len(arr) - 1
        while i < j and arr[i] <= arr[j]:
            i += 1
            j -= 1
        return j - i

    # based on leetcode editorial
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i,j = 0, len(arr) - 1
        # find sorted right portion of the array
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1
        answer = j
        while i < j and (i == 0 or arr[i - 1] <= arr[i]):
            while j < len(arr) and arr[i] > arr[j]:
                j += 1
            answer = min(answer, j - i -1)
            i += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,10,4,2,3,5]
        o = 3
        self.assertEqual(s.findLengthOfShortestSubarray(i), o)

    def test_two(self):
        s = Solution()
        i = [5,4,3,2,1]
        o = 4
        self.assertEqual(s.findLengthOfShortestSubarray(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3]
        o = 0
        self.assertEqual(s.findLengthOfShortestSubarray(i), o)

    def test_four(self):
        s = Solution()
        i = [1,2]
        o = 0
        self.assertEqual(s.findLengthOfShortestSubarray(i), o)

    def test_five(self):
        s = Solution()
        i = [1,1,1,1,1]
        o = 0
        self.assertEqual(s.findLengthOfShortestSubarray(i), o)

    def test_six(self):
        s = Solution()
        i = [1,1,10,1,1]
        o = 1
        self.assertEqual(s.findLengthOfShortestSubarray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)