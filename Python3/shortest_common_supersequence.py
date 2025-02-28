# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings str1 and str2, return the shortest string that has both
    str1 and str2 as subsequences. If there are multiple valid strings, return
    any of them.

    A string s is a subsequence of string t if deleting some number of
    characters from t (possibly 0) results in the string s.
    '''
    # incorrectly read hint
    def shortestCommonSupersequence_wrong(self, str1: str, str2: str) -> str:
        m,n = len(str1), len(str2)
        # hint 1) figure out the length of supersequence for each i,j in str1,str2
        # oops... should be finding longest common subsequence...
        @cache
        def dp(i:int, j:int) -> int:
            if i == m or j == n:
                return max(m-i, n-j)
            if str1[i:] == str2[j:]:
                return m - i
            answer = m-i + n-j
            for k in range(i,m):
                if str1[k] == str2[j]:
                    answer = min(answer, k - i + 1 + dp(k+1, j+1))
            for k in range(j,n):
                if str1[i] == str2[k]:
                    answer = min(answer, k - j + 1 + dp(i+1, k+1))
            return answer
        length = dp(0,0)
        if length == max(m,n):
            return str1 if m > n else str2
        add = length - max(m,n)
        return ""

    # read hint but went wrong direction, not solving anything useful
    def shortestCommonSupersequence_wrong(self, str1: str, str2: str) -> str:
        m,n = len(str1), len(str2)
        dp = [[-1] * n for _ in range(m)]
        # hint 1) find length of longest common subsequence
        def f(i:int,j:int)->int:
            if i == m or j == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            answer = 0
            for a in range(i,m):
                for b in range(j,n):
                    answer = max(answer, f(a, b+1), f(a+1, b))
                    if str1[a] == str2[b]:
                        answer = max(answer, 1 + f(a+1, b+1))
            dp[i][j] = answer
            return answer
        f(0,0)
        # hint 2 build the answer
        return

    # based on LeetCode Bottom-up Dynamic Programming solution
    # https://leetcode.com/problems/shortest-common-supersequence/editorial/?envType=daily-question&envId=2025-02-28
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m,n = len(str1), len(str2)
        prev = [str2[:i] for i in range(n+1)]
        # rows
        for i in range(1,m+1):
            curr = [""] * (n+1)
            curr[0] = str1[:i]
            # columns
            for j in range(1, n+1):
                # character matches
                if str1[i-1] == str2[j-1]:
                    curr[j] = prev[j-1] + str1[i-1]
                else:
                    # skip character in str1
                    a = prev[j]
                    # skip character in str2
                    b = curr[j-1]
                    if len(a) < len(b):
                        curr[j] = a + str1[i-1]
                    else:
                        curr[j] = b + str2[j-1]
            prev = curr
        return prev[n]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abac", "cab"
        o = "cabac"
        self.assertEqual(s.shortestCommonSupersequence(*i), o)

    def test_two(self):
        s = Solution()
        i = "aaaaaaaa", "aaaaaaaa"
        o = "aaaaaaaa"
        self.assertEqual(s.shortestCommonSupersequence(*i), o)

    def test_three(self):
        s = Solution()
        i = "aaaa", "bbbb"
        o = "aaaabbbb"
        self.assertEqual(s.shortestCommonSupersequence(*i), o)

    def test_four(self):
        s = Solution()
        i = "bbabb", "bbcbb"
        o = "bbacbb"
        self.assertEqual(s.shortestCommonSupersequence(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)