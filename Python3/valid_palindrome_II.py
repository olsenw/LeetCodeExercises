# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s, return true if the string can be a palindrome
    after deleting at most one character from it.
    '''
    def validPalindrome(self, s: str) -> bool:
        # check if palindrome without removing letter
        def check(s):
            i = 0
            j = len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                # check if removing one letter works
                # have to check both can't decide early
                return check(s[i+1:j+1]) or check(s[i:j])
            i += 1
            j -= 1
        return True

    # string comparison idea came from looking at other solutions
    def validPalindrome_faster(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                a = s[:i] + s[i+1:]
                b = s[:j] + s[j+1:]
                return a == a[::-1] or b == b[::-1]
            i += 1
            j -= 1
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aba"
        o = True
        self.assertEqual(s.validPalindrome(i), o)
        self.assertEqual(s.validPalindrome_faster(i), o)

    def test_two(self):
        s = Solution()
        i = "abca"
        o = True
        self.assertEqual(s.validPalindrome(i), o)
        self.assertEqual(s.validPalindrome_faster(i), o)

    def test_three(self):
        s = Solution()
        i = "abc"
        o = False
        self.assertEqual(s.validPalindrome(i), o)
        self.assertEqual(s.validPalindrome_faster(i), o)

    def test_four(self):
        s = Solution()
        i = "adbccbad"
        o = False
        self.assertEqual(s.validPalindrome(i), o)
        self.assertEqual(s.validPalindrome_faster(i), o)

    def test_five(self):
        s = Solution()
        i = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
        o = True
        self.assertEqual(s.validPalindrome(i), o)
        self.assertEqual(s.validPalindrome_faster(i), o)

    def test_six(self):
        s = Solution()
        i = "ebcbbececabbacecbbcbe"
        o = True
        self.assertEqual(s.validPalindrome(i), o)
        self.assertEqual(s.validPalindrome_faster(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)