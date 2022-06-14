# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from functools import cache

class Solution:
    '''
    Given two strings word1 and word2, return the minimum number of
    steps required to make word1 and word2 the same.

    In one step, it is possible to delete exactly one character in
    either string.
    '''
    # time limit exceeded (20/1306)
    def minDistance_time_exceeded(self, word1: str, word2: str) -> int:
        @cache 
        def s(s1, s2):
            # base case they are both equal
            if s1 == s2:
                return 0
            if len(s1) == 0:
                return len(s2)
            if len(s2) == 0:
                return len(s1)
            a = 1001
            for i in range(len(s1)):
                a = min(a, s(s1[:i] + s1[i+1:], s2))
            b = 1001
            for i in range(len(s2)):
                b = min(b, s(s1, s2[:i] + s2[i+1:]))
            return min(a+1,b+1)
        return s(word1, word2)

    def minDistance_time_exceeded_2(self, word1: str, word2: str) -> int:
        @cache 
        def s(s1, s2):
            # base case they are both equal
            if s1 == s2:
                return 0
            if len(s1) == 0:
                return len(s2)
            if len(s2) == 0:
                return len(s1)
            if len(s2) > len(s1):
                s1, s2 = s2, s1
            a = 1001
            for i in range(len(s1)):
                a = min(a, s(s1[:i] + s1[i+1:], s2))
            return a + 1
        return s(word1, word2)

    # passes... but is slow
    def minDistance_cache_strings(self, word1: str, word2: str) -> int:
        @cache 
        def s(s1, s2):
            # base case they are both equal
            if s1 == s2:
                return 0
            # base case empty string
            if len(s1) == 0 or len(s2) == 0:
                return max(len(s1), len(s2))
            # find index of 1st mismatch
            for i in range(min(len(s1), len(s2))):
                if s1[i] != s2[i]:
                    break
            else:
                i += 1
            a = s(s1[i+1:], s2[i:])
            b = s(s1[i:], s2[i+1:])
            return min(a,b) + 1
        return s(word1, word2)

    # similar to above but uses indexes
    def minDistance(self, word1: str, word2: str) -> int:
        @cache 
        def s(i, j):
            # find first mismatched letter
            while i < len(word1) and j < len(word2):
                if word1[i] != word2[j]:
                    break
                i += 1
                j += 1
            # if one string empty return remaining characters of other
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            # get answer deleting mismatched character from each string
            a = s(i + 1, j) + 1
            b = s(i, j + 1) + 1
            return min(a,b)
        return s(0, 0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "sea"
        j = "eat"
        o = 2
        self.assertEqual(s.minDistance(i,j), o)

    def test_two(self):
        s = Solution()
        i = "leetcode"
        j = "etco"
        o = 4
        self.assertEqual(s.minDistance(i,j), o)

    def test_three(self):
        s = Solution()
        i = "prosperity"
        j = "properties"
        o = 6
        self.assertEqual(s.minDistance(i,j), o)

    def test_four(self):
        s = Solution()
        i = "abc"
        j = "abc"
        o = 0
        self.assertEqual(s.minDistance(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)