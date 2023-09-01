# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a row x col grid representing a map where grid[i][j] = 1 represents
    land and grid[i][j] = 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). The grid
    is completely surrounded by water, and there is exactly one island (ie one
    or more connected land cells).

    The island doesn't have "lakes", meaning the water inside isn't connected to
    the water around the island. One cell is a square with side length 1. The
    grid is rectangular, width and height don't exceed 100. Determine the
    perimeter of the island.
    '''
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q = deque([(i,j)])
                    v = set()
                    while q:
                        x,y = q.popleft()
                        if (x,y) in v:
                            continue
                        v.add((x,y))
                        for a,b in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                            if a < 0 or a == m or b < 0 or b == n:
                                if a < 0:
                                    answer += 1
                                if a == m:
                                    answer += 1
                                if b < 0:
                                    answer += 1
                                if b == n:
                                    answer += 1
                            else:
                                if grid[a][b] == 1:
                                    q.append((a,b))
                                else:
                                    answer += 1
                    return answer
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        o = 16
        self.assertEqual(s.islandPerimeter(i), o)

    def test_two(self):
        s = Solution()
        i = [[1]]
        o = 4
        self.assertEqual(s.islandPerimeter(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,0]]
        o = 4
        self.assertEqual(s.islandPerimeter(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,0,0],[1,0,1],[1,1,1]]
        o = 14
        self.assertEqual(s.islandPerimeter(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)