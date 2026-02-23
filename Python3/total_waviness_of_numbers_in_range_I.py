# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers nums1 and nums2 representing an inclusive range
    [num1, num2].

    The waviness of a number is defined as the total count of its peaks and
    valleys:
    * A digit is a peak if it is strictly greater than both of its immediate
      neighbors.
    * A digit is a valley if it is strictly less than both of its immediate
      neighbors.
    * The first and last digits of a number cannot be peaks or valleys.
    * Any number with fewer than 3 digits has a waviness of 0.

    Return the total sum of waviness for all numbers in the range [num1, num2].
    '''
    def totalWaviness(self, num1: int, num2: int) -> int:
        @cache
        # def waviness(n:list[int]) -> int:
        def waviness(n:int) -> int:
            n = list(int(s) for s in str(n))
            answer = 0
            for i in range(1,len(n)-1):
                if n[i-1] < n[i] > n[i+1]:
                    answer += 1
                if n[i-1] > n[i] < n[i+1]:
                    answer += 1
            return answer
        answer = 0
        for n in range(num1, num2+1):
            # n = list(int(s) for s in str(n))
            answer += waviness(n)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 120
        j = 130
        o = 3
        self.assertEqual(s.totalWaviness(i,j), o)

    def test_two(self):
        s = Solution()
        i = 198
        j = 202
        o = 3
        self.assertEqual(s.totalWaviness(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4848
        j = 4848
        o = 2
        self.assertEqual(s.totalWaviness(i,j), o)

    def test_four(self):
        s = Solution()
        i = 1
        j = 166005
        o = 0
        self.assertEqual(s.totalWaviness(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)