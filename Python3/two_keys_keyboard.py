# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is only one character 'A' on the screen of a notepad. The following
    two operations can be performed multiple times:
    * Copy All: copy all the characters present on the screen.
    * Paste: paste the characters which were last copied.

    Given an integer n, return the minimum number of operations to get the
    character 'A' exactly n times on the screen.
    '''
    # wrong
    # trial division https://en.wikipedia.org/wiki/Trial_division
    def minSteps_wrong(self, n: int) -> int:
        @cache
        def dp(i):
            if i == 1:
                return 0
            answer = 1000
            # first possible factor
            factor = 2
            # keep going while factor is less than the square root of i
            while factor * factor <= i:
                # factor found
                if i % factor == 0:
                    answer = min(answer, dp(factor) + (i // factor))
                    i //= factor
                # not a factor
                else:
                    factor += 1
            if i != 1:
                answer = min(answer, dp(factor) + (i // factor))
            return answer
        return dp(n)

    # based on Leetcode editorial
    # https://leetcode.com/problems/2-keys-keyboard/editorial/?envType=daily-question&envId=2024-08-19
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        def dp(i,j):
            if i == n:
                return 0
            if i > n:
                return 1000
            # try copy
            copy = 2 + dp(i * 2, i)
            # try paste
            paste = 1 + dp(i + j, j)
            return min(copy, paste)
        return dp(1,n)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 0
        self.assertEqual(s.minSteps(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 2
        self.assertEqual(s.minSteps(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = 3
        self.assertEqual(s.minSteps(i), o)

    def test_four(self):
        s = Solution()
        i = 4
        o = 4
        self.assertEqual(s.minSteps(i), o)

    def test_five(self):
        s = Solution()
        i = 5
        o = 5
        self.assertEqual(s.minSteps(i), o)

    def test_six(self):
        s = Solution()
        i = 6
        o = 5
        self.assertEqual(s.minSteps(i), o)

    def test_seven(self):
        s = Solution()
        i = 7
        o = 7
        self.assertEqual(s.minSteps(i), o)

    def test_eight(self):
        s = Solution()
        i = 8
        o = 6
        self.assertEqual(s.minSteps(i), o)

    def test_nine(self):
        s = Solution()
        i = 9
        o = 6
        self.assertEqual(s.minSteps(i), o)

    def test_ten(self):
        s = Solution()
        i = 10
        o = 7
        self.assertEqual(s.minSteps(i), o)

    def test_twentyfour(self):
        s = Solution()
        i = 24
        o = 9
        self.assertEqual(s.minSteps(i), o)

    # def test_thousand(self):
    #     s = Solution()
    #     i = 1000
    #     o = 21
    #     self.assertEqual(s.minSteps(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)