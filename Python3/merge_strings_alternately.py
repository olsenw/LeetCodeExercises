# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import zip_longest
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings word1 and word2. Merge the strings by adding letters in
    alternating order, starting with word1. If a string is longer than the
    other, append the additional letters onto the end of the merged string.

    Return the merged string.
    '''
    def mergeAlternately_works(self, word1: str, word2: str) -> str:
        return "".join(a+b for a,b in zip_longest(word1,word2,fillvalue=""))

    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = ""
        i,j = 0,0
        while i < len(word1) and j < len(word2):
            a += word1[i] + word2[j]
            i += 1
            j += 1
        return a + word1[i:len(word1)] + word2[j:len(word2)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        j = "pqr"
        o = "apbqcr"
        self.assertEqual(s.mergeAlternately(i,j), o)

    def test_two(self):
        s = Solution()
        i = "ab"
        j = "pqrs"
        o = "apbqrs"
        self.assertEqual(s.mergeAlternately(i,j), o)

    def test_three(self):
        s = Solution()
        i = "abcd"
        j = "pq"
        o = "apbqcd"
        self.assertEqual(s.mergeAlternately(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)