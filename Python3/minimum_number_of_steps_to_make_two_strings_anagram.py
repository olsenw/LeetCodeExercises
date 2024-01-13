# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings of the same length s and t. In one step it is possible to
    choose any character of t and replace it with another character.

    Return the minimum number of steps to make t an anagram of s.

    An Anagram of a string is a string that contains the same character with a
    different (or the same) ordering.
    '''
    def minSteps(self, s: str, t: str) -> int:
        s = Counter(s)
        t = Counter(t)
        d = {c:0 for c in 'abcdefghijklmnopqrstuvwxyz'}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            d[c] += s[c] - t[c]
        return sum(abs(d[c]) for c in d) // 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "bab"
        j = "aba"
        o = 1
        self.assertEqual(s.minSteps(i,j), o)

    def test_two(self):
        s = Solution()
        i = "anagram"
        j = "mangaar"
        o = 0
        self.assertEqual(s.minSteps(i,j), o)

    def test_three(self):
        s = Solution()
        i = "leetcode"
        j = "practice"
        o = 5
        self.assertEqual(s.minSteps(i,j), o)

    def test_four(self):
        s = Solution()
        i = "aaaaaaab"
        j = "bbcccaaa"
        o = 4
        self.assertEqual(s.minSteps(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)