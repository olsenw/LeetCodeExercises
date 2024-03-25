# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer k, return the minimum number of Fibonacci numbers whose sum
    is equal to k. The same Fibonacci number can be used multiple times.

    The Fibonacci numbers are defined as:
    * f1 = 1
    * f2 = 1
    * fn = fn-1 + fn-2 for n > 2

    It is guaranteed that for the given constraints it is always possible to
    find such Fibonacci numbers that sum up to k.
    '''
    # hint 2 points out a neat way to calculate, recursion
    def findMinFibonacciNumbers(self, k: int) -> int:
        # base case
        if k <= 1:
            return k
        # find largest Fibonacci <= k
        a,b = 1,1
        while b <= k:
            a,b = b,a+b
        # recurse for smaller value
        return 1 + self.findMinFibonacciNumbers(k - a)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 7
        o = 2
        self.assertEqual(s.findMinFibonacciNumbers(i), o)

    def test_two(self):
        s = Solution()
        i = 10
        o = 2
        self.assertEqual(s.findMinFibonacciNumbers(i), o)

    def test_three(self):
        s = Solution()
        i = 19
        o = 3
        self.assertEqual(s.findMinFibonacciNumbers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)