# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an n x n integer matrix grid where each value grid[i][j] represents
    the elevation at that point (i,j).

    It starts raining, and water gradually rises over time. At time t, the water
    level is t, meaning any cell with elevation less than or equal to t is
    submerged or reachable.

    It is possible to swim from a square to another 4-directionally adjacent
    square if an only if the elevation of both squares individually are at most
    t. It is possible to swim infinite distance in zero time, when swimming
    within the boundaries of the grid.

    Return the minimum time until it is possible to swim to the bottom right
    square (n-1, n-1) if starting at the top left square (0, 0).
    '''
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def possible(height:int) -> bool:
            visited = set()
            queue = deque([(0,0)])
            while queue:
                i,j = queue.popleft()
                if (i,j) in visited:
                    continue
                if i == n-1 and j == n-1:
                    return True
                visited.add((i,j))
                for x,y in [[-1,0],[1,0],[0,-1],[0,1]]:
                    if 0 <= i + x < n and 0 <= j + y < n and (i+x,j+y) not in visited and grid[i+x][j+y] <= height:
                        queue.append((i+x,j+y))
            return False
        j = max(max(i) for i in grid)
        i = grid[0][0]
        while i < j:
            k = i + ((j - i) // 2)
            if possible(k):
                j = k
            else:
                i = k + 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,2],[1,3]]
        o = 3
        self.assertEqual(s.swimInWater(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
        o = 16
        self.assertEqual(s.swimInWater(i), o)

    def test_three(self):
        s = Solution()
        i = [[3,2],[0,1]]
        o = 3
        self.assertEqual(s.swimInWater(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)