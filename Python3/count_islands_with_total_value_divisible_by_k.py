# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n matrix grid and a positive integer k. An island is a group of
    positive integers (representing land) that are 4-directionally connected
    (horizontal or vertically).

    The total value of an island is the sum of the values of all cells in the
    island.

    Return the number of islands with a total value divisible by k.
    '''
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        def bfs(row:int,col:int) -> int:
            total = 0
            queue = deque([[row,col]])
            while queue:
                r,c = queue.popleft()
                if grid[r][c] == 0:
                    continue
                total += grid[r][c]
                grid[r][c] = 0
                for i,j in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                    if 0 <= i < m and 0 <= j < n and grid[i][j] > 0:
                        queue.append([i,j])
            return total
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    a = bfs(i,j)
                    answer += a % k == 0
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]]
        j = 5
        o = 2
        self.assertEqual(s.countIslands(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[3,0,3,0], [0,3,0,3], [3,0,3,0]]
        j = 3
        o = 6
        self.assertEqual(s.countIslands(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[0,0,0],[0,0,1],[11,0,6],[0,10,2],[0,0,0],[8,0,0]]
        j = 19
        o = 1
        self.assertEqual(s.countIslands(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)