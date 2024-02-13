# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of strings words, return the first palindromic string in the
    array. If there is no such string, return an empty string "".

    A string is palindromic if it reads the same forward and backward.
    '''
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["abc","car","ada","racecar","cool"]
        o = "ada"
        self.assertEqual(s.firstPalindrome(i), o)

    def test_two(self):
        s = Solution()
        i = ["notapalindrome","racecar"]
        o = "racecar"
        self.assertEqual(s.firstPalindrome(i), o)

    def test_three(self):
        s = Solution()
        i = ["def","ghi"]
        o = ""
        self.assertEqual(s.firstPalindrome(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)