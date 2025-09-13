# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters ('a' to 'z').

    Complete the following tasks:
    * Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum
      frequency.
    * Find the consonant (all other letters excluding vowels) with the maximum
      frequency.

    Return the sum of the two frequencies.

    Note if multiple vowels or consonants have the same maximum frequency,
    choose any one of them. If there are no vowels or no consonants in the
    string, consider their frequency as 0.

    The frequency of a letter x is the number of times it occurs in the string.
    '''
    def maxFreqSum(self, s: str) -> int:
        c = Counter(s)
        a = max((c[i] for i in "aeiou"), default=0)
        b = max((c[i] for i in c if i not in "aeiou"), default=0)
        return a + b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "successes"
        o = 6
        self.assertEqual(s.maxFreqSum(i), o)

    def test_two(self):
        s = Solution()
        i = "aeiaeia"
        o = 3
        self.assertEqual(s.maxFreqSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)