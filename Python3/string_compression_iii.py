# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string word, compress it using the following algorithm:
    * Begin with an empty comp. While word is not empty, use the following
      operation:
      * Remove a maximum length prefix of word made of a single character c
        repeating at most 9 times.
    * Append the length of the prefix followed by c to comp.

    Return the string comp.
    '''
    def compressedString(self, word: str) -> str:
        comp = ""
        a,b = word[0], 1
        for w in word[1:]:
            if w == a and b < 9:
                b += 1
            else:
                comp += f'{b}{a}'
                a = w
                b = 1
        comp += f'{b}{a}'
        return comp

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcde"
        o = "1a1b1c1d1e"
        self.assertEqual(s.compressedString(i), o)

    def test_two(self):
        s = Solution()
        i = "aaaaaaaaaaaaaabb"
        o = "9a5a2b"
        self.assertEqual(s.compressedString(i), o)

    def test_three(self):
        s = Solution()
        i = "aaaabaaaabbbbbbbbbbbbbvccdddcc"
        o = "4a1b4a9b4b1v2c3d2c"
        self.assertEqual(s.compressedString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)