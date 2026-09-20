# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters.

    Construct a binary string by replacing each character in s with the 8-bit
    binary representation of its ASCII value, including leading zeros, while
    preserving the original order of the characters.

    Return true if the resulting binary string is a palindrome. Otherwise,
    return false.
    '''
    def isPalindromic_brute(self, s: str) -> bool:
        s = ''.join(f"{ord(c):08b}" for c in s)
        return s == s[::-1]

    # note only f -> f, n -> v and v -> n are palindromic
    def isPalindromic(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2 + 1):
            if s[i] == 'f' and s[n-1-i] == 'f':
                continue
            if s[i] == 'n' and s[n-1-i] == 'v':
                continue
            if s[i] == 'v' and s[n-1-i] == 'n':
                continue
            return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ff"
        o = True
        self.assertEqual(s.isPalindromic(i), o)

    def test_two(self):
        s = Solution()
        i = "leet"
        o = False
        self.assertEqual(s.isPalindromic(i), o)

    def test_three(self):
        s = Solution()
        i = "ffnnfvvff"
        o = True
        self.assertEqual(s.isPalindromic(i), o)

    def test_four(self):
        s = Solution()
        i = "ffnnnvvff"
        o = False
        self.assertEqual(s.isPalindromic(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)