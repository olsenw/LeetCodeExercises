# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two strings needle and haystack, return the index of the first
    occurrence of needle in haystack, or -1 if needle is not part of haystack.
    '''
    # incorrect
    # if passes over start doing previous check unable to recover
    def strStr_wrong(self, haystack: str, needle: str) -> int:
        possible = 0
        check = 0
        for i in range(len(haystack)):
            if check == len(needle):
                return possible
            elif haystack[i] == needle[check]:
                check += 1
            else:
                possible = i + 1
                check = 0
        return possible if check == len(needle) else -1

    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if len(haystack) - i < len(needle):
                break
            if haystack[i] != needle[0]:
                continue
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
            else:
                return i
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "sadbutsad"
        j = "sad"
        o = 0
        self.assertEqual(s.strStr(i,j), o)

    def test_two(self):
        s = Solution()
        i = "leetcode"
        j = "leeto"
        o = -1
        self.assertEqual(s.strStr(i,j), o)

    def test_three(self):
        s = Solution()
        i = "a"
        j = "a"
        o = 0
        self.assertEqual(s.strStr(i,j), o)

    def test_four(self):
        s = Solution()
        i = "mississippi"
        j = "issip"
        o = 4
        self.assertEqual(s.strStr(i,j), o)

    def test_five(self):
        s = Solution()
        i = "i" * 10**4
        j = "i" * 10**3 + "a"
        o = -1
        self.assertEqual(s.strStr(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)