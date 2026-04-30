# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n grid where each cell contains on of the values 0, 1, or 2.
    Also given is an integer k.

    Starting from the top-left corner (0,0) reach the bottom-right corner
    (m-1, n-1) by moving only right or down.

    Each cell contributes a specific score and incurs an associated cost,
    according to their cell values:
    * 0: adds 0 to the score and costs 0.
    * 1: adds 1 to the score and costs 1.
    * 2: adds 2 to the score and costs 1.

    Return the maximum score achievable without exceeding a total cost of k, or
    -1 if no valid path exists.

    Note: If the path reaches the bottom right cell but the total cost exceeds
    k, the path is invalid.
    '''
    # a lot of repeating work when doing dfs
    def maxPathScore_tle(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        def dfs(i:int,j:int,score:int,cost:int) -> int:
            if i == m-1 and j == n-1:
                return -1 if cost > k else score
            answer = -1
            if i < m-1:
                answer = max(
                    answer,
                    dfs(i+1, j, score + grid[i+1][j], cost + min(1, grid[i+1][j]))
                )
            if j < n-1:
                answer = max(
                    answer,
                    dfs(i, j+1, score + grid[i][j+1], cost + min(1, grid[i][j+1]))
                )
            return answer
        return dfs(0,0,0,0)

    # based on hints
    # gives away the dynamic relation
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        k = min(k+1, m+n)
        # max score possible at [i][j][exact cost]
        dp = [[[-1]*k for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0
        for i in range(m):
            for j in range(n):
                cost = min(grid[i][j], 1)
                score = grid[i][j]
                for c in range(k):
                    if c - cost < 0:
                        continue
                    if i > 0 and dp[i-1][j][c-cost] != -1:
                        dp[i][j][c] = max(
                            dp[i][j][c],
                            dp[i-1][j][c-cost] + score
                        )
                    if j > 0 and dp[i][j-1][c-cost] != -1:
                        dp[i][j][c] = max(
                            dp[i][j][c],
                            dp[i][j-1][c-cost] + score
                        )
        pass
        return max(dp[m-1][n-1])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0, 1],[2, 0]]
        j = 1
        o = 2
        self.assertEqual(s.maxPathScore(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[0, 1],[1, 2]]
        j = 1
        o = -1
        self.assertEqual(s.maxPathScore(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[1] * 200 for _ in range(200)]
        i[0][0] = 0
        j = 400
        o = 398
        self.assertEqual(s.maxPathScore(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)