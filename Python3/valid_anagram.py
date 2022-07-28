# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter

class Solution:
    '''
    Given two strings s and t, return true if t is an anagram of s, and
    false otherwise.

    An anagram is a word or phrase formed by rearranging the letters of
    a different word or phrase, typically using all the original letters
    exactly once.
    '''
    def isAnagram_counter(self, s: str, t: str) -> bool:
        count = Counter(s)
        valid = count.total()
        for c in t:
            if valid and count[c]:
                count[c] -= 1
                valid -= 1
            else:
                return False
        return not valid

    def isAnagram_dict(self, s: str, t: str) -> bool:
        count = {c:0 for c in "abcdefghijklmnopqrstuvwxyz"}
        valid = 0
        for c in s:
            count[c] += 1
            valid += 1
        for c in t:
            if valid and count[c]:
                count[c] -= 1
                valid -= 1
            else:
                return False
        return not valid

    def isAnagram_counter_compare(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    def isAnagram_sort(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "anagram"
        j = "nagaram"
        o = True
        self.assertEqual(s.isAnagram(i,j), o)

    def test_two(self):
        s = Solution()
        i = "rat"
        j = "car"
        o = False
        self.assertEqual(s.isAnagram(i,j), o)

    def test_three(self):
        s = Solution()
        i = "r"
        j = "t"
        o = False
        self.assertEqual(s.isAnagram(i,j), o)

    def test_four(self):
        s = Solution()
        i = "abc"
        j = "ab"
        o = False
        self.assertEqual(s.isAnagram(i,j), o)

    def test_five(self):
        s = Solution()
        i = "ab"
        j = "abc"
        o = False
        self.assertEqual(s.isAnagram(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)