# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D grid consisting of 0s (land) and 1s (water). An island is a
    maximal 4-directionally connected group of 0s and a closed island is an
    island totally (all left, top, right, bottom) surrounded by 1s.

    Return the number of closed islands.
    '''
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    valid = True
                    q = deque([(i,j)])
                    while q:
                        a,b = q.popleft()
                        if grid[a][b] == 1:
                            continue
                        if a == 0 or a == m - 1 or b == 0 or b == n - 1:
                            valid = False
                        grid[a][b] = 1
                        if a > 0:
                            q.append((a-1,b))
                        if a < m - 1:
                            q.append((a+1,b))
                        if b > 0:
                            q.append((a,b-1))
                        if b < n - 1:
                            q.append((a,b+1))
                    if valid:
                        islands += 1
        return islands

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
        o = 2
        self.assertEqual(s.closedIsland(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
        o = 1
        self.assertEqual(s.closedIsland(i), o)

    def test_three(self):
        s = Solution()
        i =[[1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1],
            [1,0,1,1,1,0,1],
            [1,0,1,0,1,0,1],
            [1,0,1,1,1,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1]]
        o = 2
        self.assertEqual(s.closedIsland(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)