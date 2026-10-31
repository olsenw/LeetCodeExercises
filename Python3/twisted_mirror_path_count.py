# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an mxn binary grid where:
    * grid[i][j] == 0 represents an empty cell, and
    * grid[i][j] == 1 represents a mirror.

    A robot starts at the top-left corner of the grid (0,0) and wants to reach
    the bottom-right corner (m-1,n-1). It can move only right or down. If the
    robot attempts to move into a mirror cell, it is reflected before entering
    that cell:
    * If it tries to move right into a mirror, it is turned down and moved into
      the cell directly below the mirror.
    * If it tries to move down into a mirror, it is turned right and moved into
      the cell directly to the right of the mirror.
    
    If this reflection would cause the robot to move outside the grid
    boundaries, the path is considered invalid and should not be counted.

    Return the number of unique valid paths from (0,0) to (m-1, n-1).

    Since the answer may be very large, return it modulo 10^9 + 7.

    Note: If a reflection moves the robot into a mirror cell, the robot is
    immediately reflected again based on the direction it used to enter that
    mirror: if it entered while moving right, it will be turned down; if it
    entered while moving down, it will be turned right. This process will
    continue until either the last cell is reached, the robot moves out of
    bounds or the robot moves to a non-mirror cell.
    '''
    def uniquePaths_tle(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m,n = len(grid), len(grid[0])
        go = [[[[0]*2 for _ in range(2)] for _ in range(n)] for _ in range(m)]
        @cache
        def follow(i:int, j:int, dir:int) -> List[int]:
            # dir == 0 is right
            # dir == 1 is down
            if i == m or j == n:
                return [-1,-1]
            if grid[i][j] == 1:
                dir = 0 if dir == 1 else 1
                if dir == 0:
                    return follow(i,j+1,dir)
                return follow(i+1,j,dir)
            return [i,j]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                go[i][j][0] = follow(i,j+1,0)
                go[i][j][1] = follow(i+1,j,1)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                x,y = go[i][j][0]
                if x == -1 or y == -1:
                    pass
                else:
                    dp[x][y] = ((dp[i][j] % MOD) + (dp[x][y] % MOD)) % MOD
                x,y = go[i][j][1]
                if x == -1 or y == -1:
                    pass
                else:
                    dp[x][y] = ((dp[i][j] % MOD) + (dp[x][y] % MOD)) % MOD
        return dp[-1][-1]

    # slow but it works
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m,n = len(grid), len(grid[0])
        go = [[[[m-1,n-1] for _ in range(2)] for _ in range(n)] for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    continue
                if grid[i][j] == 0:
                    # go[i][j][0] = go[i][j+1][0] if j < n - 1 else [-1,-1]
                    # go[i][j][1] = go[i+1][j][1] if i < m - 1 else [-1,-1]
                    go[i][j][0] = ([i,j+1] if grid[i][j+1] == 0 else go[i][j+1][0]) if j < n - 1 else [-1,-1]
                    go[i][j][1] = ([i+1,j] if grid[i+1][j] == 0 else go[i+1][j][1]) if i < m - 1 else [-1,-1]
                else:
                    go[i][j][0] = ([i+1,j] if grid[i+1][j] == 0 else go[i+1][j][1]) if i < m - 1 else [-1,-1]
                    go[i][j][1] = ([i,j+1] if grid[i][j+1] == 0 else go[i][j+1][0]) if j < n - 1 else [-1,-1]
                pass
        go[-1][-1] = [[-1,-1],[-1,-1]]
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                x,y = go[i][j][0]
                if x == -1 or y == -1:
                    pass
                else:
                    dp[x][y] = ((dp[i][j] % MOD) + (dp[x][y] % MOD)) % MOD
                x,y = go[i][j][1]
                if x == -1 or y == -1:
                    pass
                else:
                    dp[x][y] = ((dp[i][j] % MOD) + (dp[x][y] % MOD)) % MOD
        return dp[-1][-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,0],[0,0,1],[1,0,0]]
        o = 5
        self.assertEqual(s.uniquePaths(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0],[0,0]]
        o = 2
        self.assertEqual(s.uniquePaths(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,1,1],[1,1,0]]
        o = 1
        self.assertEqual(s.uniquePaths(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)