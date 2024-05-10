# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a sorted integer array arr counting 1 and prime numbers, where all the
    integers of arr are unique. Also given an integer k.

    For every i and j where 0 <= i < j < arr.length, consider the fraction
    arr[i] / arr[j].

    Return the kth smallest fraction considered. Return an answer as an array of
    integers of size 2, where answer[0] == arr[i] and answer[j] == arr[j].
    '''
    # O(n^2) - passes
    def kthSmallestPrimeFraction_brute(self, arr: List[int], k: int) -> List[int]:
        arr = [(arr[i] / arr[j], [arr[i],arr[j]]) for i in range(len(arr)) for j in range(i+1, len(arr))]
        arr.sort()
        return arr[k-1][1]

    '''
    See LeetCode editorial for how to do it in O(n log m^2) or O((n+k) log n) time
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,5]
        j = 3
        o = [2,5]
        self.assertEqual(s.kthSmallestPrimeFraction(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,7]
        j = 1
        o = [1,7]
        self.assertEqual(s.kthSmallestPrimeFraction(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,5,7,11,13,17,19,23,9739,9743,9749,9767,9769,9781,9787,9791,9803,9811,9817,9829,9833,9839,9851,9857,9859,9871,9883,9887,9901,9907,9923,9929,9931,9941,9949,9967,9973]
        j = 32
        o = [2,9949]
        self.assertEqual(s.kthSmallestPrimeFraction(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)