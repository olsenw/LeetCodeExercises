# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n binary matrix grid and an integer health.

    Start on the upper left corner (0,0) and navigate to the lower right corner
    (m-1,n-1).
    
    It is possible to move up, down, left, or right from one cell to another
    adjacent cell as long as health is positive.

    Cells (i,j) with grid[i][j] = 1 are considered unsafe and reduce health by
    1.

    Return true if is possible to reach the final cell with a health value of 1
    or more, and false otherwise.
    '''
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m,n = len(grid), len(grid[0])
        heap = [(-health,0,0)]
        visited = set()
        while heap:
            h,x,y = heapq.heappop(heap)
            if (x,y) in visited:
                continue
            h += grid[x][y]
            if h == 0:
                continue
            visited.add((x,y))
            if x == m-1 and y == n-1:
                return True
            for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= a < m and 0 <= b < n and (a,b) not in visited:
                    heapq.heappush(heap, (h,a,b))
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
        j = 1
        o = True
        self.assertEqual(s.findSafeWalk(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]]
        j = 3
        o = False
        self.assertEqual(s.findSafeWalk(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[1,1,1],[1,0,1],[1,1,1]]
        j = 5
        o = True
        self.assertEqual(s.findSafeWalk(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)