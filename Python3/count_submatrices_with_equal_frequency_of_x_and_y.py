# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or
    '.', return the number of submatrices that contain:
    * grid[0][0]
    * an equal frequency of 'X' and 'Y'.
    * at least one 'X'.
    '''
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        answer = 0
        prefixX = [[0] * n for _ in range(m)]
        prefixY = [[0] * n for _ in range(m)]
        for i in range(m):
            sX = 0
            sY = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    sX += 1
                elif grid[i][j] == 'Y':
                    sY += 1
                prefixX[i][j] = sX + (prefixX[i-1][j] if i > 0 else 0)
                prefixY[i][j] = sY + (prefixY[i-1][j] if i > 0 else 0)
                if prefixX[i][j] > 0 and prefixX[i][j] == prefixY[i][j]:
                    answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["X","Y","."],["Y",".","."]]
        o = 3
        self.assertEqual(s.numberOfSubmatrices(i), o)

    def test_two(self):
        s = Solution()
        i = [["X","X"],["X","Y"]]
        o = 0
        self.assertEqual(s.numberOfSubmatrices(i), o)

    def test_three(self):
        s = Solution()
        i = [[".","."],[".","."]]
        o = 0
        self.assertEqual(s.numberOfSubmatrices(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)