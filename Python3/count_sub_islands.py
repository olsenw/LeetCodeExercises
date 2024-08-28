# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two m x n binary matrices grid1 and grid2 containing only 0's
    (representing water) and 1's (representing land). An island is a group of
    1's connected 4-directionally (horizontal or vertical). Any cells outside of
    the grid are considered water cells.

    An island in grid2 is considered a sub-island if there is an island in grid1
    that contains all the cells that make up this island in grid2.

    Return the number of islands in grid2 that are considered sub-islands 
    '''
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        islandCount = 2
        for i in range(m):
            for j in range(n):
                if grid1[i][j] != 1:
                    continue
                q = deque([(i,j)])
                while q:
                    x,y = q.popleft()
                    if grid1[x][y] != 1:
                        continue
                    grid1[x][y] = islandCount
                    if x > 0:
                        q.append((x-1,y))
                    if x < m - 1:
                        q.append((x+1,y))
                    if y > 0:
                        q.append((x,y-1))
                    if y < n - 1:
                        q.append((x,y+1))
                islandCount += 1
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] != 1:
                    continue
                q = deque([(i,j)])
                s = set()
                while q:
                    x,y = q.popleft()
                    if grid2[x][y] != 1:
                        continue
                    s.add(grid1[x][y])
                    grid2[x][y] = 0
                    if x > 0:
                        q.append((x-1,y))
                    if x < m - 1:
                        q.append((x+1,y))
                    if y > 0:
                        q.append((x,y-1))
                    if y < n - 1:
                        q.append((x,y+1))
                answer += len(s) == 1 and 0 not in s
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
        j = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
        o = 3
        self.assertEqual(s.countSubIslands(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
        j = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
        o = 2
        self.assertEqual(s.countSubIslands(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)