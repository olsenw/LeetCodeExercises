# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string text of words that are placed among some number of spaces.
    Each word consists of one or more lowercase English letters and are
    separated by at least one space. It's guaranteed that text contains at least
    one word.

    Rearrange the spaces so that there is an equal number between every pair of
    adjacent words and that number is maximized. If it is impossible to equally
    redistribute all the spaces, place the extra spaces at the end.

    Return the string after rearranging the spaces
    '''
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + (" " * spaces)
        a,b = divmod(spaces, len(words) - 1)
        return (" " * a).join(words) + (" " * b)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "  this   is  a sentence "
        o = "this   is   a   sentence"
        self.assertEqual(s.reorderSpaces(i), o)

    def test_two(self):
        s = Solution()
        i = " practice   makes   perfect"
        o = "practice   makes   perfect "
        self.assertEqual(s.reorderSpaces(i), o)

    def test_three(self):
        s = Solution()
        i = "a"
        o = "a"
        self.assertEqual(s.reorderSpaces(i), o)

    def test_four(self):
        s = Solution()
        i = "  a  "
        o = "a    "
        self.assertEqual(s.reorderSpaces(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)