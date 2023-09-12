# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings words, return the words that can be typed using
    letters of the alphabet on only one row of an American keyboard.
    '''
    def findWords(self, words: List[str]) -> List[str]:
        r1,r2,r3 = set("qwertyuiopQWERTYUIOP"), set("asdfghjklASDFGHJKL"), set("zxcvbnmZXCVBNM")
        return [w for w in words if r1.issuperset(w) or r2.issuperset(w) or r3.issuperset(w)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["Hello","Alaska","Dad","Peace"]
        o = ["Alaska","Dad"]
        self.assertEqual(s.findWords(i), o)

    def test_two(self):
        s = Solution()
        i = ["omk"]
        o = []
        self.assertEqual(s.findWords(i), o)

    def test_three(self):
        s = Solution()
        i = ["adsdf","sfd"]
        o = ["adsdf","sfd"]
        self.assertEqual(s.findWords(i), o)

    def test_four(self):
        s = Solution()
        i = ["a","b"]
        o = ["a","b"]
        self.assertEqual(s.findWords(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)