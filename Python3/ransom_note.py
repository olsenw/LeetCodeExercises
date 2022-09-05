# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter

class Solution:
    '''
    Given two strings ransomNote and magazine, return true if ransomNote
    can be constructed by using the letters from magazine and false
    otherwise.

    Each letter in magazine can only be used once in ransomNote.
    '''
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n = Counter(ransomNote)
        m = Counter(magazine)
        '''
        for k in n:
            if n[k] > m[k]:
                return False
        return True
        '''
        return all(n[k] <= m[k] for k in n)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "a"
        j = "b"
        o = False
        self.assertEqual(s.canConstruct(i,j), o)

    def test_two(self):
        s = Solution()
        i = "aa"
        j = "ab"
        o = False
        self.assertEqual(s.canConstruct(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aa"
        j = "aab"
        o = True
        self.assertEqual(s.canConstruct(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)