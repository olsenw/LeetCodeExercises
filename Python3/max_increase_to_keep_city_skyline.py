# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a city composed of n x n blocks, where each block contains a single
    building shaped like a vertical square prism. Given a 0-indexed n x n
    integer matrix grid where grid[r][c] represents the height of te building
    located in the block at row r and column c.

    A city's skyline is the outer contour formed by all the buildings when
    viewing the side of the city from a distance. The skyline from each cardinal
    direction north, east, south, and west may be different.

    It is possible to increase the height of any number of building by any
    amount (the amount can be different per building). The height of a 0-height
    building can also be increased. However, increasing the height of a building
    should not affect the city's skyline from any cardinal direction.

    Return the maximum total sum that the height of the buildings can be
    increased by without changing the city's skyline from any cardinal
    direction.
    '''
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        right = [max(g) for g in grid]
        down = [max(grid[i][j] for i in range(n)) for j in range(n)]
        answer = 0
        for i in range(n):
            for j in range(n):
                answer += min(right[j], down[i]) - grid[i][j]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
        o = 35
        self.assertEqual(s.maxIncreaseKeepingSkyline(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0,0],[0,0,0],[0,0,0]]
        o = 0
        self.assertEqual(s.maxIncreaseKeepingSkyline(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)