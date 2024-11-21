# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers m and n representing a 0-indexed m x n grid. Also given
    two 2D integer arrays guards and walls where guards[i] = [rowi,coli] and
    walls[j] = [rowj, colj] represent the positions of the ith guard and jth
    wall respectively.

    A guard can see every cell in the four cardinal directions (north, east,
    south, or west) starting from their position unless obstructed by a wall or
    another guard. A cell is guarded if there is al least one guard that can see
    it.

    Return the number of unoccupied cells that are not guarded.
    '''
    def countUnguarded_tle(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for i,j in walls:
            grid[i][j] = 2
        for i,j in guards:
            for x in range(i,-1,-1):
                if grid[x][j] < 2:
                    grid[x][j] = 1
                else:
                    break
            for x in range(i+1,m):
                if grid[x][j] < 2:
                    grid[x][j] = 1
                else:
                    break
            for y in range(j,-1,-1):
                if grid[i][y] < 2:
                    grid[i][y] = 1
                else:
                    break
            for y in range(j+1,n):
                if grid[i][y] < 2:
                    grid[i][y] = 1
                else:
                    break
            grid[i][j] = 3
        return sum(grid[i][j] == 0 for i in range(m) for j in range(n))

    # place guards as blockers first to allow early loop termination
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for i,j in walls:
            grid[i][j] = 2
        for i,j in guards:
            grid[i][j] = 3
        for i,j in guards:
            for x in range(i-1,-1,-1):
                if grid[x][j] < 2:
                    grid[x][j] = 1
                else:
                    break
            for x in range(i+1,m):
                if grid[x][j] < 2:
                    grid[x][j] = 1
                else:
                    break
            for y in range(j-1,-1,-1):
                if grid[i][y] < 2:
                    grid[i][y] = 1
                else:
                    break
            for y in range(j+1,n):
                if grid[i][y] < 2:
                    grid[i][y] = 1
                else:
                    break
        return sum(grid[i][j] == 0 for i in range(m) for j in range(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = 6
        k = [[0,0],[1,1],[2,3]]
        l = [[0,1],[2,2],[1,4]]
        o = 7
        self.assertEqual(s.countUnguarded(i,j,k,l), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 3
        k = [[1,1]]
        l = [[0,1],[1,0],[2,1],[1,2]]
        o = 4
        self.assertEqual(s.countUnguarded(i,j,k,l), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)