# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an n x n grid where some 1 x 1 x 1 cubes. Each value v = grid[i][j]
    represents a tower of v cubes placed on top of cell (i,j).

    After placing these cubes, the adjacent cubes are glued together forming
    several irregular 3D shapes.

    Return the total surface area of the resulting shapes.

    Note: The bottom face of each shape counts toward its surface area.
    '''
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    answer += 2
                    # left
                    if i == 0:
                        answer += grid[i][j]
                    elif grid[i][j] > grid[i-1][j]:
                        answer += grid[i][j] - grid[i-1][j]
                    # up
                    if j == 0:
                        answer += grid[i][j]
                    elif grid[i][j] > grid[i][j-1]:
                        answer += grid[i][j] - grid[i][j-1]
                    # down
                    if i == m-1:
                        answer += grid[i][j]
                    elif grid[i][j] > grid[i+1][j]:
                        answer += grid[i][j] - grid[i+1][j]
                    # right
                    if j == n-1:
                        answer += grid[i][j]
                    elif grid[i][j] > grid[i][j+1]:
                        answer += grid[i][j] - grid[i][j+1]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[3,4]]
        o = 34
        self.assertEqual(s.surfaceArea(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1,1],[1,0,1],[1,1,1]]
        o = 32
        self.assertEqual(s.surfaceArea(i), o)

    def test_three(self):
        s = Solution()
        i = [[2,2,2],[2,1,2],[2,2,2]]
        o = 46
        self.assertEqual(s.surfaceArea(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)