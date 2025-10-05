# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings: s1 and s2 with the same size, check if some permutation
    of string s1 can break some permutation of string s2 or vice-versa.

    A string x can break string y (both of size n) if x[i] >= y[i] (in
    alphabetical order) for all i between 0 and n-1.
    '''
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        return all(i >= j for i,j in zip(s1,s2)) or all(i >= j for i,j in zip(s2,s1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        j = "xya"
        o = True
        self.assertEqual(s.checkIfCanBreak(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abe"
        j = "acd"
        o = False
        self.assertEqual(s.checkIfCanBreak(i,j), o)

    def test_three(self):
        s = Solution()
        i = "leetcodee"
        j = "interview"
        o = True
        self.assertEqual(s.checkIfCanBreak(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)