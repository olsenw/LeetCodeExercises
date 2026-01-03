# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a grid of size n x 3 where each cell needs to be painted with exactly
    one of three colors: Red, Yellow, or Green while making sure that no two
    adjacent cells have the same color (ie, no two cells that share vertical or
    horizontal sides have the same color).

    Given n the number of rows of the grid, return the number of ways that the
    grid can be painted. As the answer may grow large, return it modulo
    10^9 + 7.
    '''
    def numOfWays_fails(self, n: int) -> int:
        m = 10**9 + 7
        def madd(a,b):
            return (a % m + b % m) % m
        possible = ["RYR", "RYG", "RGR", "RGY", "YRY", "YRG", "YGR", "YGY", "GRY", "GRG", "GYR", "GYG"]
        @cache
        def dp(s:str,n:int) -> int:
            if n == 0:
                return 0
            answer = 0
            for p in possible:
                t = any(p[i] == s[i] for i in range(len(s)))
                if not t:
                    answer = madd(answer, 1 + dp(p,n-1))
            return answer
        d = {p:[s for s in possible if not any(p[i] == s[i] for i in range(3))] for p in possible}
        answer = 0
        for p in possible:
            answer = madd(answer, 1 + dp(p,n-1))
        return answer

    def numOfWays(self, n: int) -> int:
        m = 10**9 + 7
        def madd(a,b):
            return (a % m + b % m) % m
        possible = ["RYR", "RYG", "RGR", "RGY", "YRY", "YRG", "YGR", "YGY", "GRY", "GRG", "GYR", "GYG"]
        d = {p:[s for s in possible if not any(p[i] == s[i] for i in range(3))] for p in possible}
        @cache
        def dp(s:str,n:int) -> int:
            if n == 0:
                return 1
            answer = 0
            for p in d[s]:
                answer = madd(answer, dp(p,n-1))
            return answer
        answer = 0
        for p in possible:
            answer = madd(answer, dp(p,n-1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 12
        self.assertEqual(s.numOfWays(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 54
        self.assertEqual(s.numOfWays(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = 246
        self.assertEqual(s.numOfWays(i), o)

    def test_four(self):
        s = Solution()
        i = 4
        o = 1122
        self.assertEqual(s.numOfWays(i), o)

    def test_five(self):
        s = Solution()
        i = 5
        o = 5118
        self.assertEqual(s.numOfWays(i), o)

    def test_six(self):
        s = Solution()
        i = 5000
        o = 30228214
        self.assertEqual(s.numOfWays(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)