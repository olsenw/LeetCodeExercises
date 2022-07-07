# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from functools import cache

class Solution:
    '''
    Given strings s1, s2, and s3, find whether s3 is formed by an
    interleaving of s1 and s2.

    An interleaving of two strings s and t is a configuration where they
    are divided into non-empty substrings such that:
    * s = s1 + s2 + ... + sn
    * t = t1 + t2 + ... + tn
    * |n - m| <= 1
    * The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 +
      t2 + s2 + t3 + s3 + ...

    Note: a + b is the concatenation of strings a and b.
    '''
    @cache
    def isInterleave_dp(self, s1: str, s2: str, s3: str) -> bool:
        if not len(s3):
            return not len(s1) and not len(s2)
        # build a tree of taking character from either string?
        if len(s1) and s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:]):
            return True
        if len(s2) and s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:]):
            return True
        return False

    def isInterleave_dp_improved(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dp(i,j):
            if i + j == len(s3):
                return i == len(s1) and j == len(s2)
            if i < len(s1) and s1[i] == s3[i + j] and dp(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dp(i, j + 1):
                return True
            return False
        return dp(0, 0)

    '''
    There is a follow up to use only O(n) space... It is done using a 1D
    (as opposed to the above solution 2D) dynamic programming array that
    stores the string prefix along the current path. (ie it will be
    overwritten during a backtrack)

    See Leetcode Solutions for how to do it.
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aabcc"
        j = "dbbca"
        k = "aadbbcbcac"
        o = True
        self.assertEqual(s.isInterleave(i, j, k), o)

    def test_two(self):
        s = Solution()
        i = "aabcc"
        j = "dbbca"
        k = "aadbbbaccc"
        o = False
        self.assertEqual(s.isInterleave(i, j, k), o)

    def test_three(self):
        s = Solution()
        i = ""
        j = ""
        k = ""
        o = True
        self.assertEqual(s.isInterleave(i, j, k), o)

    def test_four(self):
        s = Solution()
        i = "a"
        j = "b"
        k = "a"
        o = False
        self.assertEqual(s.isInterleave(i, j, k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)