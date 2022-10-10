# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a palindromic string of lowercase English letters palindrome, replace
    exactly one character with any lowercase English letter so that the
    resulting string is not a palindrome and that it is the lexicographically
    smallest one possible.
    
    Return the resulting string. If there is no way to replace a character to
    make it not a palindrome, return an empty string.
    
    A string is lexicographically smaller that a string b (of the same length)
    if in the first position where a and b differ, a has a character strictly
    smaller that the corresponding character in b. For example, "abcc" is
    lexicographically smaller than "abcd" because the first position they differ
    is at the forth character, and 'c' is smaller than 'd'.
    '''
    def breakPalindrome_works(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        # for i in range(len(palindrome) // 2):
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                if len(palindrome) % 2 == 0 or i != len(palindrome) // 2:
                    break
        if palindrome[i] != 'a':
            return palindrome[:i] + 'a' + palindrome[i+1:]
        else:
            return palindrome[:i] + 'b' + palindrome[i+1:]

    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome)):
            if palindrome[i] != 'a' and (len(palindrome) % 2 == 0 or i != len(palindrome) // 2):
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abccba"
        o = "aaccba"
        self.assertEqual(s.breakPalindrome(i), o)

    def test_two(self):
        s = Solution()
        i = "a"
        o = ""
        self.assertEqual(s.breakPalindrome(i), o)

    def test_three(self):
        s = Solution()
        i = "aa"
        o = "ab"
        self.assertEqual(s.breakPalindrome(i), o)

    def test_four(self):
        s = Solution()
        i = "aaa"
        o = "aab"
        self.assertEqual(s.breakPalindrome(i), o)

    def test_five(self):
        s = Solution()
        i = "aba"
        o = "abb"
        self.assertEqual(s.breakPalindrome(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)