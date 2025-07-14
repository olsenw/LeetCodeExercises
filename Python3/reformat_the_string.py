# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import zip_longest
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an alphanumeric string s.

    Find a permutation of the string where no letter is followed by another
    letter and no digit is followed by another digit. That is, no tow adjacent
    characters have the same type.

    Return the reformated string or return an empty string if it is impossible
    to reformat the string.
    '''
    def reformat(self, s: str) -> str:
        c = [c for c in s if ord(c) > 96]
        n = [n for n in s if ord(n) < 96]
        if abs(len(c) - len(n)) > 1:
            return ""
        if len(n) < len(c):
            c,n = n,c
        return "".join(i + j for i,j in zip_longest(n,c,fillvalue=""))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "a0b1c2"
        o = "0a1b2c"
        self.assertEqual(s.reformat(i), o)

    def test_two(self):
        s = Solution()
        i = "leetcode"
        o = ""
        self.assertEqual(s.reformat(i), o)

    def test_three(self):
        s = Solution()
        i = "1229857369"
        o = ""
        self.assertEqual(s.reformat(i), o)

    def test_four(self):
        s = Solution()
        i = "covid2019"
        o = "c2o0v1i9d"
        self.assertEqual(s.reformat(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)