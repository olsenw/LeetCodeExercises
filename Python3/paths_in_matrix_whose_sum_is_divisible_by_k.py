# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed m x n integer matrix grid and an integer k. Starting at
    (0,0) move to position (m-1, n-1) by moving only down or right.

    Return the number of paths where the sum of the elements on the path is
    divisible by k. Since the answer may be very large return it modulo
    10**9 + 7.
    '''
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10**9 + 7
        m,n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        # running sum for initializing dp
        s = grid[m-1][n-1] % k
        # initialize dp final destination
        dp[m-1][n-1][s] = 1
        # initialize dp right column
        for i in range(m-2, -1, -1):
            s = (s + grid[i][n-1] % k) % k
            dp[i][n-1][s] = 1
        # initialize dp bottom row
        s = grid[m-1][n-1] % k
        for j in range(n-2, -1, -1):
            s = (s + grid[m-1][j] % k) % k
            dp[m-1][j][s] = 1
        # fill out rest of the array based on diagonal
        for x in range(1, min(m, n)):
            j = n - x - 1
            for i in range(m - x - 1, -1, -1):
                for y in range(k):
                    s = (y + grid[i][j] % k) % k
                    dp[i][j][s] = (dp[i][j][s] + dp[i][j+1][y]) % mod
                    dp[i][j][s] = (dp[i][j][s] + dp[i+1][j][y]) % mod
            i = m - x - 1
            for j in range(n - x - 2, -1, -1):
                for y in range(k):
                    s = (y + grid[i][j] % k) % k
                    dp[i][j][s] = (dp[i][j][s] + dp[i][j+1][y]) % mod
                    dp[i][j][s] = (dp[i][j][s] + dp[i+1][j][y]) % mod
        return dp[0][0][0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[5,2,4],[3,0,5],[0,7,2]]
        j = 3
        o = 2
        self.assertEqual(s.numberOfPaths(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[0,0]]
        j = 5
        o = 1
        self.assertEqual(s.numberOfPaths(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[7,3,4,9],[2,3,6,2],[2,3,7,0]]
        j = 1
        o = 10
        self.assertEqual(s.numberOfPaths(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)