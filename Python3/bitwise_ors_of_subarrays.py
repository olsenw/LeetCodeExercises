# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array arr, return the number of distinct bitwise ORs of all
    the non-empty subarrays of arr.

    The bitwise OR of a subarray is the bitwise OR of each integer in the
    subarray. The bitwise OR of a subarray of one integer is that integer.

    A subarray is a contiguous non-empty sequence of elements within an array.
    '''
    def subarrayBitwiseORs_brute(self, arr: List[int]) -> int:
        s = set()
        for i in range(len(arr)):
            a = arr[i]
            for j in range(i, len(arr)):
                a |= arr[j]
                s.add(a)
        return len(s)

    # based on Leetcode editorial
    # https://leetcode.com/problems/bitwise-ors-of-subarrays/?envType=daily-question&envId=2025-07-31
    # this works because the maximum size of answer is 32
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        answer = set()
        curr = {0}
        for a in arr:
            curr = {a | i for i in curr}.union({a})
            answer = answer.union(curr)
        return len(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0]
        o = 1
        self.assertEqual(s.subarrayBitwiseORs(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2]
        o = 3
        self.assertEqual(s.subarrayBitwiseORs(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,4]
        o = 6
        self.assertEqual(s.subarrayBitwiseORs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)