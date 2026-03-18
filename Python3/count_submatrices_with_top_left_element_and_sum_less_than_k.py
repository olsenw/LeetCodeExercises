# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer matrix grid and an integer k.

    Return the number of submatrices that contain the top left element of the
    grid, and have a sum less than or equal to k.
    '''
    def countSubmatrices_incorrect(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        rowPrefix:list[list[int]] = [[0] * n for _ in range(m)]
        colPrefix:list[list[int]] = [[0] * n for _ in range(m)]
        for i in range(m):
            rowPrefix[i][0] = grid[i][0]
            for j in range(1,n):
                rowPrefix[i][j] = rowPrefix[i][j-1] + grid[i][j]
        for j in range(n):
            colPrefix[0][j] = grid[0][j]
        for i in range(1,m):
            for j in range(n):
                colPrefix[i][j] = colPrefix[i-1][j] + grid[i][j]
        answer = 0
        for i in range(m):
            for j in range(n):
                if rowPrefix[i][j] + colPrefix[i][j] <= k:
                    answer += 1
                else:
                    break
        return answer

    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        colPrefix = [[0] * n for _ in range(m)]
        rowPrefix = [[0] * n for _ in range(m)]
        answer = 0
        for i in range(m):
            for j in range(n):
                colPrefix[i][j] += colPrefix[i-1][j] + grid[i][j] if i > 0 else grid[i][j]
                rowPrefix[i][j] = rowPrefix[i][j-1] + colPrefix[i][j] if j > 0 else colPrefix[i][j]
                answer += rowPrefix[i][j] <= k
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[7,6,3],[6,6,1]]
        j = 18
        o = 4
        self.assertEqual(s.countSubmatrices(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[7,2,9],[1,5,0],[2,6,6]]
        j = 20
        o = 6
        self.assertEqual(s.countSubmatrices(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)