# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an n x n integer matrix grid.

    Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
    * maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid
      centered around row i + 1 and column j + 1.
    
    In other words, find the largest value in every contiguous 3 x 3 matrix in
    grid.

    Return the generated matrix.
    '''
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        answer = [[0] * (n-2) for _ in range(n-2)]
        for i in range(1,n-1):
            for j in range(1,n-1):
                answer[i-1][j-1] = max(
                    grid[x][y] for x in range(i-1,i+2) for y in range(j-1,j+2)
                )
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
        o = [[9,9],[8,6]]
        self.assertEqual(s.largestLocal(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
        o = [[2,2,2],[2,2,2],[2,2,2]]
        self.assertEqual(s.largestLocal(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)