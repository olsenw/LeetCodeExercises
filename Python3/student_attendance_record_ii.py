# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An attendance record for a student can be represented as a string where each
    character signifies whether the student was absent, late, or present on that
    day. The record only contains the following three characters:
    * 'A': Absent
    * 'L': Late
    * 'P': Present

    Any student is eligible for an attendance award if they meet both of the
    following criteria:
    * The student was absent ('A") for strictly fewer than 2 days total.
    * The student was never late ('L') for 3 or more consecutive days.

    Given an integer n, return the number of possible attendance records of
    length n that make a student eligible for an attendance award. The answer
    may be very large, so return it modulo 10^9 + 7.
    '''
    # This will generate a correct answer, but does not pass LeetCode
    def checkRecord_memory_limit_exceeded(self, n: int) -> int:
        m = (10**9 + 7)
        @cache
        def dp(i, a, l):
            if a == 2 or l == 3:
                return 0
            if i == 0:
                return 1
            return ((dp(i - 1, a, 0) % m)
                     + (dp(i - 1, a + 1, 0) % m)
                     + (dp(i - 1, a, l + 1) % m)
                    ) % m
        for i in range(n):
            dp(i, 0, 0)
        return dp(n, 0, 0)

    # corrected dp solution
    # fixes the memory issue by changing the scope of dp function
    @cache
    def dp(i, a, l):
        m = (10**9 + 7)
        if i == 0:
            return 1
        c = Solution.dp(i - 1, a, 0) % m
        if a < 1:
            c += Solution.dp(i - 1, a + 1, 0) % m
        if l < 2:
            c += Solution.dp(i - 1, a, l + 1) % m
        return c % m
    def checkRecord(self, n: int) -> int:
        return Solution.dp(n, 0, 0)

    # note does not pass without the modulo addition
    # python super large numbers are slow
    def checkRecord_iterative(self, n: int) -> int:
        m = 10 ** 9 + 7
        dp = [[1,1,1,0],
              [1,1,1,0],
              [0,0,0,0]]
        # dp = [[1] * 4 for _ in range(3)]
        for _ in range(n):
            temp = [[0] * 4 for _ in range(3)]
            for i in range(2):
                for j in range(3):
                    temp[i][j] = ((dp[i][0] % m) + (dp[i+1][0] % m) + (dp[i][j+1] % m)) % m
            dp = temp
        return dp[0][0] % m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        o = 8
        self.assertEqual(s.checkRecord(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = 3
        self.assertEqual(s.checkRecord(i), o)

    def test_three(self):
        s = Solution()
        i = 10101
        o = 183236316
        self.assertEqual(s.checkRecord(i), o)

    def test_four(self):
        s = Solution()
        i = 100000
        o = 749184020
        self.assertEqual(s.checkRecord(i), o)

    def test_five(self):
        s = Solution()
        i = 99999
        o = 816671055
        self.assertEqual(s.checkRecord(i), o)

    def test_six(self):
        s = Solution()
        i = 3
        o = 19
        self.assertEqual(s.checkRecord(i), o)

    def test_seven(self):
        s = Solution()
        i = 4
        o = 43
        self.assertEqual(s.checkRecord(i), o)

    def test_eight(self):
        s = Solution()
        i = 5
        o = 94
        self.assertEqual(s.checkRecord(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)