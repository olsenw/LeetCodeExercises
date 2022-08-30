# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an m x n 2D binary grid which represents a map of '1's (land)
    and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting
    adjacent lands horizontally or vertically. It is assumed that all
    four edges of the grid are all surrounded by water.
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        answer = 0
        def clear(a, b):
            if 0 <= a < m and 0 <= b < n and grid[a][b] == "1":
                grid[a][b] = "0"
                clear(a, b - 1)
                clear(a, b + 1)
                clear(a - 1, b)
                clear(a + 1, b)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    answer += 1
                    clear(i, j)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ]
        o = 1
        self.assertEqual(s.numIslands(i), o)

    def test_two(self):
        s = Solution()
        i = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
        o = 3
        self.assertEqual(s.numIslands(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)