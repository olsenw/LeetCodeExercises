# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s and goal, return true if it is possible to swap two
    letters in s so the result is equal to goal, otherwise, return false.

    Swapping letters is defined as taking two indices i and j (0-indexed) such
    that i != j and swapping the characters at s[i] and s[j].
    '''
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        a,b = -1, -1
        # find first off character
        for i in range(len(s)):
            if s[i] != goal[i]:
                a = i
                break
        # find second off character
        for i in range(a+1, len(s)):
            if s[i] != goal[i]:
                b = i
                break
        # all characters match is there a duplicate letter
        if a == -1:
            return any(i >= 2 for i in Counter(s).values())
        # return if first off swapped with second off is valid
        if b == -1 or s[a] != goal[b] or s[b] != goal[a]:
            return False
        # bail on third off character
        for i in range(b+1, len(s)):
            if s[i] != goal[i]:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ab"
        j = "ba"
        o = True
        self.assertEqual(s.buddyStrings(i,j), o)

    def test_two(self):
        s = Solution()
        i = "ab"
        j = "ab"
        o = False
        self.assertEqual(s.buddyStrings(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aa"
        j = "aa"
        o = True
        self.assertEqual(s.buddyStrings(i,j), o)

    def test_four(self):
        s = Solution()
        i = "a"
        j = "a"
        o = False
        self.assertEqual(s.buddyStrings(i,j), o)

    def test_five(self):
        s = Solution()
        i = "ab"
        j = "babbb"
        o = False
        self.assertEqual(s.buddyStrings(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)