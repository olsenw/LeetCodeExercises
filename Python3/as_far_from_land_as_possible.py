# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an nxn grid containing only values 0 and 1, where 0 represents water
    and 1 represents land, find a water cell such that its distance to the
    nearest land cell is maximized, and return the distance. If no land or water
    exists in the grid, return -1.

    The distance used in this problem is the Manhattan distance between two
    cells (x0,y0) and (x1,y1) is |x0 - x1| + |y0 + y1|.
    '''
    # bfs time limit exceeded
    def maxDistance_bfs_tle(self, grid: List[List[int]]) -> int:
        n = len(grid)
        answer = 0
        def bfs(i:int, j:int) -> int:
            q = deque([(i,j,0)])
            v = set()
            while q:
                i,j,k = q.popleft()
                if (i,j) in v:
                    continue
                v.add((i,j))
                if grid[i][j] == 1:
                    return k
                if i > 0:
                    q.append((i-1,j,k+1))
                if j > 0:
                    q.append((i,j-1,k+1))
                if i < n - 1:
                    q.append((i+1,j,k+1))
                if j < n - 1:
                    q.append((i,j+1,k+1))
            return 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    answer = max(answer, bfs(i,j))
        return -1 if answer == 0 else answer

    # leetcode disscusion post by harshithdshetty
    # https://leetcode.com/problems/as-far-from-land-as-possible/solutions/3166139/python3-522-ms-faster-than-91-13-of-python3/?languageTags=python
    # tipsy and not thinking
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = deque((i, j) for i in range(n) for j in range(n) if grid[i][j])
        res = 0
        while dq:
            r0, c0 = dq.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r1, c1 = r0 + dr, c0 + dc
                if 0 <= r1 < n and 0 <= c1 < n and not grid[r1][c1]:
                    dq.append((r1, c1))
                    grid[r1][c1] = grid[r0][c0] + 1
                    res = max(res, grid[r1][c1])
        return res - 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0,1],[0,0,0],[1,0,1]]
        o = 2
        self.assertEqual(s.maxDistance(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0,0],[0,0,0],[0,0,0]]
        o = 4
        self.assertEqual(s.maxDistance(i), o)

    def test_three(self):
        s = Solution()
        i = [[1]]
        o = -1
        self.assertEqual(s.maxDistance(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,1],[1,1]]
        o = -1
        self.assertEqual(s.maxDistance(i), o)

    def test_five(self):
        s = Solution()
        i = [[0]]
        o = -1
        self.assertEqual(s.maxDistance(i), o)

    def test_six(self):
        s = Solution()
        i = [[0,0],[0,0]]
        o = -1
        self.assertEqual(s.maxDistance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)