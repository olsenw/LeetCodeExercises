# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer x, return true if x is a palindrome, and false otherwise.
    '''
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        i,j = 0, len(n) - 1
        while i <= j:
            if n[i] != n[j]:
                return False
            i += 1
            j -= 1
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 121
        o = True
        self.assertEqual(s.isPalindrome(i), o)

    def test_two(self):
        s = Solution()
        i = -121
        o = False
        self.assertEqual(s.isPalindrome(i), o)

    def test_two(self):
        s = Solution()
        i = 10
        o = False
        self.assertEqual(s.isPalindrome(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)