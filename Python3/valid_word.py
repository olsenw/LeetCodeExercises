# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A word is considered valid if:
    * It contains a minimum of 3 characters.
    * It contains only digits (0-9), and English letters (uppercase and
      lowercase).
    * It includes at least one vowel.
    * It includes at least one consonant.

    Given a string word.

    Return true if word is valid, otherwise, return false.
    '''
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if any(w not in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" for w in word):
            return False
        if all(v not in word for v in "aeiouAEIOU"):
            return False
        if all(c not in word for c in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"):
            return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "234Adas"
        o = True
        self.assertEqual(s.isValid(i), o)

    def test_two(self):
        s = Solution()
        i = "b3"
        o = False
        self.assertEqual(s.isValid(i), o)

    def test_two(self):
        s = Solution()
        i = "a3$e"
        o = False
        self.assertEqual(s.isValid(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)