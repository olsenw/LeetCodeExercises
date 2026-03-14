# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s that consists of lowercase English letters.

    Return the string obtained by removing all trailing vowels from s.

    The vowels consist of the characters 'a', 'e', 'i', 'o', and 'u'.
    '''
    def trimTrailingVowels(self, s: str) -> str:
        i = len(s)
        while i > 0:
            if s[i-1] in "aeiou":
                i -= 1
            else:
                break
        return s[:i]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "idea"
        o = "id"
        self.assertEqual(s.trimTrailingVowels(i), o)

    def test_two(self):
        s = Solution()
        i = "day"
        o = "day"
        self.assertEqual(s.trimTrailingVowels(i), o)

    def test_three(self):
        s = Solution()
        i = "aeiou"
        o = ""
        self.assertEqual(s.trimTrailingVowels(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)