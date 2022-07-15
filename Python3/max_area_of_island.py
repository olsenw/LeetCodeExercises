# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an m x n binary matrix grid. An island is a group of 1's
    (representing land) connected 4-directionally (horizontal and
    vertical). Assume that the edges of grid are surrounded by water.

    The area of an island is the number of cells with a value 1 in the
    island.

    Return the maximum area of an island in grid. If there is no island
    return 0.
    '''
    def maxAreaOfIsland_dfs(self, grid: List[List[int]]) -> int:
        m = len(grid) - 1
        n = len(grid[0]) - 1
        def dfs(i,j):
            a = 1
            grid[i][j] = 0
            if i > 0 and grid[i-1][j]:
                a += dfs(i-1,j)
            if i < m and grid[i+1][j]:
                a += dfs(i+1,j)
            if j > 0 and grid[i][j-1]:
                a += dfs(i,j-1)
            if j < n and grid[i][j+1]:
                a += dfs(i,j+1)
            return a
        b = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    b = max(b, dfs(i,j))
        return b

    def maxAreaOfIsland_dfs_alt(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
        b = 0
        for i in range(m):
            for j in range(n):
                b = max(b, dfs(i,j))
        return b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        o = 6
        self.assertEqual(s.maxAreaOfIsland(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0,0,0,0,0,0,0]]
        o = 0
        self.assertEqual(s.maxAreaOfIsland(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)