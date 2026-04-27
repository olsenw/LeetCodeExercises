# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
from enum import Enum
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n grid. Each cell of grid represents a street. The street of
    grid[i][j] can be:
    * 1 which means a street connecting the left cell and the right cell.
    * 2 which means a street connecting the upper cell and the lower cell.
    * 3 which means a street connecting the left cell and the lower cell.
    * 4 which means a street connecting the right cell and the lower cell.
    * 5 which means a street connecting the left cell and the upper cell.
    * 6 which means a street connecting the right cell cell and the upper cell.

    Initially start at the street of the upper-left cell (0,0). A valid path in
    the grid is a path that starts from the upper left cell (0,0) and ends at
    the bottom-right cell (m-1, n-1). The path should only follow the streets.

    Notice that it is not possible to change any street.

    Return true if there is a valid path in the grid or false otherwise.
    '''
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m,n = len(grid), len(grid[0])
        North = 0
        East = 1
        South = 2
        West = 3
        street = {
            # North,East,South,West
            0:[True,True,True,True],
            1:[False,True,False,True],
            2:[True,False,True,False],
            3:[False,False,True,True],
            4:[False,True,True,False],
            5:[True,False,False,True],
            6:[True,True,False,False]
        }
        visited = set()
        def dfs(x:int,y:int)->bool:
            if x == m-1 and y == n-1:
                return True
            if (x,y) in visited:
                return False
            visited.add((x,y))
            if grid[x][y] == 1:
                if y-1 >= 0 and street[grid[x][y-1]][East]:
                    if dfs(x,y-1):
                        return True
                if y+1 < n and street[grid[x][y+1]][West]:
                    if dfs(x,y+1):
                        return True
            elif grid[x][y] == 2:
                if x-1 >= 0 and street[grid[x-1][y]][South]:
                    if dfs(x-1,y):
                        return True
                if x+1 < m and street[grid[x+1][y]][North]:
                    if dfs(x+1,y):
                        return True
            elif grid[x][y] == 3:
                if y-1 >= 0 and street[grid[x][y-1]][East]:
                    if dfs(x,y-1):
                        return True
                if x+1 < m and street[grid[x+1][y]][North]:
                    if dfs(x+1,y):
                        return True
            elif grid[x][y] == 4:
                if y+1 < n and street[grid[x][y+1]][West]:
                    if dfs(x,y+1):
                        return True
                if x+1 < m and street[grid[x+1][y]][North]:
                    if dfs(x+1,y):
                        return True
            elif grid[x][y] == 5:
                if y-1 >= 0 and street[grid[x][y-1]][East]:
                    if dfs(x,y-1):
                        return True
                if x-1 >= 0 and street[grid[x-1][y]][South]:
                    if dfs(x-1,y):
                        return True
            elif grid[x][y] == 6:
                if y+1 < n and street[grid[x][y+1]][West]:
                    if dfs(x,y+1):
                        return True
                if x-1 >= 0 and street[grid[x-1][y]][South]:
                    if dfs(x-1,y):
                        return True
            return False
        return dfs(0,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,4,3],[6,5,2]]
        o = True
        self.assertEqual(s.hasValidPath(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,1],[1,2,1]]
        o = False
        self.assertEqual(s.hasValidPath(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,1,2]]
        o = False
        self.assertEqual(s.hasValidPath(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)