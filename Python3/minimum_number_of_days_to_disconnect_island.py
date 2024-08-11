# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n binary grid where 1 represents land and 0 represents water.
    An island is a maximal 4-directionally (horizontal or vertical) connected
    group of 1's.

    The grid is said to be connected if there is exactly one island, otherwise
    it is said to be disconnected.

    In one day, it is possible to change any single land cell (1) into a water
    cell (0).

    Return the minimum number of days to disconnect the grid. 
    '''
    # hints state that there are 3 possible answers
    def minDays_wrong(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def bfs(x,y):
            landmass = 0
            q = deque([(x,y)])
            while q:
                i,j = q.popleft()
                if grid[i][j] != 1:
                    continue
                landmass += 1
                grid[i][j] = 0
                for a,b in [(-1,0),(0,-1),(1,0),(0,1)]:
                    if 0 <= i+a < m and 0 <= j+b < n and grid[i+a][j+b] != 0:
                        grid[i][j] -= 1
                        q.append((i+a,j+b))
            return landmass
        islands = 0
        landmass = m * n + 1
        easy = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    islands += 1
                    landmass = min(landmass,bfs(i,j))
                if grid[i][j] == -1:
                    easy = True
        if islands == 1:
            if easy and landmass != 2:
                return 1
            return 2
        return 0

    def minDays(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        # use bfs to count the number of islands
        def numIslands():
            islands = 0
            visited = set()
            for x in range(m):
                for y in range(n):
                    if grid[x][y] == 1 and (x,y) not in visited:
                        islands += 1
                        queue = deque([(x,y)])
                        while queue:
                            i,j = queue.popleft()
                            if (i,j) in visited:
                                continue
                            visited.add((i,j))
                            for a,b in [(-1,0),(0,-1),(1,0),(0,1)]:
                                if 0 <= i+a < m and 0 <= j+b < n and grid[i+a][j+b] == 1:
                                    queue.append((i+a,j+b))
            return islands
        # if there are zero islands or 2+ islands the grid is already disconnected
        if numIslands() != 1:
            return 0
        # try removing every land tile and check if that changes the number of islands
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if numIslands() != 1:
                        return 1
                    grid[i][j] = 1
        # default case to cut the corner off an island
        return 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
        o = 2
        self.assertEqual(s.minDays(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1]]
        o = 2
        self.assertEqual(s.minDays(i), o)

    def test_three(self):
        s = Solution()
        i = [
            [0,0,1,0,0,0],
            [1,1,1,0,0,0],
            [1,1,1,1,0,0],
            [0,1,1,0,0,0],
            [0,0,1,0,0,0]
            ]
        o = 1
        self.assertEqual(s.minDays(i), o)

    def test_four(self):
        s = Solution()
        i = [
            [0,0,1,0,0,0],
            [1,1,1,0,0,0],
            [1,1,1,1,0,0],
            [0,1,1,0,0,0],
            [0,0,1,0,0,1]
            ]
        o = 0
        self.assertEqual(s.minDays(i), o)

    def test_five(self):
        s = Solution()
        i = [
            [0,1,1,0,0,0],
            [1,1,1,1,1,0],
            [1,1,1,1,1,0],
            [0,1,1,1,1,0],
            [0,1,1,0,0,0]
            ]
        o = 2
        self.assertEqual(s.minDays(i), o)

    def test_six(self):
        s = Solution()
        i = [
            [1,1,0,1,1],
            [1,1,1,1,1],
            [1,1,0,1,1],
            [1,1,0,1,1]]
        o = 1
        self.assertEqual(s.minDays(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)