# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, find any substring of length 2 which is also present in
    the reverse of s.

    Return true if such a substring exists, and false otherwise.
    '''
    def isSubstringPresent(self, s: str) -> bool:
        substrings = {s[i:i+2] for i in range(len(s)-1)}
        s = s[::-1]
        return any(s[i:i+2] in substrings for i in range(len(s)-1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "leetcode"
        o = True
        self.assertEqual(s.isSubstringPresent(i), o)

    def test_two(self):
        s = Solution()
        i = "abcba"
        o = True
        self.assertEqual(s.isSubstringPresent(i), o)

    def test_three(self):
        s = Solution()
        i = "abcd"
        o = False
        self.assertEqual(s.isSubstringPresent(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)