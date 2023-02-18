# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import string
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A phrase is a palindrome if, after converting all uppercase letters into
    lowercase letters and removing all non-alphanumeric characters, it reads the
    same forward and backward. Alphanumeric characters include letters and
    numbers.

    Given a string s, return true if is is a palindrome, or false otherwise.
    '''
    def isPalindrome(self, s: str) -> bool:
        valid = string.ascii_lowercase + string.digits
        s = ''.join(i for i in s.lower() if i in valid)
        return all(i==j for i,j in zip(s, s[::-1]))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "A man, a plan, a canal: Panama"
        o = True
        self.assertEqual(s.isPalindrome(i), o)

    def test_two(self):
        s = Solution()
        i = "race a car"
        o = False
        self.assertEqual(s.isPalindrome(i), o)

    def test_three(self):
        s = Solution()
        i = " "
        o = True
        self.assertEqual(s.isPalindrome(i), o)

    def test_four(self):
        s = Solution()
        i = "12321"
        o = True
        self.assertEqual(s.isPalindrome(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)