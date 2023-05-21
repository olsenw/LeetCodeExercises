# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an n x n binary matrix grid where 1 represents land and 0 represents
    water.

    An island is a 4-directionally connected group of 1's not connected to any
    other 1's. There are exactly two islands in grid.

    It is possible to change 0's to 1's, connecting two islands.

    Return the smallest number of 0's that must be flipped to connect the two
    islands.
    '''
    def shortestBridge_tle(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def mark():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        q = deque([(i,j)])
                        while q:
                            a,b = q.popleft()
                            grid[a][b] = -1
                            if a > 0 and grid[a-1][b] == 1:
                                q.append((a-1,b))
                            if a < m - 1 and grid[a+1][b] == 1:
                                q.append((a+1,b))
                            if b > 0 and grid[a][b-1] == 1:
                                q.append((a,b-1))
                            if b < n - 1 and grid[a][b+1] == 1:
                                q.append((a,b+1))
                        return
        def bridge(i,j):
            q = deque([(i,j,0)])
            v = set()
            while q:
                a,b,c = q.popleft()
                if (a,b) in v:
                    continue
                v.add((a,b))
                if grid[a][b] == -1:
                    return c - 1
                if a > 0 and grid[a-1][b] < 1:
                    q.append((a-1,b,c+1))
                if a < m - 1 and grid[a+1][b] < 1:
                    q.append((a+1,b,c+1))
                if b > 0 and grid[a][b-1] < 1:
                    q.append((a,b-1,c+1))
                if b < n - 1 and grid[a][b+1] < 1:
                    q.append((a,b+1,c+1))
            return -1
        mark()
        answer = 1000
        for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        b = bridge(i,j)
                        if b != -1:
                            answer = min(answer, b)
        return answer

    # memory exceeded
    def shortestBridge_memory(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        island = deque()
        def mark():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        q = deque([(i,j)])
                        while q:
                            a,b = q.popleft()
                            grid[a][b] = -1
                            island.append((a,b,0))
                            if a > 0 and grid[a-1][b] == 1:
                                q.append((a-1,b))
                            if a < m - 1 and grid[a+1][b] == 1:
                                q.append((a+1,b))
                            if b > 0 and grid[a][b-1] == 1:
                                q.append((a,b-1))
                            if b < n - 1 and grid[a][b+1] == 1:
                                q.append((a,b+1))
                        return
        mark()
        visited = set()
        while island:
            a,b,c = island.popleft()
            if (a,b) in visited:
                continue
            if grid[a][b] == 1:
                return c - 1
            visited.add((a,b))
            if a > 0:
                island.append((a-1,b,c+1))
            if a < m - 1:
                island.append((a+1,b,c+1))
            if b > 0:
                island.append((a,b-1,c+1))
            if b < n - 1:
                island.append((a,b+1,c+1))
        return 0

    # based on leetcode solution
    # https://leetcode.com/problems/shortest-bridge/editorial/
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def find():
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        return (i,j)
        i,j = find()
        grid[i][j] = 2
        island = [(i,j)]
        queue = [(i,j)]
        while island:
            iteration = []
            for x,y in island:
                if x > 0 and grid[x-1][y] == 1:
                    iteration.append((x-1,y))
                    queue.append((x-1,y))
                    grid[x-1][y] = 2
                if x < n - 1 and grid[x+1][y] == 1:
                    iteration.append((x+1,y))
                    queue.append((x+1,y))
                    grid[x+1][y] = 2
                if y > 0 and grid[x][y-1] == 1:
                    iteration.append((x,y-1))
                    queue.append((x,y-1))
                    grid[x][y-1] = 2
                if y < n - 1 and grid[x][y+1] == 1:
                    iteration.append((x,y+1))
                    queue.append((x,y+1))
                    grid[x][y+1] = 2
            island = iteration
        answer = 0
        while queue:
            iteration = []
            for x,y in queue:
                if x > 0:
                    if grid[x-1][y] == 1:
                        return answer
                    elif grid[x-1][y] == 0:
                        iteration.append((x-1,y))
                        grid[x-1][y] = 2
                if x < n - 1:
                    if grid[x+1][y] == 1:
                        return answer
                    elif grid[x+1][y] == 0:
                        iteration.append((x+1,y))
                        grid[x+1][y] = 2
                if y > 0:
                    if grid[x][y-1] == 1:
                        return answer
                    elif grid[x][y-1] == 0:
                        iteration.append((x,y-1))
                        grid[x][y-1] = 2
                if y < n - 1:
                    if grid[x][y+1] == 1:
                        return answer
                    elif grid[x][y+1] == 0:
                        iteration.append((x,y+1))
                        grid[x][y+1] = 2
            queue = iteration
            answer += 1
        return 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[1,0]]
        o = 1
        self.assertEqual(s.shortestBridge(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,1,0],[0,0,0],[0,0,1]]
        o = 2
        self.assertEqual(s.shortestBridge(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
        o = 1
        self.assertEqual(s.shortestBridge(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,0,1,1,1,0],[0,1,1,1,0,0],[1,1,1,0,0,0],[0,1,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        o = 1
        self.assertEqual(s.shortestBridge(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)