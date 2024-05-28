# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s and t of the same length and an integer maxCost.

    Change s to t. Changing the ith character of s to ith character of t costs
    abs(s[i] - t[i]) (ie the absolute difference between the ASCII values of the
    characters).

    Return the maximum length of a substring of s that can be changed to be the
    same as the corresponding substring of t with a cost less than or equal to
    maxCost. If there is no substring from s that can be changed to its
    corresponding substring from t, return 0.
    '''
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        answer = 0
        curr = 0
        i,j = 0,0
        while j < len(s):
            while j < len(s) and curr <= maxCost:
                curr += abs(ord(s[j]) - ord(t[j]))
                j += 1
                if curr <= maxCost:
                    answer = max(answer, j - i)
            while i < j and curr > maxCost:
                curr -= abs(ord(s[i]) - ord(t[i]))
                i += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcd"
        j = "bcdf"
        k = 3
        o = 3
        self.assertEqual(s.equalSubstring(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = "abcd"
        j = "cdef"
        k = 3
        o = 1
        self.assertEqual(s.equalSubstring(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = "abcd"
        j = "acde"
        k = 0
        o = 1
        self.assertEqual(s.equalSubstring(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = "a"
        j = "a"
        k = 0
        o = 1
        self.assertEqual(s.equalSubstring(i,j,k), o)

    def test_five(self):
        s = Solution()
        i = "b"
        j = "a"
        k = 2
        o = 1
        self.assertEqual(s.equalSubstring(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)