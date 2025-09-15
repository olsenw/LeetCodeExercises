# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a malfunctioning keyboard where some letter keys do not work. All
    other keys on the keyboard work properly.

    Given a string text of words separated by a single space (no leading or
    trailing spaces) and a string brokenLetters of all distinct letter keys that
    are broken, return the number of words in text that can be fully typed using
    this keyboard.
    '''
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        answer = 0
        for w in text.split():
            if not any(c in brokenLetters for c in w):
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "hello world"
        j = "ad"
        o = 1
        self.assertEqual(s.canBeTypedWords(i,j), o)

    def test_two(self):
        s = Solution()
        i = "leet code"
        j = "lt"
        o = 1
        self.assertEqual(s.canBeTypedWords(i,j), o)

    def test_three(self):
        s = Solution()
        i = "leet code"
        j = "e"
        o = 0
        self.assertEqual(s.canBeTypedWords(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)