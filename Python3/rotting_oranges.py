# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n grid where each cell can have one of three values:
    * 0 representing an empty cell,
    * 1 representing a fresh orange, or
    * 2 representing a rotten orange.

    Every minute, any fresh orange that is 4-directionally adjacent to a rotten
    orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a
    fresh orange. If this is impossible, return -1.
    '''
    # simulation (works due to small constraints)
    # could instead been done using bfs instead (less repeats)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        answer = 0
        g = [r[:] for r in grid]
        rotted = any(any(c == 1 for c in r) for r in grid)
        while rotted:
            rotted = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (
                       (i > 0 and grid[i-1][j] == 2) or
                       (i < m - 1 and grid[i+1][j] == 2) or
                       (j > 0 and grid[i][j-1] == 2) or
                       (j < n - 1 and grid[i][j+1] == 2)):
                            g[i][j] = 2
                            rotted += 1
            if rotted:
                answer += 1
            grid = [r[:] for r in g]
        return -1 if any(any(c == 1 for c in r) for r in grid) else answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,1,1],[1,1,0],[0,1,1]]
        o = 4
        self.assertEqual(s.orangesRotting(i), o)

    def test_two(self):
        s = Solution()
        i = [[2,1,1],[0,1,1],[1,0,1]]
        o = -1
        self.assertEqual(s.orangesRotting(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,2]]
        o = 0
        self.assertEqual(s.orangesRotting(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)