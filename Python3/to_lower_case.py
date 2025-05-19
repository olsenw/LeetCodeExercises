# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, return the string after replacing every uppercase letter
    with the same lowercase letter.
    '''
    def toLowerCase_builtin(self, s: str) -> str:
        return s.lower()

    def toLowerCase(self, s: str) -> str:
        return "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in s)
        return "".join(c if ord(c) >= ord('a') else chr(ord(c) + 32) for c in s)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "Hello"
        o = "hello"
        self.assertEqual(s.toLowerCase(i), o)

    def test_two(self):
        s = Solution()
        i = "here"
        o = "here"
        self.assertEqual(s.toLowerCase(i), o)

    def test_three(self):
        s = Solution()
        i = "LOVELY"
        o = "lovely"
        self.assertEqual(s.toLowerCase(i), o)

    def test_four(self):
        s = Solution()
        i = "al&phaBET"
        o = "al&phabet"
        self.assertEqual(s.toLowerCase(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)