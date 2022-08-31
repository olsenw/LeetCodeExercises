# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is an m x n rectangular island that borders both the Pacific
    Ocean and Atlantic Ocean. The Pacific Ocean touches the island's
    left and top edges, and the Atlantic Ocean touches the island's
    right and bottom edges.

    The island is partitioned into a grid of square cells. Given an
    m x n integer matrix heights where heights[r][c] represents the
    height above sea level of the cell at coordinate (r,c).

    The island receives a lot of rain, and the rain water can flow to
    neighboring cells directly north, south, east, and west if the
    neighboring cell's height is less than or equal to the current
    cell's height. Water can flow from any cell adjacent to an ocean
    into the ocean.

    Return a 2D list of grid coordinates result where
    result[i] = [ri, ci] denotes that the rain water can flow
    from cell (ri, ci) to both the Pacific and Atlantic oceans.
    '''
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        def bfs(matrix, check):
            v = set()
            while check:
                u = []
                for r,c in check:
                    if (r,c) not in v:
                        matrix[r][c] = True
                        v.add((r,c))
                        if r > 0 and heights[r-1][c] >= heights[r][c]: u.append([r-1,c])
                        if r < m - 1 and heights[r+1][c] >= heights[r][c]: u.append([r+1,c])
                        if c > 0 and heights[r][c-1] >= heights[r][c]: u.append([r,c-1])
                        if c < n - 1 and heights[r][c+1] >= heights[r][c]: u.append([r,c+1])
                check = u
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        p = []
        a = []
        for r in range(m):
            p.append([r,0])
            a.append([r,n-1])
        for c in range(n):
            p.append([0,c])
            a.append([m-1,c])
        # expand pacific
        bfs(pacific, p)
        # expand atlantic
        bfs(atlantic, a)
        return [[r,c] for r in range(m) for c in range(n) if pacific[r][c] and atlantic[r][c]]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        o = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        self.assertEqual(s.pacificAtlantic(i), o)

    def test_two(self):
        s = Solution()
        i = [[1]]
        o = [[0,0]]
        self.assertEqual(s.pacificAtlantic(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)