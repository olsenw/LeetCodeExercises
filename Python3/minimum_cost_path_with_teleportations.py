# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a m x n 2D integer array grid and an integer k. Start at the top-left
    cell (0,0) and reach the bottom-right cell (m-1,n-1).

    There are two types of moves available:
    * Normal move: move right or down from the current (i,j). The cost is the
      value of the destination cell.
    * Teleportation: teleport from any cell (i,j), to any cell (x,y) such that
      grid[x][y] <= grid[i][j]; the cost of this move is 0. It is possible to
      teleport at most k times.
    
    Return the minimum total cost to reach cell (m-1, n-1) from (0, 0).
    '''
    # time limit exceeded
    def minCost_tle(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        @cache
        def dp(teleports:int, x:int, y:int) -> int:
            if x == m - 1 and y == n - 1:
                return 0
            answer = float('inf')
            if x < m - 1:
                answer = min(answer, dp(teleports, x+1, y) + grid[x+1][y])
            if y < n - 1:
                answer = min(answer, dp(teleports, x, y+1) + grid[x][y+1])
            if teleports > 0:
                for i in range(m):
                    for j in range(n):
                        if grid[i][j] <= grid[x][y]:
                            answer = min(answer, dp(teleports-1, i, j))
            return answer
        return dp(k, 0, 0)

    # based on Leetcode editorial
    # https://leetcode.com/problems/minimum-cost-path-with-teleportations/editorial/?envType=daily-question&envId=2026-01-28
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        # sort the points in grid by their costs
        points = [(i,j) for i in range(m) for j in range(n)]
        points.sort(key=lambda x: grid[x[0]][x[1]])
        # track current cost from (i,j) -> (m-1,n-1)
        dp = [[float('inf')] * n for _ in range(m)]
        # iterate through the teleports
        for t in range(k + 1):
            minCost = float('inf')
            # update based on last teleport
            # i,j used to iterate through sorted grid points
            j = 0
            for i in range(len(points)):
                minCost = min(minCost, dp[points[i][0]][points[i][1]])
                # find all points with the same grid value
                if i + 1 < len(points) and grid[points[i][0]][points[i][1]] == grid[points[i+1][0]][points[i+1][1]]:
                    i += 1
                    continue
                # update minimum costs for points with given grid value
                for r in range(j, i + 1):
                    dp[points[r][0]][points[r][1]] = minCost
                j = i + 1
            # iterate through the dp array
            # calculate minimum cost of moving right/down
            # note the iteration is backwards (up/left) (m-1,n-1) -> (0,0)
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if i == m - 1 and j == n -1:
                        dp[i][j] = 0
                        continue
                    # update base on cost going down
                    if i != m - 1:
                        dp[i][j] = min(dp[i][j], dp[i+1][j] + grid[i+1][j])
                    # update base on cost going right
                    if j != n - 1:
                        dp[i][j] = min(dp[i][j], dp[i][j+1] + grid[i][j+1])
        return dp[0][0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,3,3],[2,5,4],[4,3,5]]
        j = 2
        o = 7
        self.assertEqual(s.minCost(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[2,3],[3,4]]
        j = 1
        o = 9
        self.assertEqual(s.minCost(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)