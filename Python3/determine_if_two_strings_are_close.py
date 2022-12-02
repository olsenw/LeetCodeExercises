# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Two strings are considered close if string one can be obtained from string
    two using the following operations:
    * Swap any two existing characters.
    * Transform every occurrence of one existing character into another existing
      character, and do the same with the other character.
    
    The operations may be applied to the strings as many times as necessary.

    Given two strings word1 and word2 return true if word1 and word2 are close,
    and false otherwise.
    '''
    def closeStrings_incorrect_sort(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        a,b = '1', '1'
        for i,j in zip(sorted(word1), sorted(word2)):
            if (i,j) == (a,b):
                continue
            if i == a or j == b:
                return False
            else:
                a,b = i,j
        return True

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        a = [0] * 26
        b = [0] * 26
        for i in range(len(word1)):
            a[ord(word1[i]) - ord('a')] += 1
            b[ord(word2[i]) - ord('a')] += 1
        for i,j in zip(a,b):
            if i != j and (i == 0 or j == 0):
                return False
        for i,j in zip(sorted(a), sorted(b)):
            if i != j:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        j = "bca"
        o = True
        self.assertEqual(s.closeStrings(i,j), o)

    def test_two(self):
        s = Solution()
        i = "a"
        j = "aa"
        o = False
        self.assertEqual(s.closeStrings(i,j), o)

    def test_three(self):
        s = Solution()
        i = "cabbba"
        j = "abbccc"
        o = True
        self.assertEqual(s.closeStrings(i,j), o)

    def test_four(self):
        s = Solution()
        i = "uau"
        j = "ssx"
        o = False
        self.assertEqual(s.closeStrings(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)