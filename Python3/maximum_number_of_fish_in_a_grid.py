# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed 2D matrix grid of size m x n, where [r, c] represents:
    * A land cell if grid[r][c] = 0, or
    * A water cell containing grid[r][c] fish, if grid[r][c] > 0.

    A fisher can start at any water cell (r, c) and can do the following
    operations any number of times:
    * Catch all the fish at cell (r, c), or
    * Move to any adjacent water cell.

    Return the maximum number of fish the fisher can catch if he chooses his
    starting cell optimally, or 0 if no water cell exists.

    An adjacent cell of the cell (r, c), is one of the cells (r, c+1), (r, c-1),
    (r+1, c) or (r-1, c) if it exists.
    '''
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def bfs(i:int, j:int) -> int:
            answer = grid[i][j]
            grid[i][j] = 0
            queue = deque([(i,j)])
            while queue:
                i,j = queue.popleft()
                for a,b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0 <= a < m and 0 <= b < n and grid[a][b] > 0:
                        answer += grid[a][b]
                        grid[a][b] = 0
                        queue.append((a,b))
            return answer
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    answer = max(answer, bfs(i,j))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
        o = 7
        self.assertEqual(s.findMaxFish(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
        o = 1
        self.assertEqual(s.findMaxFish(i), o)

    def test_three(self):
        s = Solution()
        i = [[9,10]]
        o = 19
        self.assertEqual(s.findMaxFish(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)