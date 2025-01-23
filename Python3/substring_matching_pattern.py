# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import re
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s and a pattern string p, where p contains exactly one '*'
    character.

    The '*' in p can be replaced with any sequence of zero or more characters.

    Return true if p can be made a substring of s, and false otherwise.
    '''
    def hasMatch_regex(self, s: str, p: str) -> bool:
        return True if re.search(p.replace("*",".*"),s) else False

    def hasMatch(self, s: str, p: str) -> bool:
        if p == "*":
            return True
        a,b = p.split('*')
        try:
            f = s.index(a)
            e = s.index(b, f + len(a))
        except ValueError as e:
            return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "leetcode", "ee*e"
        o = True
        self.assertEqual(s.hasMatch(*i), o)

    def test_two(self):
        s = Solution()
        i = "cat", "c*v"
        o = False
        self.assertEqual(s.hasMatch(*i), o)

    def test_three(self):
        s = Solution()
        i = "luck", "u*"
        o = True
        self.assertEqual(s.hasMatch(*i), o)

    def test_four(self):
        s = Solution()
        i = "l", "*"
        o = True
        self.assertEqual(s.hasMatch(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)