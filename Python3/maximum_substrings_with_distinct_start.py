# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters.

    Return an integer denoting the maximum number of substrings that s can be
    split into such that each substring starts with a distinct character (ie no
    two substrings start with the same character).
    '''
    def maxDistinct(self, s: str) -> int:
        return len(set(s))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abab"
        o = 2
        self.assertEqual(s.maxDistinct(i), o)

    def test_two(self):
        s = Solution()
        i = "abcd"
        o = 4
        self.assertEqual(s.maxDistinct(i), o)

    def test_three(self):
        s = Solution()
        i = "aaaa"
        o = 1
        self.assertEqual(s.maxDistinct(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)