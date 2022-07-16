# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is an m x n grid with a ball. The ball is initially at the
    position [startRow, startColumn]. The ball is allowed to move to one
    of the four adjacent cells in the grid (possibly out of the grid
    crossing the grid boundary). At most maxMove moves may be applied to
    the ball.

    Given the five integers m, n, maxMove, startRow, startColumn, return
    the number of paths to move the ball out of the grid boundary. Since
    the answer can be very large, return it modulo 10^9 + 7.
    '''
    # pretty sure modulo is done wrong... (python has infinite integers)
    # to do correctly probably needed to do modulo addition every pace
    # addition occurs (in other language would prevent overflow)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        a = 0
        dp = [[0] * (n + 2) for _ in range(m + 2)]
        dp[startRow + 1][startColumn + 1] = 1
        for _ in range(maxMove):
            g = [[0] * (n + 2) for _ in range(m + 2)]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if dp[i][j]:
                        g[i-1][j] += dp[i][j]
                        g[i+1][j] += dp[i][j]
                        g[i][j+1] += dp[i][j]
                        g[i][j-1] += dp[i][j]
            dp = g
            for i in range(len(dp)):
                a += dp[i][0] + dp[i][-1]
            for i in range(len(dp[0])):
                a += dp[0][i] + dp[-1][i]
        return a % (10**9 + 7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = 2
        k = 2
        l = 0
        m = 0
        o = 6
        self.assertEqual(s.findPaths(i,j,k,l,m), o)

    def test_two(self):
        s = Solution()
        i = 1
        j = 3
        k = 3
        l = 0
        m = 1
        o = 12
        self.assertEqual(s.findPaths(i,j,k,l,m), o)

    def test_three(self):
        s = Solution()
        i = 20
        j = 20
        k = 20
        l = 10
        m = 10
        o = 430048903
        self.assertEqual(s.findPaths(i,j,k,l,m), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)