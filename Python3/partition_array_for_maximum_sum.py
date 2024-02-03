# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array arr, partition the array into (contiguous) subarrays
    of length at most k. After partitioning, each subarray has their values
    changed to become the maximum value of that subarray.

    Return the largest sum of the given array after partitioning. Test cases are
    generated so that the answer fits in a 32-bit integer.
    '''
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache
        def dp(i):
            if i >= len(arr):
                return 0
            a = arr[i]
            answer = a + dp(i+1)
            for j in range(i+1, min(i+k, len(arr))):
                a = max(a, arr[j])
                answer = max(answer, a * (j - i + 1) + dp(j+1))
                pass
            return answer
        return dp(0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,15,7,9,2,5,10]
        j = 3
        o = 84
        self.assertEqual(s.maxSumAfterPartitioning(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,4,1,5,7,3,6,1,9,9,3]
        j = 4
        o = 83
        self.assertEqual(s.maxSumAfterPartitioning(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1]
        j = 1
        o = 1
        self.assertEqual(s.maxSumAfterPartitioning(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)