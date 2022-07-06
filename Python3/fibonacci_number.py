# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from functools import cache
from math import sqrt

class Solution:
    '''
    The Fibonacci numbers commonly denoted F(n) form a sequence, called
    the Fibonacci sequence, such that each number is the sum of the two
    preceding ones, starting from 0 and 1. That is:
        F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2), for n > 1
    
    Given n, calculate F(n).
    '''
    def fib_dynamic(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    def fib_memoization(self, n: int) -> int:
        if n < 2:
            return n
        n1, n2 = 1, 0
        for i in range(2,n+1):
            n = n1 + n2
            n2 = n1
            n1 = n
        return n1

    @cache
    def fib_cached_recursion(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n-1) + self.fib(n-2)

    # https://www.geeksforgeeks.org/fibonacci-sequence-formula/
    def fib_golden_ratio(self, n: int) -> int:
        return (1.618034**n - (1-1.618034)**n) // sqrt(5)
        # for leetcode submission
        # return int((1.618034**n - (1-1.618034)**n) / sqrt(5))

class UnitTesting(unittest.TestCase):
    def test_zero(self):
        s = Solution()
        i = 0
        o = 0
        self.assertEqual(s.fib(i), o)

    def test_one(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.fib(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 1
        self.assertEqual(s.fib(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = 2
        self.assertEqual(s.fib(i), o)

    def test_four(self):
        s = Solution()
        i = 4
        o = 3
        self.assertEqual(s.fib(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)