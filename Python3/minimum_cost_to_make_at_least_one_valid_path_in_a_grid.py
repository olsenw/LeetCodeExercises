# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n grid. Each cell of the grid has a sign pointing to the next
    cell that should be visited if currently in the cell. The sign of grid[i][j]
    can be:
    * 1 which means go to the cell to the right. (ie go from grid[i][j] to
      grid[i][j+1])
    * 2 which means go to the cell to the left. (ie go from grid[i][j] to
      grid[i][j-1])
    * 3 which means go to the lower cell. (ie go from grid[i][j] to
      grid[i+1][j])
    * 4 which means go to the upper cell. (ie go from grid[i][j] to
      grid[i-1][j])
    
    Notice that there could be some signs on the cells of the grid that point
    outside the grid.

    Initially start at the upper left cell (0,0). A valid path in the grid is a
    path that starts from the upper left cell (0,0) and ends at the bottom-right
    cell (m - 1, n - 1) following the signs on the grid. The valid path does not
    have to be the shortest.

    It is possible to modify the sign on a cell with a cost = 1. A cell can be
    modified only once.

    Return the minimum cost to make the grid have at least one valid path.
    '''
    def minCost(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        # [up 0, right 1, down 2, left 3]
        arr = {(i,j):[1,1,1,1] for i in range(m) for j in range(n)}
        for i in range(m):
            for j in range(n):
                if i == 0:
                    arr[(i,j)][0] = 10000
                if grid[i][j] == 3:
                    arr[(i,j)][2] = 0
                if i == m - 1:
                    arr[(i,j)][2] = 10000
                if grid[i][j] == 1:
                    arr[(i,j)][1] = 0
                if j == 0:
                    arr[(i,j)][3] = 10000
                if grid[i][j] == 4:
                    arr[(i,j)][0] = 0
                if j == n - 1:
                    arr[(i,j)][1] = 10000
                if grid[i][j] == 2:
                    arr[(i,j)][3] = 0
        visited = set()
        heap = [(0,0,0)]
        while heap:
            d,i,j = heapq.heappop(heap)
            if (i,j) == (m-1,n-1):
                return d
            if (d,i,j) in visited:
                continue
            visited.add((d,i,j))
            if i > 0:
                heapq.heappush(heap, (d+arr[(i,j)][0], i-1, j))
            if i < m-1:
                heapq.heappush(heap, (d+arr[(i,j)][2], i+1, j))
            if j > 0:
                heapq.heappush(heap, (d+arr[(i,j)][3], i, j-1))
            if j < n-1:
                heapq.heappush(heap, (d+arr[(i,j)][1], i, j+1))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
        o = 3
        self.assertEqual(s.minCost(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1,3],[3,2,2],[1,1,4]]
        o = 0
        self.assertEqual(s.minCost(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2],[4,3]]
        o = 1
        self.assertEqual(s.minCost(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)