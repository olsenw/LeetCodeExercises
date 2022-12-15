# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two strings text1 and text2, return the length of their longest common
    subsequence. If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original string
    with some characters (can be none) deleted without changing the relative
    order of the remaining characters.

    A common subsequence of two strings is a subsequence that is common to both
    strings.
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i,j):
            # base case no more characters
            if i >= len(text1) or j >= len(text2):
                return 0
            # take a character
            a = 1 + dp(i+1, j+1) if text1[i] == text2[j] else 0
            # leave character text1
            b = dp(i+1, j)
            # leave character text2
            c = dp(i, j+1)
            return max(a,b,c)
        return dp(0,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcde"
        j = "ace"
        o = 3
        self.assertEqual(s.longestCommonSubsequence(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abc"
        j = "abc"
        o = 3 
        self.assertEqual(s.longestCommonSubsequence(i,j), o)

    def test_three(self):
        s = Solution()
        i = "abc"
        j = "def"
        o = 0
        self.assertEqual(s.longestCommonSubsequence(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)