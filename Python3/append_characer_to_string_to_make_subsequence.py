# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s and t consisting of only lowercase English letters.

    Return the minimum number of characters that need to be appended to the end
    of s so that t becomes a subsequence of s.

    A subsequence is a string that can be derived from another string by
    deleting some or no characters without changing the order of the remaining
    characters.
    '''
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for i in range(len(s)):
            if s[i] == t[j]:
                j += 1
            if j == len(t):
                break
        return len(t) - j

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "coaching"
        j = "coding"
        o = 4
        self.assertEqual(s.appendCharacters(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abcde"
        j = "a"
        o = 0
        self.assertEqual(s.appendCharacters(i,j), o)

    def test_three(self):
        s = Solution()
        i = "z"
        j = "abcde"
        o = 5
        self.assertEqual(s.appendCharacters(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)