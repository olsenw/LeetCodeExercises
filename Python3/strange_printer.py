# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a strange printer with the following two special properties:
    * The printer can only print a sequence of the same character each time.
    * At each turn, the printer can print new characters starting from and
      ending at any place and will cover the original existing characters.
    
    Given a string s, return the minimum number of turns the printers needed to
    print it.
    '''
    def strangePrinter_tle(self, s: str) -> int:
        n = len(s)
        se: dict[str, list[list[int]]] = dict()
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                j += 1
            if s[i] in se:
                se[s[i]].append([i, j - 1])
            else:
                se[s[i]] = [[i, j - 1]]
            i = j
        @cache
        def dp(state):
            # if state == s:
            #     return 0
            a = 101
            i = 0
            while i < n:
                if state[i] != s[i]:
                    for j,k in reversed(se[s[i]]):
                        if j < i:
                            break
                        a = min(a, 1 + dp(state[:i] + s[i] * (k - i + 1) + state[k+1:]))
                    else:
                        i = k
                i += 1
            return a if a < 101 else 0
        return dp("*" * n)

    # LeetCode solution
    # https://leetcode.com/problems/strange-printer/editorial/
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[n] * n for _ in range(n)]
        for length in range(1,n+1):
            for left in range(n - length + 1):
                right = left + length - 1
                j = -1
                for i in range(left, right):
                    if s[i] != s[right] and j == -1:
                        j = i
                    if j != -1:
                        dp[left][right] = min(dp[left][right], 1 + dp[j][i] + dp[i+1][right])
                if j == -1:
                    dp[left][right] = 0
        return dp[0][n-1] + 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aaabbb"
        o = 2
        self.assertEqual(s.strangePrinter(i), o)

    def test_two(self):
        s = Solution()
        i = "aba"
        o = 2
        self.assertEqual(s.strangePrinter(i), o)

    def test_three(self):
        s = Solution()
        i = "aaaabbbbbbbaaaaaaaabbbbbbbaabbbbbbba"
        o = 4
        self.assertEqual(s.strangePrinter(i), o)

    def test_four(self):
        s = Solution()
        i = "abababaabababaabababa"
        o = 10
        self.assertEqual(s.strangePrinter(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)