# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
from math import ceil, floor
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two positive integers n and x.

    Return the number of ways n cab be expressed as the sum of the xth power of
    unique positive integers, in other words, the number of sets of unique
    integers [n1, n2, ..., nk] where n = n1^x + n2^x + ... + nk^x.

    Since the answer can be very large, return it modulo 10**9 + 7.
    '''
    # double dips are possible
    def numberOfWays_fails(self, n: int, x: int) -> int:
        def dp(n:int) -> int:
            if n < 0:
                return 0
            if n == 0:
                return 1
            answer = 0
            for i in range(floor(n ** (1/x)), 0, -1):
                a = dp(n - (i ** x))
                if a > 0:
                    answer += a
            return answer
        return dp(n)

    # 1500 / 1502
    # case of n = 125 x = 3
    # note 5 ^ 3 = 125
    # however 125 ^ (1/3) = 4.9999999999999999999999
    # floor undercuts due to rounding
    def numberOfWays_fails(self, n: int, x: int) -> int:
        m = 10**9 + 7
        powers = [i ** x for i in range(1, floor(n ** (1 / x) + 1))]
        @cache
        def dp(i:int, n:int) -> int:
            if n == 0:
                return 1
            if n < 0 or i == len(powers):
                return 0
            answer = 0
            answer = (answer % m + dp(i+1, n - powers[i]) % m) % m
            answer = (answer % m + dp(i+1, n) % m) % m
            return answer
        return dp(0,n)

    # passes all test cases 1502/1502 but memory limit is exceeded
    def numberOfWays_memory(self, n: int, x: int) -> int:
        m = 10**9 + 7
        powers = [i ** x for i in range(1, ceil(n ** (1 / x) + 1))]
        @cache
        def dp(i:int, n:int) -> int:
            if n == 0:
                return 1
            if n < 0 or i == len(powers):
                return 0
            answer = 0
            answer = (answer % m + dp(i+1, n - powers[i]) % m) % m
            answer = (answer % m + dp(i+1, n) % m) % m
            return answer
        return dp(0,n)

    def numberOfWays(self, n: int, x: int) -> int:
        m = 10**9 + 7
        powers = [i ** x for i in range(1, ceil(n ** (1 / x) + 1))]
        @cache
        def dp(i:int, n:int) -> int:
            if n == 0:
                return 1
            if n < 0 or i < 0:
                return 0
            answer = 0
            answer = (answer % m + dp(i-1, n - powers[i]) % m) % m
            answer = (answer % m + dp(i-1, n) % m) % m
            return answer
        return dp(len(powers) - 1,n)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10
        j = 2
        o = 1
        self.assertEqual(s.numberOfWays(i,j), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = 1
        o = 2
        self.assertEqual(s.numberOfWays(i,j), o)

    def test_three(self):
        s = Solution()
        i = 160
        j = 3
        o = 1
        self.assertEqual(s.numberOfWays(i,j), o)

    def test_four(self):
        s = Solution()
        i = 300
        j = 1
        o = 872471266
        self.assertEqual(s.numberOfWays(i,j), o)

    def test_five(self):
        s = Solution()
        i = 125
        j = 3
        o = 1
        self.assertEqual(s.numberOfWays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)