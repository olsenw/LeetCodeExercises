# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to
    get t.

    All occurrences of a character must be replaced with another character while
    preserving the order of characters. No two characters may map to the same
    character, but a character may map to itself.
    '''
    # does not maintain order
    def isIsomorphic_incorrect(self, s: str, t: str) -> bool:
        cs = [0] * 26
        ct = [0] * 26
        for i in range(len(s)):
            cs[ord(s[i]) - ord('a')] += 1
            ct[ord(t[i]) - ord('a')] += 1
        return sorted(cs) == sorted(ct)

    def isIsomorphic(self, s: str, t: str) -> bool:
        m = dict()
        u = set()
        for i in range(len(s)):
            if s[i] in m:
                if m[s[i]] != t[i]:
                    return False
            else:
                if t[i] in u:
                    return False
                m[s[i]] = t[i]
                u.add(t[i])
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "egg"
        j = "add"
        o = True
        self.assertEqual(s.isIsomorphic(i,j), o)

    def test_two(self):
        s = Solution()
        i = "foo"
        j = "bar"
        o = False
        self.assertEqual(s.isIsomorphic(i,j), o)

    def test_three(self):
        s = Solution()
        i = "paper"
        j = "title"
        o = True
        self.assertEqual(s.isIsomorphic(i,j), o)

    def test_four(self):
        s = Solution()
        i = "bbbaaaba"
        j = "aaabbbba"
        o = False
        self.assertEqual(s.isIsomorphic(i,j), o)

    def test_five(self):
        s = Solution()
        i = "badc"
        j = "baba"
        o = False
        self.assertEqual(s.isIsomorphic(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)