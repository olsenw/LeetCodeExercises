# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers arr, return the sum of all possible
    odd-length subarrays of arr.

    A sub array is a contiguous subsequence of the array.
    '''
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        answer = 0
        for w in range(1,n+1,2):
            s = sum(arr[:w])
            answer += s
            for j in range(w,n):
                s += arr[j] - arr[j - w]
                answer += s
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,4,2,5,3]
        o = 58
        self.assertEqual(s.sumOddLengthSubarrays(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        o = 3
        self.assertEqual(s.sumOddLengthSubarrays(i), o)

    def test_three(self):
        s = Solution()
        i = [10,11,12]
        o = 66
        self.assertEqual(s.sumOddLengthSubarrays(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)