# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a m x n matrix grid consisting of non-negative integers where
    grid[row][col] represents the minimum time required to be able to visit the
    cell (row, col), which means that cell (row, col) can only be visited when
    the visit time is greater than or equal to grid[row][col].

    Start at the top-left cell of the matrix in the 0th second, and it is
    required to move to any adjacent cell in the four directions: up, down,
    left, and right. Each move takes 1 second.

    Return the minimum time required to visit the bottom right cell of the
    matrix. If it is not possible to the visit the bottom-right cell, then
    return -1.
    '''
    # based on Leetcode modified Dijkstra's Algorithm editorial
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        m,n = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        queue = [(grid[0][0],0,0)]
        while queue:
            x,y,z = heapq.heappop(queue)
            if (y,z) == (m-1,n-1):
                return x
            if (y,z) in visited:
                continue
            visited.add((y,z))
            for a,b in directions:
                if 0 <= y+a <= m-1 and 0 <= z+b <= n-1:
                    w = 1 if (grid[y+a][z+b] - x) % 2 == 0 else 0
                    heapq.heappush(queue, (max(grid[y+a][z+b] + w, x + 1), y+a, z+b))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
        o = 7
        self.assertEqual(s.minimumTime(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,2,4],[3,2,1],[1,0,4]]
        o = -1
        self.assertEqual(s.minimumTime(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)