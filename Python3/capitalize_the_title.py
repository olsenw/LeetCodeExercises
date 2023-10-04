# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string title consisting of one or more words separated by a single
    space, where each word consists of English letters. Capitalize the string by
    changing the capitalization of each word such that:
    * If the length of the word is 1 or 2 letters, change all letters to
      lowercase.
    * Otherwise, change the first letter to uppercase and the remaining letters
      to lowercase.
    
    Return the capitalized title.
    '''
    def capitalizeTitle_passes(self, title: str) -> str:
        title = [t.lower() for t in title.split()]
        return ' '.join(t[0].upper() + t[1:] if len(t) > 2 else t for t in title)

    def capitalizeTitle(self, title: str) -> str:
        l = lambda x: x[0].upper() + x[1:] if len(x) > 2 else x
        return " ".join(l(t.lower()) for t in title.split())

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "capiTalIze tHe titLe"
        o = "Capitalize The Title"
        self.assertEqual(s.capitalizeTitle(i), o)

    def test_two(self):
        s = Solution()
        i = "First leTTeR of EACH Word"
        o = "First Letter of Each Word"
        self.assertEqual(s.capitalizeTitle(i), o)

    def test_three(self):
        s = Solution()
        i = "i lOve leetcode"
        o = "i Love Leetcode"
        self.assertEqual(s.capitalizeTitle(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)