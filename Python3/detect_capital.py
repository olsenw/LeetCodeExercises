# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Define the usage of capitals in a word to be right when one of the
    following three cases holds:
    1) All letters in the word are capitals, like "USA".
    2) All letters in the word are lower case, like "leetcode".
    3) Only the first letter in the word is capital, like "Google".

    Given a string word, return true if the usage of capitals in the 
    word is correct.
    '''
    def detectCapitalUse(self, word: str) -> bool:
        for s in word:
            if not s.isupper(): break
        else:
            return True
        for s in word[1:]:
            if s.isupper(): break
        else:
            return True
        return False

    def detectCapitalUse_alt(self, word: str) -> bool:
        upper = False
        lower = False
        for s in word[1:]:
            if s.isupper():
                upper = True
            else:
                lower = True
            if upper and lower: break
        else:
            if len(word) == 1: return True
            return lower or (word[0].isupper() and upper)
        return False

    def detectCapitalUse_regex(self, word: str) -> bool:
        import re
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word) != None

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "USA"
        o = True
        self.assertEqual(s.detectCapitalUse(i), o)
        self.assertEqual(s.detectCapitalUse_alt(i), o)
        self.assertEqual(s.detectCapitalUse_regex(i), o)

    def test_two(self):
        s = Solution()
        i = "leetcode"
        o = True
        self.assertEqual(s.detectCapitalUse(i), o)
        self.assertEqual(s.detectCapitalUse_alt(i), o)
        self.assertEqual(s.detectCapitalUse_regex(i), o)

    def test_three(self):
        s = Solution()
        i = "Google"
        o = True
        self.assertEqual(s.detectCapitalUse(i), o)
        self.assertEqual(s.detectCapitalUse_alt(i), o)
        self.assertEqual(s.detectCapitalUse_regex(i), o)

    def test_four(self):
        s = Solution()
        i = "FlaG"
        o = False
        self.assertEqual(s.detectCapitalUse(i), o)
        self.assertEqual(s.detectCapitalUse_alt(i), o)
        self.assertEqual(s.detectCapitalUse_regex(i), o)

    def test_five(self):
        s = Solution()
        i = "aBAG"
        o = False
        self.assertEqual(s.detectCapitalUse(i), o)
        self.assertEqual(s.detectCapitalUse_alt(i), o)
        self.assertEqual(s.detectCapitalUse_regex(i), o)

    def test_six(self):
        s = Solution()
        i = "x"
        o = True
        self.assertEqual(s.detectCapitalUse(i), o)
        self.assertEqual(s.detectCapitalUse_alt(i), o)
        self.assertEqual(s.detectCapitalUse_regex(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)