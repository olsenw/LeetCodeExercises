# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s1 and s2 of equal length. A string swap is an operation
    where two indices are chosen (not necessarily different) and swap the
    characters at these indices.

    Return true if it is possible to make both strings equal by performing at
    most one string swap on exactly one of the strings. Otherwise, return false.
    '''
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        d = sum(i != j for i,j in zip(s1, s2))
        s1,s2 = Counter(s1), Counter(s2)
        return d == 0 or (d == 2 and s1 == s2)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "bank", "kanb"
        o = True
        self.assertEqual(s.areAlmostEqual(*i), o)

    def test_two(self):
        s = Solution()
        i = "attack", "defend"
        o = False
        self.assertEqual(s.areAlmostEqual(*i), o)

    def test_three(self):
        s = Solution()
        i = "kelb", "kelb"
        o = True
        self.assertEqual(s.areAlmostEqual(*i), o)

    def test_four(self):
        s = Solution()
        i = "caa", "aaz"
        o = False
        self.assertEqual(s.areAlmostEqual(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)