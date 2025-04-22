# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# calculate all prime factors for the problem space
modulo = 10**9 + 7
maxN = 10**4 + 10
maxP = 15
sieve = [0] * maxN
for i in range(2, maxN):
    if sieve[i] == 0:
        for j in range(i, maxN, i):
            sieve[j] = i
ps = [[] for _ in range(maxN)]
for i in range(2, maxN):
    x = i
    while x > 1:
        p = sieve[x]
        c = 0
        while x % p == 0:
            x //= p
            c += 1
        ps[i].append(c)
c = [[0] * (maxP + 1) for _ in range(maxN + maxP)]
c[0][0] = 1
for i in range(1, maxN + maxP):
    c[i][0] = 1
    for j in range(1, min(i, maxP) + 1):
        c[i][j] = (c[i-1][j] + c[i-1][j-1]) % modulo

class Solution:
    '''
    Given two integers n and maxValue, which are used to describe an ideal
    array.

    A 0-indexed integer array arr of length n is considered ideal if the
    following conditions hold:
    * Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
    * Every arr[i] is divisible by arr[i-1], for 0 < i < n.

    Return the number of distinct ideal arrays of length n. Since the answer may
    be very large, return it modulo 10^9 + 7.
    '''
    modulo = 10**9 + 7
    # exceeds time limit for large n and maxValue
    def idealArrays_tle(self, n: int, maxValue: int) -> int:
        @cache
        def dp(low:int, index:int) -> int:
            if index == n:
                return 1
            answer = 0
            for v in range(low, maxValue+1, low):
                answer = ((answer % self.modulo) + (dp(v, index + 1) % self.modulo)) % self.modulo
            return answer
        return dp(1, 0)

    # based on LeetCode solution
    # https://leetcode.com/problems/count-the-number-of-ideal-arrays/editorial/?envType=daily-question&envId=2025-04-22
    # see precalculation code before the class is defined
    def idealArrays(self, n: int, maxValue: int) -> int:
        answer = 0
        for x in range(1, maxValue + 1):
            m = 1
            for p in ps[x]:
                m = m * c[n + p - 1][p] % self.modulo
            answer = (answer + m) % self.modulo
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2,5
        o = 10
        self.assertEqual(s.idealArrays(*i), o)

    def test_two(self):
        s = Solution()
        i = 5,3
        o = 11
        self.assertEqual(s.idealArrays(*i), o)

    def test_three(self):
        s = Solution()
        i = 500,500
        o = 652553975
        self.assertEqual(s.idealArrays(*i), o)

    def test_four(self):
        s = Solution()
        i = 1000,1000
        o = 91997497
        self.assertEqual(s.idealArrays(*i), o)

    def test_five(self):
        s = Solution()
        i = 10000,10000
        o = 22940607
        self.assertEqual(s.idealArrays(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)