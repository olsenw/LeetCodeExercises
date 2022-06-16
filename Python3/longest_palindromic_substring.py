# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from functools import cache
class Solution:
    # Memory limit exceeded
    def longestPalindrome_timeout(self, s: str) -> str:
        @cache
        def dp(i,j):
            if j < i:
                return 0
            if i == j:
                return 1
            if i + 1 == j:
                return 2 if s[i] == s[j] else 0
            if s[i] == s[j]:
                t = dp(i + 1, j - 1)
                return 2 + t if t else 0
            return 0
        m = a = b = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                k = dp(i, j)
                if m < k:
                    m, a, b = k, i, j
        return s[a:b+1]

    # passes but slow
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = 2
        for j in range(2, len(s)):
            for i in range(j):
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
        a = b = c = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if c < dp[i][j]:
                    a, b, c = i, j, dp[i][j]
        return s[a:b + 1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "babad"
        o = "bab"
        self.assertEqual(s.longestPalindrome(i), o)

    def test_two(self):
        s = Solution()
        i = "cbbd"
        o = "bb"
        self.assertEqual(s.longestPalindrome(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)