# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed string word and a character ch, reverse the segment of
    word that starts at index 0 and ends at the index of the first occurrence of
    ch (inclusive). If the character ch does not exit in word, do nothing.

    Return the resulting string.
    '''
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch) + 1
        return word[:i][::-1] + word[i:]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcdefd"
        j = "d"
        o = "dcbaefd"
        self.assertEqual(s.reversePrefix(i,j), o)

    def test_two(self):
        s = Solution()
        i = "xyxzxe"
        j = "z"
        o = "zxyxxe"
        self.assertEqual(s.reversePrefix(i,j), o)

    def test_three(self):
        s = Solution()
        i = "abcd"
        j = "z"
        o = "abcd"
        self.assertEqual(s.reversePrefix(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)