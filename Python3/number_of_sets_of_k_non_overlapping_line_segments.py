# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at
    x = i, find the number of ways exactly k non-overlapping line segments such
    that each segment covers two or more points. The endpoints of each segment
    must have integral coordinates. the k line segments do not have to cover all
    n points and they are allowed to share endpoints.

    Return the number of ways that k non-overlapping line segments can be drawn.
    Since this number can be huge, return it modulo 10^9+7.
    '''
    # does not count anything
    def numberOfSets_fails(self, n: int, k: int) -> int:
        m = 10**9 + 7
        @cache
        def dp(index:int, segments:int, open:bool) -> int:
            if index == n:
                return 0 if segments == 0 else -1
            if segments <= 0:
                return segments
            answer = dp(index+1, segments, open)
            if open == True:
                answer = max(answer, 1 + dp(index, segments-1, False))
            for i in range(index, n):
                answer = max(answer, dp(i+1, segments, open))
                if open == False:
                    answer = max(answer, dp(i+1, segments, True))
            return answer % m
        answer = dp(0,0,False)
        return answer if answer >= 0 else -1

    # based on leetcode editorial
    # https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/editorial/?envType=daily-question&envId=2026-09-16
    def numberOfSets(self, n: int, k: int) -> int:
        m = 10**9 + 7
        # rolling dp array
        dp = [1] * n
        # used to precalculate all previous combinations
        prefix = [0] * (n+1)
        # initialize
        for j in range(n):
            prefix[j+1] = (prefix[j] + dp[j]) % m
        # find exact number of segments
        for _ in range(k):
            # impossible to have segment at zero as it needs to open first
            dp[0] = 0
            # previous transition + all possible previous states
            for j in range(1,n):
                dp[j] = (dp[j-1] + prefix[j]) % m
            # increment prefix array with updated values
            for j in range(n):
                prefix[j+1] = (prefix[j] + dp[j]) % m
        return dp[n-1]

    # describing this as a combination is easier, but requires understanding of
    # to the math behind why it works
    # comb(n+k-1, 2k) selecting 2k distinct numbers from possible numbers

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = 2
        o = 5
        self.assertEqual(s.numberOfSets(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 1
        o = 3
        self.assertEqual(s.numberOfSets(i,j), o)

    def test_three(self):
        s = Solution()
        i = 30
        j = 7
        o = 796297179
        self.assertEqual(s.numberOfSets(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)