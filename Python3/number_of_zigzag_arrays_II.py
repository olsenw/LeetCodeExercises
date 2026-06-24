# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given three integers n, l, and r.

    A ZigZag array of length n is defined as follows:
    * Each element lies in the range [l, r].
    * No two adjacent elements are equal.
    * No three consecutive elements form a strictly increasing or strictly
      decreasing sequence.

    Return the total number of valid ZigZag arrays.

    Since the answer may be large, return it modulo 10^9 + 7.

    A sequence is said to be strictly increasing if each element is strictly
    greater than its previous one (if exists).

    A sequence is said to be strictly decreasing if each element is strictly
    smaller than its previous one (if exists).
    '''
    MOD = 10**9 + 7

    def mul(self, a, b):
        n = len(a)
        m = len(b[0])
        answer = [[0] * m for _ in range(n)]
        for i in range(n):
            for k in range(len(a[0])):
                r = a[i][k]
                if r == 0:
                    continue
                for j in range(m):
                    answer[i][j] = (answer[i][j] + r * b[k][j]) % self.MOD
        return answer
    
    def powMul(self, base, exponent, answer):
        while exponent > 0:
            if exponent & 1:
                answer = self.mul(answer, base)
            base = self.mul(base, base)
            exponent //= 2
        return answer

    # based on editorial
    # https://leetcode.com/problems/number-of-zigzag-arrays-ii/editorial/?envType=daily-question&envId=2026-06-24
    # Change from previous problem is input is much longer (when if narrower)
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        if n == 1:
            return m
        
        size = 2 * m
        u = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(i):
                u[i][j + m] = 1
            for j in range(i+1, m):
                u[i + m][j] = 1
        
        dp = [[1] * size]
        dp = self.powMul(u, n-1, dp)
        answer = 0
        for i in range(size):
            answer = (answer + dp[0][i]) % self.MOD
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3,4,5
        o = 2
        self.assertEqual(s.zigZagArrays(*i), o)

    def test_two(self):
        s = Solution()
        i = 3,1,3
        o = 10
        self.assertEqual(s.zigZagArrays(*i), o)

    def test_three(self):
        s = Solution()
        i = 673333,23,27
        o = 372342446
        self.assertEqual(s.zigZagArrays(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)