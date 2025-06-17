# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

MOD = 10**9 + 7
MX = 10 ** 5
fact = [0] * MX
inv_fact = [0] * MX

def qpow(x,n):
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res

def init():
    # only run this the once
    if fact[0] != 0:
        return
    fact[0] = 1
    for i in range(1, MX):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[MX - 1] = qpow(fact[MX - 1], MOD - 2)
    for i in range(MX - 1, 0, -1):
        inv_fact[i-1] = inv_fact[i] * i % MOD 

def comb(n,m):
    return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD

class Solution:
    '''
    Given three integers n, m, k. A good array arr of size n is defined a
    follows:
    * Each element in arr is in the inclusive range [1, m].
    * Exactly k indices i (where 1 <= i < n) satisfy the condition
      arr[i-1] == arr[i].

    Return the number of good arrays that can be formed.

    Since the answer may be very large, return it modulo 10^9 + 7.
    '''
    # based on LeetCode editorial
    # https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/editorial/?envType=daily-question&envId=2025-06-17
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        init()
        return comb(n-1, k) * m % MOD * qpow(m - 1, n - k - 1) % MOD

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = 2
        k = 1
        o = 4
        self.assertEqual(s.countGoodArrays(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = 2
        k = 2
        o = 6
        self.assertEqual(s.countGoodArrays(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 5
        j = 2
        k = 0
        o = 2
        self.assertEqual(s.countGoodArrays(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 5581
        j = 58624
        k = 4766
        o = 846088010
        self.assertEqual(s.countGoodArrays(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)