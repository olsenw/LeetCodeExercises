# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D array of characters grid of size m x n, find if there exists any
    cycles consisting of the same value in grid.

    A cycle is a path of length 4 or more in the grid that starts and ends at
    the same cell. From a given cell, it is possible to move to one of the cells
    adjacent to it - in one of the four directions (up, down, left, or right),
    if it has the same value of the current cell.

    It is not possible to move to the cell that was previously occupied.

    Return true if any cycle of the same value exists in grid, otherwise, return
    false.
    '''
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n = len(grid),len(grid[0])
        visited = set()
        def dfs(x:int,y:int, a:int,b:int):
            if (x,y) in visited:
                return True
            visited.add((x,y))
            if y-1 >= 0 and (x,y-1) != (a,b) and grid[x][y-1] == grid[a][b] and dfs(x,y-1,x,y):
                return True
            if y+1 < n and (x,y+1) != (a,b) and grid[x][y+1] == grid[a][b] and dfs(x,y+1,x,y):
                return True
            if x-1 >= 0 and (x-1,y) != (a,b) and grid[x-1][y] == grid[a][b] and dfs(x-1,y,x,y):
                return True
            if x+1 < m and (x+1,y) != (a,b) and grid[x+1][y] == grid[a][b] and dfs(x+1,y,x,y):
                return True
            return False
        for i in range(m):
            for j in range(n):
                visited.clear()
                if grid[i][j] != ' ' and dfs(i,j,i,j):
                    return True
                for x,y in visited:
                    grid[x][y] = ' '
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
        o = True
        self.assertEqual(s.containsCycle(i), o)

    def test_two(self):
        s = Solution()
        i = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
        o = True
        self.assertEqual(s.containsCycle(i), o)

    def test_three(self):
        s = Solution()
        i = [["a","b","b"],["b","z","b"],["b","b","a"]]
        o = False
        self.assertEqual(s.containsCycle(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)