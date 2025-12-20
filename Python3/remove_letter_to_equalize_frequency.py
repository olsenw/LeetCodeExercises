# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed string word, consisting of lowercase English letters.
    Select one index and remove the letter at that index from word so that the
    frequency of every letter present in word is equal.

    Return true if it is possible to remove one letter so that the frequency of
    all letters in word are equal, and false otherwise.

    Note:
    * The frequency of a letter x is the number of times it occurs in the
      string.
    * It is required to remove exactly one letter.
    '''
    def equalFrequency_fails(self, word: str) -> bool:
        c = Counter(word)
        return all(v == 1 for v in c.values()) or abs(min(c.values()) - max(c.values())) == 1

    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        for i in list(c.keys()):
            c[i] -= 1
            if c[i] == 0:
                del c[i]
            if min(c.values()) == max(c.values()):
                return True
            c[i] += 1
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcc"
        o = True
        self.assertEqual(s.equalFrequency(i), o)

    def test_two(self):
        s = Solution()
        i = "aazz"
        o = False
        self.assertEqual(s.equalFrequency(i), o)

    def test_three(self):
        s = Solution()
        i = "bac"
        o = True
        self.assertEqual(s.equalFrequency(i), o)

    def test_four(self):
        s = Solution()
        i = "abccdd"
        o = False
        self.assertEqual(s.equalFrequency(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)