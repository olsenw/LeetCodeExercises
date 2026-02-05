# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters, spaces, and
    digits.

    Let v be the number of vowels in s and c be the number of consonants in s.

    A vowel is one of the letters 'a', 'e', 'i', 'o', or 'u', while any other
    letter in the English alphabet is considered a consonant.

    The score of the string s is defined as follows:
    * if c > 0, the score = floor(v / c) where floor denotes rounding down to
      the nearest integer.
    * Otherwise, the score = 0.

    Return an integer denoting the score of the string.
    '''
    def vowelConsonantScore(self, s: str) -> int:
        v = 0
        c = 0
        for i in s:
            if i.isalpha():
                if i in "aeiou":
                    v += 1
                else:
                    c += 1
        return v // c if c > 0 else 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "cooear"
        o = 2
        self.assertEqual(s.vowelConsonantScore(i), o)

    def test_two(self):
        s = Solution()
        i = "axeyizou"
        o = 1
        self.assertEqual(s.vowelConsonantScore(i), o)

    def test_three(self):
        s = Solution()
        i = "au 123"
        o = 0
        self.assertEqual(s.vowelConsonantScore(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)