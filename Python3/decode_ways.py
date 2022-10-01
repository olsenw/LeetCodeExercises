# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A message containing letters from A-Z can be encoded into numbers using the
    following mapping:
      'A' -> "1"
      'B' -> "2"
      ...
      'Z' -> "26"
    
    To decode an encoded message, all the digits must be grouped then mapped
    back into letters using the reverse of the mapping above (there may be
    multiple ways). For example, "11106" can be mapped into:
    * "AAJF" with the grouping (1 1 10 6)
    * "KJF" with the grouping (11 10 6)

    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped
    into 'F' since "6" is different from "06".

    Given a string s containing only digits, return the number of ways to decode
    it.

    The test cases are generated so that the answer fits in a 32-bit integer.
    '''
    def numDecodings_wrong(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) > 1 and s[1] == '0' and s[0] != '1' and s[0] != '2':
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] == '0' and s[i-1] != '1' and s[i-1] != '2':
                return 0
            elif s[i] == '0':
                dp[i] = dp[i-1]
            elif '1' <= s[i-1] <= '2' and '0' <= s[i] <= '6':
                dp[i] = dp[i-1] + 2
            else:
                dp[i] = dp[i-1] + 1
        return dp[-1]

    def numDecodings_fails(self, s: str) -> int:
        @cache
        def dp(i):
            if i >= len(s):
                return 1
            a = dp(i+1) if s[i] != '0' else 0
            b = dp(i+2) if i+1 < len(s) and '1' <= s[i] <= '2' and '0' <= s[i+1] <= '6' else 0
            return a + b
        return dp(0)

    # based on discussion post by Abhishek-Kakoriya
    # https://leetcode.com/problems/decode-ways/discuss/2644133/Decode-Ways-or-Dynamic-Programming-or-41ms
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i+1]
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and '0' <= s[i+1] <= '6'):
                dp[i] += dp[i+2]
        return dp[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "12"
        o = 2
        self.assertEqual(s.numDecodings(i), o)

    def test_two(self):
        s = Solution()
        i = "226"
        o = 3
        self.assertEqual(s.numDecodings(i), o)

    def test_three(self):
        s = Solution()
        i = "06"
        o = 0
        self.assertEqual(s.numDecodings(i), o)

    def test_four(self):
        s = Solution()
        i = "11106"
        o = 2
        self.assertEqual(s.numDecodings(i), o)

    def test_five(self):
        s = Solution()
        i = "2611055971756562"
        o = 4
        self.assertEqual(s.numDecodings(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)