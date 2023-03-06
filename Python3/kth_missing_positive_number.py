# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array arr of positive integers sorted in a strictly increasing
    order, and an integer k.

    Return the kth positive integer that is missing from this array.
    '''
    def findKthPositive_brute(self, arr: List[int], k: int) -> int:
        s = set(arr)
        answer = 0
        while k:
            answer += 1
            if answer not in s:
                k -= 1
        return answer

    # binary search solution from harshithdshetty
    # https://leetcode.com/problems/kth-missing-positive-number/solutions/3262072/python3-44-ms-faster-than-96-22-of-python3/
    # was unsure on the up down criteria so looked at answer
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i,j = 0, len(arr)-1
        while i <= j:
            m = (j-i)//2 + i
            if arr[m] - m - 1 < k:
                i = m + 1
            else:
                j = m - 1
        return i + k

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,4,7,11]
        j = 5
        o = 9
        self.assertEqual(s.findKthPositive(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        j = 2
        o = 6
        self.assertEqual(s.findKthPositive(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)