# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import deque

class Solution:
    '''
    Given an n x n binary matrix grid, return the length of the shortest
    clear path in the matrix. If there is no clear path return -1.

    A clear path in a binary matrix is a path from the top-left cell (ie
    (0,0)) to the bottom-right cell (ie (n-1, n-1)) such that:
    * All the visited cells of the path are 0.
    * All the adjacent cells of the path are 8-directionally connected
      (ie they are different and they share an edge or a corner).

    The length of a clear path is the number of visited cells of this 
    path.
    '''
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # start square is non zero
        if grid[0][0]:
            return -1
        n = len(grid)
        d = [[float('inf')] * n for _ in range(n)]
        d[0][0] = 1
        s = deque([(0,0)])
        while s:
            x, y = s.popleft()
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < n and 0 <= j < n and not grid[i][j] \
                        and d[x][y] + 1 < d[i][j]:
                        d[i][j] = d[x][y] + 1
                        s.append((i,j))
        return d[n-1][n-1] if d[n-1][n-1] < float('inf') else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[1,0]]
        o = 2
        self.assertEqual(s.shortestPathBinaryMatrix(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0,0],[1,1,0],[1,1,0]]
        o = 4
        self.assertEqual(s.shortestPathBinaryMatrix(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,0,0],[1,1,0],[1,1,0]]
        o = -1
        self.assertEqual(s.shortestPathBinaryMatrix(i), o)

    def test_four(self):
        s = Solution()
        i = [[0,1,0],[1,1,0],[1,1,0]]
        o = -1
        self.assertEqual(s.shortestPathBinaryMatrix(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)