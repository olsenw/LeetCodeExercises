# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, find the longest palindromic subsequence's length in s.

    A subsequence is a sequence that can be derived from another sequence by
    deleting some or no elements without changing the order of the remaining
    elements.
    '''
    # based on recursive dynamic programming solution by LeetCode
    # https://leetcode.com/problems/longest-palindromic-subsequence/editorial/
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def lps(i:int,j:int):
            if j < i:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return 2 + lps(i + 1, j - 1)
            return max(lps(i + 1, j), lps(i, j - 1))
        return lps(0, len(s) - 1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "bbbab"
        o = 4
        self.assertEqual(s.longestPalindromeSubseq(i), o)

    def test_two(self):
        s = Solution()
        i = "cbbd"
        o = 2
        self.assertEqual(s.longestPalindromeSubseq(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)