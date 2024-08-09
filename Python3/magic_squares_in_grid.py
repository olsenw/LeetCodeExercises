# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to
    9 such that each row, column, and both diagonals all have the same sum.

    Given a row x col grid of integers, how many 3 x 3 contiguous magic square
    subgrids are there?

    Note: while a magic square can only contain numbers from 1 to 9, grid may
    contain numbers up to 15.
    '''
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        magic = [0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0]
        answer = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                m = [0] * 16
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        m[grid[x][y]] += 1
                x,y = i,j
                if (m == magic and 
                    grid[x][y] + grid[x][y+1] + grid[x][y+2] ==
                    grid[x+1][y] + grid[x+1][y+1] + grid[x+1][y+2] ==
                    grid[x+2][y] + grid[x+2][y+1] + grid[x+2][y+2] ==
                    grid[x][y] + grid[x+1][y] + grid[x+2][y] ==
                    grid[x][y+1] + grid[x+1][y+1] + grid[x+2][y+1] ==
                    grid[x][y+2] + grid[x+1][y+2] + grid[x+2][y+2] ==
                    grid[x][y] + grid[x+1][y+1] + grid[x+2][y+2] ==
                    grid[x+2][y] + grid[x+1][y+1] + grid[x][y+2]
                ):
                    answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
        o = 1
        self.assertEqual(s.numMagicSquaresInside(i), o)

    def test_two(self):
        s = Solution()
        i = [[8]]
        o = 0
        self.assertEqual(s.numMagicSquaresInside(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)