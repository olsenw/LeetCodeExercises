# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    In a gold mine grid of size of m x n, each cell in this mine has an integer
    representing the amount of gold in that cell, 0 if it is empty.

    Return the maximum amount of gold that can be collected under the following
    conditions:
    * Every time a cell is occupied all the gold is collected from that cell.
    * From a given cell it is possible to move up, down, left or right.
    * A cell can never be visited more than once.
    * Never visit a cell with 0 gold.
    * It is possible to start and stop collecting gold from any position in the
      grind that has gold.
    '''
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        visited.update((i,-1) for i in range(m))
        visited.update((i,n) for i in range(m))
        visited.update((-1,j) for j in range(n))
        visited.update((m,j) for j in range(n))
        def dfs(i:int, j:int) -> int:
            t = (i,j)
            if t in visited or grid[i][j] == 0:
                return 0
            visited.add(t)
            a = max(
                dfs(i-1,j),
                dfs(i+1,j),
                dfs(i,j-1),
                dfs(i,j+1)
            )
            visited.remove(t)
            return grid[i][j] + a
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    answer = max(answer, dfs(i,j))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,6,0],[5,8,7],[0,9,0]]
        o = 24
        self.assertEqual(s.getMaximumGold(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
        o = 28
        self.assertEqual(s.getMaximumGold(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)