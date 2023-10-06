# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, break it into the sum of k positive integers, where
    k >= 2, and maximize the product of those integers.

    Return the maximum product possible.
    '''
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(i):
            # base case was off... needed editorial to point it out
            if i <= 3:
                return i
            best = max(i, 1 * dp(i - 1))
            for j in range(2, i // 2 + 1):
                best = max(best, dp(j) * dp(i - j))
            return best
        # return dp(n)
        # return max(dp(i) * dp(n-i) for i in range(1, n))
        return max(dp(i) * dp(n-i) for i in range(1, n // 2 + 1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        o = 1
        self.assertEqual(s.integerBreak(i), o)

    def test_two(self):
        s = Solution()
        i = 10
        o = 36
        self.assertEqual(s.integerBreak(i), o)

    def test_three(self):
        s = Solution()
        i = 20
        o = 1458
        self.assertEqual(s.integerBreak(i), o)

    def test_four(self):
        s = Solution()
        i = 50
        o = 86093442
        self.assertEqual(s.integerBreak(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)