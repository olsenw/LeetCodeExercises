# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The chess knight has a unique movement, it may move two squares vertically
    and one square horizontally, or two squares horizontally and one square
    vertically (with both forming the shape of an L). The possible movements of
    chess knight are shown in a diagram on the LeetCde problem page.

    Given a chess knight and a phone pad as seen on LeetCode problem page, the
    knight can only stand on a numeric cell.

    Given an integer n, return how many distinct phone numbers of length n that
    can be dialed.

    The knight can be placed on any numeric cell initially and should make n - 1
    jumps to dial a number of length n. All jumps should be valid knight jumps.

    As the answer may be very large, return the answer modulo 10^9+7.
    '''
    def knightDialer(self, n: int) -> int:
        m = 10**9 + 7
        @cache
        def dp(i, j, k):
            if not ((i == 1 and j == 3) or (0 <= i < 3 and 0 <= j < 3)):
                return -1
            if k == 0:
                return 1
            a = 0
            for x,y in [(i+2,j+1),(i+2,j-1),(i-2,j+1),(i-2,j-1),(i+1,j+2),(i+1,j-2),(i-1,j+2),(i-1,j-2)]:
                if dp(x,y,k-1) != -1:
                    a = ((a % m) + (dp(x,y,k-1) % m)) % m
            return a if a > 0 else -1
        a = 0
        for i,j in [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(1,3)]:
            if dp(i,j,n-1) > 0:
                a = ((a % m) + (dp(i,j,n-1) % m)) % m
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 10
        self.assertEqual(s.knightDialer(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 20
        self.assertEqual(s.knightDialer(i), o)

    '''
    passes online
    but this fails here due to recursion limit
    '''
    def test_three(self):
        s = Solution()
        i = 3131
        o = 136006598
        self.assertEqual(s.knightDialer(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)