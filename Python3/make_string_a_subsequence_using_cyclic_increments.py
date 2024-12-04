# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 0-indexed strings str1 and str2.

    In an operation, select a set of indices in str1, and for each index i in
    the set, increment str1[i] to the next character cyclically. That is 'a'
    becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

    Return true if it is possible to make str2 a subsequence of str1 by
    performing the operation at most once, and false otherwise.

    Note: A subsequence of a string is a new string that is formed from the
    original string by deleting some (possibly none) of the characters without
    disturbing the relative positions of the remaining characters.
    '''
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        d = {i:chr(ord(i)+1) for i in "abcdefghijklmnopqrstuvwxyz"}
        d['z'] = 'a'
        j = 0
        for i in range(len(str1)):
            if j < len(str2) and (str1[i] == str2[j] or d[str1[i]] == str2[j]):
                j += 1
        return j == len(str2)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc", "ad"
        o = True
        self.assertEqual(s.canMakeSubsequence(*i), o)

    def test_two(self):
        s = Solution()
        i = "zc", "ad"
        o = True
        self.assertEqual(s.canMakeSubsequence(*i), o)

    def test_three(self):
        s = Solution()
        i = "ab", "d"
        o = False
        self.assertEqual(s.canMakeSubsequence(*i), o)

    def test_four(self):
        s = Solution()
        i = "dm", "e"
        o = True
        self.assertEqual(s.canMakeSubsequence(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)