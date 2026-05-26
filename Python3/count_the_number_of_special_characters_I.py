# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string word. A letter is called special if it appears both in
    lowercase and uppercase in word.

    Return the number of special letters in word.
    '''
    def numberOfSpecialChars(self, word: str) -> int:
        word = set(word)
        return sum(i in word and i.upper() in word for i in "abcdefghijklmnopqrstuvwxyz")

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aaAbcBC"
        o = 3
        self.assertEqual(s.numberOfSpecialChars(i), o)

    def test_two(self):
        s = Solution()
        i = "abc"
        o = 0
        self.assertEqual(s.numberOfSpecialChars(i), o)

    def test_three(self):
        s = Solution()
        i = "abBCab"
        o = 1
        self.assertEqual(s.numberOfSpecialChars(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)