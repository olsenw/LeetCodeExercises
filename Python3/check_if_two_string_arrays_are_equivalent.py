# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import chain, zip_longest
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two string arrays word1 and word2, return true if the two arrays
    represent the same string, and false otherwise.
    
    A string is represented by an array if the array elements concatenated in
    order forms the string.
    '''
    def arrayStringsAreEqual_join(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return all(a == b for a,b in zip_longest(chain.from_iterable(word1), chain.from_iterable(word2), fillvalue=' '))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["ab", "c"]
        j = ["a", "bc"]
        o = True
        self.assertEqual(s.arrayStringsAreEqual(i,j), o)

    def test_two(self):
        s = Solution()
        i = ["a", "cb"]
        j = ["ab", "c"]
        o = False
        self.assertEqual(s.arrayStringsAreEqual(i,j), o)

    def test_three(self):
        s = Solution()
        i = ["abc", "d", "defg"]
        j = ["abcddefg"]
        o = True
        self.assertEqual(s.arrayStringsAreEqual(i,j), o)

    def test_four(self):
        s = Solution()
        i = ["abc", "d", "defg"]
        j = ["ab"]
        o = False
        self.assertEqual(s.arrayStringsAreEqual(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)