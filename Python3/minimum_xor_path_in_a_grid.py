# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array grid of size m * n.

    Starting at the top-left cell (0,0) and moving to the bottom-right cell
    (m-1,n-1).

    At each step it is possible to move either right or down.

    The cost of a path is defined as the bitwise XOR of all the values in the
    cells along that path, including the start and end cells.

    Return the minimum possible XOR value among all valid paths from (0,0) to
    (m-1,n-1).
    '''
    def minCost_fails(self, grid: list[list[int]]) -> int:
        m,n = len(grid), len(grid[0])
        @cache
        def dfs(i,j) -> int:
            if i == m-1 and j == n-1:
                return grid[i][j]
            if i == m-1:
                return grid[i][j] ^ dfs(i,j+1)
            if j == n-1:
                return grid[i][j] ^ dfs(i+1,j)
            return min(grid[i][j] ^ dfs(i,j+1), grid[i][j] ^ dfs(i+1,j))
        return dfs(0,0)

    def minCost_fails(self, grid: list[list[int]]) -> int:
        m,n = len(grid), len(grid[0])
        @cache
        def dfs(i,j,x) -> int:
            if i == m-1 and j == n-1:
                return x ^ grid[i][j]
            if i == m-1:
                return dfs(i,j+1, grid[i][j])
            if j == n-1:
                return dfs(i+1,j, grid[i][j])
            return min(dfs(i,j+1, grid[i][j]), dfs(i+1,j, grid[i][j]))
        return dfs(0,0,grid[0][0])

    def minCost_incomplete(self, grid: list[list[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[[False] * 1023 for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = True
        for i in range(m):
            for j in range(n):
                for x in range(1023):
                    if dp[i][j][x] == False:
                        continue
                    if i < m - 1:
                        dp[i+1][j][x ^ grid[i][j]]
                    if j < n - 1:
                        dp[i][j+1][x ^ grid[i][j]]
        answer = grid[0][0]
        for i in range(grid[0][0],-1,-1):
            if dp[0][0]:
                answer = i
        return answer

    def minCost_hints_incomplete(self, grid: list[list[int]]) -> int:
        m,n = len(grid), len(grid[0])
        answer = 1023
        def dfs(i,j,x) -> None:
            nonlocal answer
            if i == m-1 and j == n-1:
                answer = min(answer, x ^ grid[i][j])
            return
        dfs(0,0,1023)
        return answer

    # based on leetcode editorial
    # https://leetcode.com/problems/minimum-xor-path-in-a-grid/editorial/?envType=daily-question&envId=2026-10-28
    def minCost(self, grid: list[list[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                value = grid[i][j]
                # union of all reachable values
                reachable = dp[j] | (dp[j-1] if j > 0 else set())
                dp[j] = {k ^ value for k in reachable}
        return min(dp[-1])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[3,4]]
        o = 6
        self.assertEqual(s.minCost(i), o)

    def test_two(self):
        s = Solution()
        i = [[6,7],[5,8]]
        o = 9
        self.assertEqual(s.minCost(i), o)

    def test_three(self):
        s = Solution()
        i = [[2,7,5]]
        o = 0
        self.assertEqual(s.minCost(i), o)

    def test_four(self):
        s = Solution()
        i = [[11,10,4],[19,9,13]]
        o = 5
        self.assertEqual(s.minCost(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)