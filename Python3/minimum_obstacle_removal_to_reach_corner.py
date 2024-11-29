# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import sys
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed 2D integer array grid of size m x n. Each cell has one of
    two values:
    * 0 represents an empty cell,
    * 1 represents an obstacle that may be removed.

    It is possible to move up, down, left, right from and to an empty cell.

    Return the minimum number of obstacles to remove to move from the upper left
    corner (0,0) to lower right corner (m - 1, n - 1).
    '''
    def minimumObstacles_incomplete(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        target = (m-1,n-1)
        visited = dict()
        heap = [(0,0,0)]
        while heap:
            r,x,y = heapq.heappop(heap)
            if (x,y) in visited and visited[(x,y)] >= r:
                continue
            visited[(x,y)] = r
            if (x,y) == target:
                return r
            if x > 0:
                if grid[x-1][y] == 1:
                    heapq.heappush(heap, (r+1,x,y))
        return -1

    # based on Leetcode editorial Dijkstra's Algorithm
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m,n = len(grid), len(grid[0])
        visit = [[sys.maxsize] * n for _ in range(m)]
        visit[0][0] = grid[0][0]
        queue = [(visit[0][0], 0, 0)]
        while queue:
            x,y,z = heapq.heappop(queue)
            if (y,z) == (m-1,n-1):
                return x
            for a,b in directions:
                if 0 <= y + a <= m - 1 and 0 <= z + b <= n - 1:
                    o = x + grid[y+a][z+b]
                    if o < visit[y+a][z+b]:
                        visit[y+a][z+b] = o
                        heapq.heappush(queue, (o,y+a,z+b))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,1],[1,1,0],[1,1,0]]
        o = 2
        self.assertEqual(s.minimumObstacles(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
        o = 0
        self.assertEqual(s.minimumObstacles(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)