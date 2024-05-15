# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from collections import deque
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed 2D matrix grid of size n x n, where (r,c) represents:
    * A cell containing a thief if grid[r][c] = 1
    * An empty cell if grid[r][c] = 0

    Initially a knight is positioned at cell (0,0). In one move the knight can
    move to any adjacent cell in the grid, including cells containing thieves.

    The safeness factor of a path on the grid is defined as the minimum
    manhattan distance from any cell in the path to any thief in the grid.

    Return the maximum safeness factor of all path leading to cell (n-1, n-1).

    An adjacent cell of cell (r,c), is once of the cells (r,c+1), (r,c-1),
    (r+1,c), and (r-1,c) if the cells exist.

    The manhattan distance between two cells (a,b) and (x,y) is equal to
    |a - x| + |b - y|, where |val| denotes the absolute value of val.
    '''
    # time limit exceeded
    def maximumSafenessFactor_tle(self, grid: List[List[int]]) -> int:
        n = len(grid)
        thieves = [(i,j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        manhattan = [[min(abs(i - x) + abs(j - y) for x,y in thieves) for j in range(n)] for i in range(n)]
        visited = set()
        def dfs(i,j,k):
            if (i,j) in visited:
                return 0
            if (i,j) == (n-1,n-1):
                return min(k,manhattan[i][j])
            visited.add((i,j))
            a = 0
            if i < n - 1:
                a = max(a, dfs(i+1,j,min(k,manhattan[i][j])))
            if i > 0:
                a = max(a, dfs(i-1,j,min(k,manhattan[i][j])))
            if j < n - 1:
                a = max(a, dfs(i,j+1,min(k,manhattan[i][j])))
            if j > 0:
                a = max(a, dfs(i,j-1,min(k,manhattan[i][j])))
            visited.remove((i,j))
            return a
        return dfs(0,0,10**7+1)

    # time limit exceeded
    def maximumSafenessFactor_tle(self, grid: List[List[int]]) -> int:
        n = len(grid)
        thieves = [(i,j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        manhattan = [[min(abs(i - x) + abs(j - y) for x,y in thieves) for j in range(n)] for i in range(n)]
        visited = set()
        def dfs(i,j,k):
            if manhattan[i][j] < k or (i,j) in visited:
                return False
            if (i,j) == (n-1,n-1):
                return True
            a = False
            visited.add((i,j))
            if i < n - 1:
                a |= dfs(i+1,j,k)
            if j < n - 1:
                a |= dfs(i,j+1,k)
            if i > 0:
                a |= dfs(i-1,j,k)
            if j > 0:
                a |= dfs(i,j-1,k)
            visited.remove((i,j))
            return a
        i,j = 0, manhattan[-1][-1]
        while i < j:
            k = i + (j - i) // 2
            if dfs(i,j,k):
                j = k
            else:
                i = k + 1
        return i

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque((i,j,0) for i in range(n) for j in range(n) if grid[i][j] == 1)
        m = [[999] * n for _ in range(n)]
        while q:
            i,j,k = q.popleft()
            if m[i][j] > k:
                m[i][j] = k
                if i < n - 1:
                    q.append((i+1,j,k+1))
                if i > 0:
                    q.append((i-1,j,k+1))
                if j < n - 1:
                    q.append((i,j+1,k+1))
                if j > 0:
                    q.append((i,j-1,k+1))
        i,j = 0, m[-1][-1]
        while i < j:
            k = i + (j - i) // 2 + (j - i) % 2
            q = deque([(0,0)] if m[0][0] >= k else [])
            v = set()
            a = False
            while q:
                x,y = q.popleft()
                if (x,y) in v:
                    continue
                if (x,y) == (n-1,n-1):
                    a = True
                    break
                v.add((x,y))
                if x < n - 1 and m[x+1][y] >= k:
                    q.append((x+1,y))
                if x > 0 and m[x-1][y] >= k:
                    q.append((x-1,y))
                if y < n - 1 and m[x][y+1] >= k:
                    q.append((x,y+1))
                if y > 0 and m[x][y-1] >= k:
                    q.append((x,y-1))
            if a:
                i = k
            else:
                j = k - 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0,0],[0,0,0],[0,0,1]]
        o = 0
        self.assertEqual(s.maximumSafenessFactor(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0,1],[0,0,0],[0,0,0]]
        o = 2
        self.assertEqual(s.maximumSafenessFactor(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
        o = 2
        self.assertEqual(s.maximumSafenessFactor(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,1,1],[1,1,1],[1,1,0]]
        o = 0
        self.assertEqual(s.maximumSafenessFactor(i), o)

    def test_five(self):
        s = Solution()
        i = [[1,1,1],[0,1,1],[0,0,0]]
        o = 0
        self.assertEqual(s.maximumSafenessFactor(i), o)

    def test_six(self):
        s = Solution()
        i = [[0,1,1],[0,1,0],[1,0,0]]
        o = 0
        self.assertEqual(s.maximumSafenessFactor(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)