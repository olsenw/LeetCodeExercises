# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from collections import defaultdict
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s and t, return the number of distinct subsequences of s
    which equals t.

    The test cases are generated so that the answer fits on a 32-bit signed
    integer.
    '''
    # Issue occurs when many too many branching paths to check
    # Need an early termination of some kind
    def numDistinct_tle(self, s: str, t: str) -> int:
        cnt = Counter(t)
        indices = defaultdict(list)
        for i,j in enumerate(s):
            indices[j].append(i)
        for i in cnt:
            if cnt[i] > len(indices[i]):
                return 0
        # index in t, minimum index in s
        @cache
        def possibles(target:int, index:int) -> int:
            if target == len(t):
                return 1
            answer = 0
            c = t[target]
            i = bisect.bisect_left(indices[c], index)
            for j in indices[c][i:]:
                answer += possibles(target + 1, j + 1)
            return answer
        return possibles(0, 0)

    # Based on solution by Anmol Mittal
    # https://leetcode.com/problems/distinct-subsequences/solutions/8504520/intuitive-top-down-dp-memoization-step-b-56td/?envType=daily-question&envId=2026-09-06
    def numDistinct(self, s: str, t: str) -> int:
        # subsequences of t[0..j] in s[0..i]
        @cache
        def solve(i:int,j:int) -> int:
            # matched all characters in t
            if j < 0:
                return 1
            # no more characters in s left to match
            if i < 0:
                return 0
            answer = 0
            # state transition character match
            if s[i] == t[j]:
                answer += solve(i-1,j-1)
            # state transition characters do not match (also for skips on matching)
            answer += solve(i-1,j)
            return answer
        return solve(len(s)-1,len(t)-1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "rabbbit"
        j = "rabbit"
        o = 3
        self.assertEqual(s.numDistinct(i,j), o)

    def test_two(self):
        s = Solution()
        i = "babgbag"
        j = "bag"
        o = 5
        self.assertEqual(s.numDistinct(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)