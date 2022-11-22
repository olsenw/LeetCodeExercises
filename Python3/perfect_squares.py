# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
from re import S
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from math import isqrt

class Solution:
    '''
    Given an integer n, return the least number of perfect square numbers that
    sum to n.

    A perfect square is an integer that is the square of an integer, in other
    words, it is the product of some integer with itself. For example 1, 4, 9
    and 16 are perfect squares, while 3 and 11 are not.
    '''
    # may not always want the biggest square root number
    def numSquares_incorrect_greedy(self, n: int) -> int:
        c = 0
        while n > 1:
            x = isqrt(n)
            n -= x * x
            c += 1
        return c + 1

    # O(n^2) time
    @cache
    def numSquares_dp_tle(self, n: int) -> int:
        c = isqrt(n)
        if c * c == n:
            return 1
        return min(self.numSquares(x) + self.numSquares(n-x) for x in range(1,n//2 + 1))

    @cache
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        s = isqrt(n)
        if s * s == n:
            return 1
        dp = [n] * s
        for i in range(1,s):
            j = (i+1) ** 2
            dp[i] = n // j + self.numSquares(n % j)
        return min(dp)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.numSquares(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 2
        self.assertEqual(s.numSquares(i), o)

    def test_twelve(self):
        s = Solution()
        i = 12
        o = 3
        self.assertEqual(s.numSquares(i), o)

    def test_thirteen(self):
        s = Solution()
        i = 13
        o = 2
        self.assertEqual(s.numSquares(i), o)

    def test_6543(self):
        s = Solution()
        i = 6543
        o = 4
        self.assertEqual(s.numSquares(i), o)

    def test_4746(self):
        s = Solution()
        i = 4746
        o = 3
        self.assertEqual(s.numSquares(i), o)

    def test_516(self):
        s = Solution()
        i = 516
        o = 3
        self.assertEqual(s.numSquares(i), o)

    def test_513(self):
        s = Solution()
        i = 516
        o = 3
        self.assertEqual(s.numSquares(i), o)

    def test_500(self):
        s = Solution()
        i = 500
        o = 2
        self.assertEqual(s.numSquares(i), o)

    def test_8765(self):
        s = Solution()
        i = 8765
        o = 2
        self.assertEqual(s.numSquares(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)