# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an n x n binary matrix grid. It is possible to change at most one 0
    to a 1.

    Return the size of the largest island in grid after applying this operation.

    An island is a 4-directionally connected group of 1s.
    '''
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def bfs(i,j,group):
            answer = 0
            queue = deque([(i,j)])
            grid[i][j] = group
            while queue:
                i,j = queue.popleft()
                answer += 1
                for a,b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0 <= a < n and 0 <= b < n and grid[a][b] == 1:
                        grid[a][b] = group
                        queue.append((a,b))
            return answer
        answer = 0
        group = {0:0, 1:1}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    group[len(group)] = bfs(i,j,len(group))
                    answer = max(answer, group[len(group) - 1])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    g = []
                    for a,b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if 0 <= a < n and 0 <= b < n and grid[a][b] not in g:
                            g.append(grid[a][b])
                    answer = max(answer, 1 + sum(group[x] for x in g))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0],[0,1]]
        o = 3
        self.assertEqual(s.largestIsland(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[1,0]]
        o = 4
        self.assertEqual(s.largestIsland(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,1],[1,1]]
        o = 4
        self.assertEqual(s.largestIsland(i), o)

    def test_four(self):
        s = Solution()
        i = [[0,1,1],[1,0,1],[1,1,0]]
        o = 7
        self.assertEqual(s.largestIsland(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)