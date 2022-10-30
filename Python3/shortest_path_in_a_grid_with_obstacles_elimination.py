# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an m x n integer matrix grid where each cell is either 0 (empty) or 1
    (obstacle). It is possible to move up, down, left, or right from and to an
    empty cell in one step.

    Return the minimum number of steps to walk from the upper left corner (0, 0)
    to the lower right corner (m - 1, n - 1) given that at most k obstacles can
    be eliminated. If it is not possible to find such a walk, return -1.
    
    Note that grid[0][0] and grid[m-1][n-1] are both 0 (empty).
    '''
    # passes 26/52 test cases
    # seems to work just way to slow
    # because it is dfs and repeating a lot of calculation
    def shortestPath_dfs_tle(self, grid: List[List[int]], k: int) -> int:
        large = 1601
        m, n = len(grid), len(grid[0])
        cost = [[[large] * (k + 1) for _ in range(n)] for _ in range(m)]
        cost[0][0][0] = 0
        # bfs (i, j, k) note k is remaining obstacle removals
        def bfs(a,b,c):
            nonlocal cost
            pass
            # up
            # if a > 0 and cost[a - 1][b][c] == large:
            if a > 0 and cost[a - 1][b][c] > cost[a][b][c] + 1:
                if grid[a - 1][b]:
                    if c < k:
                        cost[a - 1][b][c + 1] = cost[a][b][c] + 1
                        bfs(a - 1, b, c + 1)
                else:
                    cost[a - 1][b][c] = cost[a][b][c] + 1
                    bfs(a - 1, b, c)
            # down
            # if a < m - 1 and cost[a + 1][b][c] == large:
            if a < m - 1 and cost[a + 1][b][c] > cost[a][b][c] + 1:
                if grid[a + 1][b]:
                    if c < k:
                        cost[a + 1][b][c + 1] = cost[a][b][c] + 1
                        bfs(a + 1, b, c + 1)
                else:
                    cost[a + 1][b][c] = cost[a][b][c] + 1
                    bfs(a + 1, b, c)
            # left
            # if b > 0 and cost[a][b - 1][c] == large:
            if b > 0 and cost[a][b - 1][c] > cost[a][b][c] + 1:
                if grid[a][b - 1]:
                    if c < k:
                        cost[a][b - 1][c + 1] = cost[a][b][c] + 1
                        bfs(a, b - 1, c + 1)
                else:
                    cost[a][b - 1][c] = cost[a][b][c] + 1
                    bfs(a, b - 1, c)
            # right
            # if b < n - 1 and cost[a][b + 1][c] == large:
            if b < n - 1 and cost[a][b + 1][c] > cost[a][b][c] + 1:
                if grid[a][b + 1]:
                    if c < k:
                        cost[a][b + 1][c + 1] = cost[a][b][c] + 1
                        bfs(a, b + 1, c + 1)
                else:
                    cost[a][b + 1][c] = cost[a][b][c] + 1
                    bfs(a, b + 1, c)
        bfs(0,0,0)
        answer = min(c for c in cost[m-1][n-1])
        return answer if answer < large else -1

    # passes (barely) 3276 ms
    def shortestPath_bfs(self, grid: List[List[int]], k: int) -> int:
        large = lambda: 1601
        m, n = len(grid), len(grid[0])
        visited = set()
        vist = defaultdict(large)
        vist[(0,0,0)] = 0
        while vist:
            nextUp = defaultdict(large)
            for v in vist:
                a,b,c = v
                # destination
                if a == m - 1 and b == n - 1:
                    return vist[v]
                visited.add(v)
                # up
                if a > 0:
                    if grid[a - 1][b] and c < k and (a - 1, b, c + 1) not in visited:
                        nextUp[(a - 1, b, c + 1)] = min(vist[v] + 1, nextUp[(a - 1, b, c + 1)])
                    elif not grid[a - 1][b] and (a - 1,b,c) not in visited:
                        nextUp[(a - 1, b, c)] = min(vist[v] + 1, nextUp[(a - 1, b, c)])
                # down
                if a < m - 1:
                    if grid[a + 1][b] and c < k and (a + 1, b, c + 1) not in visited:
                        nextUp[(a + 1, b, c + 1)] = min(vist[v] + 1, nextUp[(a + 1, b, c + 1)])
                    elif not grid[a + 1][b] and (a + 1,b,c) not in visited:
                        nextUp[(a + 1, b, c)] = min(vist[v] + 1, nextUp[(a + 1, b, c)])
                # left
                if b > 0:
                    if grid[a][b - 1] and c < k and (a, b - 1, c + 1) not in visited:
                        nextUp[(a, b - 1, c + 1)] = min(vist[v] + 1, nextUp[(a, b - 1, c + 1)])
                    elif not grid[a][b - 1] and (a,b - 1,c) not in visited:
                        nextUp[(a, b - 1, c)] = min(vist[v] + 1, nextUp[(a, b - 1, c)])
                # right
                if b < n - 1:
                    if grid[a][b + 1] and c < k and (a, b + 1, c + 1) not in visited:
                        nextUp[(a, b + 1, c + 1)] = min(vist[v] + 1, nextUp[(a, b + 1, c + 1)])
                    elif not grid[a][b + 1] and (a,b + 1,c) not in visited:
                        nextUp[(a, b + 1, c)] = min(vist[v] + 1, nextUp[(a, b + 1, c)])
            vist = nextUp
        return -1

    # Leetcode sample 156 ms submission
    # https://leetcode.com/submissions/api/detail/1414/python3/156/
    # much better implementation of bfs, use of list instead of dict
    # also "cleaner" state checking
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if k >= m + n - 2:
            return m + n - 2
        
        state = (0, 0, k)
        visited = set()
        visited.add(state)
        
        queue = [(0, state)]
        while len(queue) > 0:
            d, (i, j, r) = queue.pop(0)
            
            if i == m-1 and j == n-1:
                return d
            
            for (ni, nj) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:                
                if 0 <= ni < m and 0 <= nj < n:
                    nr = r - grid[ni][nj]
                    nstate = (ni, nj, nr)
                    
                    if nr >= 0 and nstate not in visited:
                        visited.add(nstate)
                        queue.append((d+1, nstate))
                        
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
        j = 1
        o = 6
        self.assertEqual(s.shortestPath(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[0,1,1],[1,1,1],[1,0,0]]
        j = 1
        o = -1
        self.assertEqual(s.shortestPath(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[0,1],[1,0]]
        j = 1
        o = 2
        self.assertEqual(s.shortestPath(i,j), o)

    def test_four(self):
        s = Solution()
        i = [[0,1],[1,1],[1,0]]
        j = 2
        o = 3
        self.assertEqual(s.shortestPath(i,j), o)

    def test_five(self):
        s = Solution()
        i = [[0,0,1,0,0,0,0,1,0,1,1,0,0,1,1],[0,0,0,1,1,0,0,1,1,0,1,0,0,0,1],[1,1,0,0,0,0,0,1,0,1,0,0,1,0,0],[1,0,1,1,1,1,0,0,1,1,0,1,0,0,1],[1,0,0,0,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,1,1,0,1,1,0,0,1,1,1,1],[0,0,0,1,0,1,0,0,0,0,1,1,0,1,1],[1,0,0,1,1,1,1,1,1,0,0,0,1,1,0],[0,0,1,0,0,1,1,1,1,1,0,1,0,0,0],[0,0,0,1,1,0,0,1,1,1,1,1,1,0,0],[0,0,0,0,1,1,1,0,0,1,1,1,0,1,0]]
        j = 27
        o = 24
        self.assertEqual(s.shortestPath(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)