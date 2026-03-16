# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n integer matrix grid.

    A rhombus sum is the sum of the elements that form the border of a regular
    rhombus shape in grid. The rhombus must have the shape of a square rotated
    45 degrees with each of the corners centered in a grid cell.
    
    Note that the rhombus can have an area of 0, which is a single cell.

    Return the biggest three distinct rhombus sums in the grid in descending
    order. If there are less than three distinct values, return all of them.
    '''
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid), len(grid[0])
        def getPerimeter(i:int,j:int,r:int) -> int:
            if i - r < 0 or i + r >= m or j - r < 0 or j + r >= n:
                return 0
            if r == 0:
                return grid[i][j]
            s = 0
            x = i - r
            y = j
            for z in range(r+1):
                s += grid[x + z][y + z]
            x = i
            y = j - r
            for z in range(r+1):
                s += grid[x + z][y + z]
            x = i
            y = j - r
            for z in range(1,r):
                s += grid[x - z][y + z]
            x = i + r
            y = j
            for z in range(1,r):
                s += grid[x - z][y + z]
            return s
        rhombus = []
        values = set()
        # treat each cell as the center of a rhombus
        for i in range(m):
            for j in range(n):
                pass
                # find the largest possible rhombus sum
                for k in range(min(m,n)):
                    r = getPerimeter(i,j,k)
                    if r == 0:
                        break
                    elif r in values:
                        continue
                    elif len(rhombus) == 3:
                        heapq.heappushpop(rhombus,r)
                    else:
                        heapq.heappush(rhombus,r)
                    values.add(r)
        return sorted(rhombus, reverse=True)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
        o = [228,216,211]
        self.assertEqual(s.getBiggestThree(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        o = [20,9,8]
        self.assertEqual(s.getBiggestThree(i), o)

    def test_three(self):
        s = Solution()
        i = [[7,7,7]]
        o = [7]
        self.assertEqual(s.getBiggestThree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)