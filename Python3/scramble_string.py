# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    It is possible to scramble a string s into string t using the following
    algorithm:
    
    If the length of the string is 1, stop.

    If the length of the string is > 1, do the following:
    * Split the string into two non-empty substrings at a random index, ie, if
      the string is s, divide it to x and y where s = x + y.
    * Randomly decide to swap the two substrings or to keep them in the same
      order. ie, after this step, s may become s = x + y or s = y + x.
    * Apply step 1 recursively on each of the two substrings x and y.

    Given two strings s1 and s2 of the same length, return true if s2 is a
    scrambled string of s1, otherwise, return false.
    '''
    # based on solution by LeetCode
    # https://leetcode.com/problems/scramble-string/editorial/
    # don't really get
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # 3d dimension dynamic program
        # n+1 because length cannot be zero
        dp = [[[False for j in range(n)] for i in range(n)] for _ in range(n+1)]
        # prepopulated trivial cases (length one)
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]
        # case of length 1 up to n
        for length in range(2, n+1):
            # the split point
            for i in range(n + 1 - length):
                for j in range(n + 1 - length):
                    # the subproblem comprising
                    for newLength in range(1, length):
                        dp1 = dp[newLength][i]
                        dp2 = dp[length - newLength][i + newLength]
                        dp[length][i][j] |= dp1[j] and dp2[j + newLength]
                        dp[length][i][j] |= dp1[j + length - newLength] and dp2[j]
        return dp[n][0][0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "great"
        j = "rgeat"
        o = True
        self.assertEqual(s.isScramble(i,j), o)

    def test_two(self):
        s = Solution()
        i = "abcde"
        j = "caebd"
        o = False
        self.assertEqual(s.isScramble(i,j), o)

    def test_three(self):
        s = Solution()
        i = "a"
        j = "a"
        o = True
        self.assertEqual(s.isScramble(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)