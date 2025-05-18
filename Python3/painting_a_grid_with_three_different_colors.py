# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers m and n. Consider an m x n grid where each cell is
    initially white. It is possible to paint each cell red, green, or blue. All
    cells must be painted.

    Return the number of ways to color the grid with no two adjacent cells
    having the same color. Since the answer can be very large, return it modulo
    10^9 + 7.
    '''
    m = 10**9 + 7

    def ma(a:int,b:int) -> int:
        return ((a % Solution.m) + (b % Solution.m)) % Solution.m

    # going out of control
    def colorTheGrid_meh(self, m: int, n: int) -> int:
        def p(i:int, last:int) -> list[int]:
            if i == m:
                return [[]]
            answer = []
            for color in [1,2,3]:
                if last == color:
                    continue
                for j in p(i + 1, color):
                    answer.append([color] + j)
            return answer
        possible = []
        for i in p(0,0):
            a = 0
            for j in i:
                a <<= 2
                a |= j
            possible.append(a)
        pass
        def dp(i:int, last:int) -> int:
            if i == n:
                return 0
            return
        return dp(0,0)

    # very slow
    def colorTheGrid(self, m: int, n: int) -> int:
        md = 10**9+7
        @cache
        def pp(i:int, last:str) -> list[int]:
            if i == m:
                return [""]
            answer = []
            for color in "rgb":
                if last == color:
                    continue
                for j in pp(i + 1, color):
                    answer.append(color + j)
            return answer
        possible = pp(0, " ")
        @cache
        def dp(i:int, last:str) -> int:
            if i == n:
                return 1
            answer = 0
            for p in possible:
                if any(a==b for a,b in zip(last, p)):
                    continue
                answer = ((answer % md) + (dp(i+1,p) % md)) % md
            return answer
        return dp(0, " ")

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        j = 1
        o = 3
        self.assertEqual(s.colorTheGrid(i,j), o)

    def test_two(self):
        s = Solution()
        i = 1
        j = 2
        o = 6
        self.assertEqual(s.colorTheGrid(i,j), o)

    def test_three(self):
        s = Solution()
        i = 5
        j = 5
        o = 580986
        self.assertEqual(s.colorTheGrid(i,j), o)

    def test_four(self):
        s = Solution()
        i = 3
        j = 50
        o = 151149117
        self.assertEqual(s.colorTheGrid(i,j), o)

    def test_five(self):
        s = Solution()
        i = 2
        j = 2
        o = 18
        self.assertEqual(s.colorTheGrid(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)