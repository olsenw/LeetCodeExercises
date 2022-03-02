# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two strings s and t, return true if s is a subsequence of t,
    or false otherwise.

    A subsequence of a string is a new string that is formed from the
    original string by deleting some (can be none) of the characters
    without disturbing the relative positions of the remaining
    characters. (ie "ace" is a subsequence of "abcde" -> "[a]b[c]d[e]"
    while "aec" is not)
    '''
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 # for s
        j = 0 # for t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def isSubsequence_iter(self, s: str, t: str) -> bool:
        i = iter(t)
        for c in s:
            # keep going through t till find letter from s
            while True:
                try:
                    # found it
                    if c == next(i):
                        break
                # no more letters in t
                except StopIteration:
                    return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        j = "ahbgdc"
        o = True
        self.assertEqual(s.isSubsequence(i,j), o)
        self.assertEqual(s.isSubsequence_iter(i,j), o)

    def test_two(self):
        s = Solution()
        i = "axc"
        j = "ahbgdc"
        o = False
        self.assertEqual(s.isSubsequence(i,j), o)
        self.assertEqual(s.isSubsequence_iter(i,j), o)

    def test_three(self):
        s = Solution()
        i = ""
        j = "ahbgdc"
        o = True
        self.assertEqual(s.isSubsequence(i,j), o)
        self.assertEqual(s.isSubsequence_iter(i,j), o)

    def test_four(self):
        s = Solution()
        i = "a"
        j = ""
        o = False
        self.assertEqual(s.isSubsequence(i,j), o)
        self.assertEqual(s.isSubsequence_iter(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)