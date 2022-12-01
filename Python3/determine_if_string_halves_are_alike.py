# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s of even length. Split this string into two halves of equal
    lengths, and let a be the first half and b be the second half.
    
    Two strings are alike if they have the same number of vowels ('a', 'e', 'i',
    'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that the s contains uppercase and
    lowercase letters.
    
    Return true if a and b are alike. Otherwise, return false.'''
    # solves a different problem... need to read description better
    def halvesAreAlike_incorrect(self, s: str) -> bool:
        c = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
        n = len(s)
        for i in range(n//2):
            if s[i] in c:
                c[s[i]] += 1
        for i in range(n//2,n):
            if s[i] in c:
                c[s[i]] -= 1
        return all(c[i] == 0 for i in c)

    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        valid = 0
        for c in s[:n//2]:
            if c in "aeiouAEIOU":
                valid += 1
        for c in s[n//2:]:
            if c in "aeiouAEIOU":
                valid -= 1
        return valid == 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "book"
        o = True
        self.assertEqual(s.halvesAreAlike(i), o)

    def test_two(self):
        s = Solution()
        i = "textbook"
        o = False
        self.assertEqual(s.halvesAreAlike(i), o)

    def test_three(self):
        s = Solution()
        i = "AbCdEfGh"
        o = True
        self.assertEqual(s.halvesAreAlike(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)