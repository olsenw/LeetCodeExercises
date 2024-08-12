# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, return a string with n characters such that each
    character in such string occurs an odd number of times.

    The returned string must contain only lowercase English letters. If there
    are multiples valid strings, return any of them.
    '''
    def generateTheString(self, n: int) -> str:
        if n % 2:
            return "a" * n
        return "a" * (n-1) + "b"

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        o = "aaab"
        self.assertEqual(s.generateTheString(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = "ab"
        self.assertEqual(s.generateTheString(i), o)

    def test_three(self):
        s = Solution()
        i = 7
        o = "aaaaaaa"
        self.assertEqual(s.generateTheString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)