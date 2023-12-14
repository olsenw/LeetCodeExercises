# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed m x n binary matrix grid.

    A 0-indexed m x n difference matrix diff is created with the following
    procedure:
    * Let the number of ones in the ith row be onesRowi.
    * Let the number of ones in the jth column be onesColj.
    * Let the number of zeros in the ith row be zerosRowi.
    * Let the number of zeros in the jth column be zerosColj.
    * diff[i][j] = onesRowi + onesColj - zerosRowi - zerosRowj.

    Return the difference matrix diff.
    '''
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        rows = list(sum(m) for m in grid)
        cols = list(sum(m) for m in zip(*grid))
        return [[rows[i] + cols[j] - m + rows[i] - n + cols[j] for j in range(n)] for i in range(m)]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,1],[1,0,1],[0,0,1]]
        o = [[0,0,4],[0,0,4],[-2,-2,2]]
        self.assertEqual(s.onesMinusZeros(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1,1],[1,1,1]]
        o = [[5,5,5],[5,5,5]]
        self.assertEqual(s.onesMinusZeros(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)