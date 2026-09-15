# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and a positive integer k.

    Select a set of non-overlapping substrings from the string s that satisfy
    the following conditions:
    * The length of the each substring is at least k.
    * Each substring is a palindrome.

    Return the maximum number of substrings in an optimal selection.

    A substring is a contiguous sequence of characters within a string.
    '''
    def maxPalindromes_tle(self, s: str, k: int) -> int:
        @cache
        def dp(i:int) -> int:
            if i < k - 1:
                return 0
            answer = dp(i-1)
            for j in range(i-k,-1,-1):
                if s[j:i] == s[j:i][::-1]:
                    answer = max(answer, 1 + dp(j))
                else:
                    answer = max(answer, dp(j))
            return answer
        a = [dp(i) for i in range(len(s)+1)]
        return dp(len(s))

    # based on leetcode editorial
    # https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/editorial/?envType=daily-question&envId=2026-09-15
    # big difference is precomputing all the palindromes
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        isPalindrome = [[False] * n for _ in range(n)]
        for length in range(1,n+1):
            for left in range(n - length + 1):
                right = left + length - 1
                isPalindrome[left][right] = s[left] == s[right] and (length <= 2 or isPalindrome[left+1][right-1])
        dp = [0] * (n+1)
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            for j in range(i-k+1):
                if isPalindrome[j][i-1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[n]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        #    012345678
        i = "abaccdbbd"
        j = 3
        o = 2
        self.assertEqual(s.maxPalindromes(i,j), o)

    def test_two(self):
        s = Solution()
        i = "adbcda"
        j = 2
        o = 0
        self.assertEqual(s.maxPalindromes(i,j), o)

    def test_three(self):
        s = Solution()
        i = "rzdtuheehuolxbhcychbpmcmxxxxxxiywqwyierjsuusjreunvvnu"
        j = 4
        o = 6
        self.assertEqual(s.maxPalindromes(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)