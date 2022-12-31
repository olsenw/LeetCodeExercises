# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an m x n integer array grid where grid[i][j] could be:
    * 1 representing the starting square. There is exactly one starting square.
    * 2 representing the ending square. There is exactly one ending square.
    * 0 representing empty squares that can be traversed.
    * -1 representing obstacles that cannot be traversed.

    Return the number of 4-directional walks from the starting square to the
    ending square, that walk over every non-obstacle square exactly once.
    '''
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def test(s,i,j):
            v = 1 << (i * n + j)
            return s & v == v
        def set(s,i,j):
            return s | 1 << (i * n + j)
        x,y,a,b,c = 0, 0, 0, 1, set(0,m,0)-1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x,y = i,j
                elif grid[i][j] == 2:
                    a,b = i,j
                elif grid[i][j] == -1:
                    c ^= set(0,i,j)
        answer = 0
        s = set(0,x,y)
        q = deque([(x,y,s)])
        while q:
            x,y,s = q.popleft()
            if x == a and y == b:
                if s == c:
                    answer += 1
                continue
            if x > 0 and grid[x-1][y] > -1 and not test(s,x-1,y):
                q.append((x-1,y,set(s,x-1,y)))
            if x < m - 1 and grid[x+1][y] > -1 and not test(s,x+1,y):
                q.append((x+1,y,set(s,x+1,y)))
            if y > 0 and grid[x][y-1] > -1 and not test(s,x,y-1):
                q.append((x,y-1,set(s,x,y-1)))
            if y < n - 1 and grid[x][y+1] > -1 and not test(s,x,y+1):
                q.append((x,y+1,set(s,x,y+1)))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
        o = 2
        self.assertEqual(s.uniquePathsIII(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
        o = 4
        self.assertEqual(s.uniquePathsIII(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,1],[2,0]]
        o = 0
        self.assertEqual(s.uniquePathsIII(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)