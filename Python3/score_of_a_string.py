# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s. The score of a string is defined as the sum of the
    absolute difference between the ASCII values of adjacent characters.

    Return the score of s.
    '''
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "hello"
        o = 13
        self.assertEqual(s.scoreOfString(i), o)

    def test_two(self):
        s = Solution()
        i = "zaz"
        o = 50
        self.assertEqual(s.scoreOfString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)