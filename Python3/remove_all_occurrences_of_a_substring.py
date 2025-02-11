# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s and part, perform the following operation on s until all
    occurrences of the substring part are removed:
    * Find the leftmost occurrence of the substring part and remove it from s.

    Return s after removing all occurrences of part.

    A substring is a contiguous sequence of characters in a string.
    '''
    def removeOccurrences(self, s: str, part: str) -> str:
        while len(s) >= len(part):
            i = s.find(part)
            if i == -1:
                break
            s = s[:i] + s[i+len(part):]
        return s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "daabcbaabcbc"
        j = "abc"
        o = "dab"
        self.assertEqual(s.removeOccurrences(i,j), o)

    def test_two(self):
        s = Solution()
        i = "axxxxyyyyb"
        j = "xy"
        o = "ab"
        self.assertEqual(s.removeOccurrences(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)