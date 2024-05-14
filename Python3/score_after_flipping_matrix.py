# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n binary matrix grid.

    A move consists of choosing any row or column and toggling each value in
    that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

    Every row of the matrix is interpreted as a binary number, and the score of
    the matrix is the sum of these numbers.

    Return the highest possible socre after making any number of moves
    (including zero moves).
    '''
    def matrixScore(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        for r in range(m):
            if grid[r][0] == 0:
                for c in range(n):
                    grid[r][c] = 0 if grid[r][c] == 1 else 1
        pass
        for c in range(n):
            a = 0
            for r in range(m):
                a += grid[r][c]
            if a < m - a:
                for r in range(m):
                    grid[r][c] = 0 if grid[r][c] == 1 else 1
        answer = 0
        for r in grid:
            a = 0
            for c in r:
                a <<= 1
                a |= c
            answer += a
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
        o = 39
        self.assertEqual(s.matrixScore(i), o)

    def test_two(self):
        s = Solution()
        i = [[0]]
        o = 1
        self.assertEqual(s.matrixScore(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,0,0,0,0],[1,0,0,0,0]]
        o = 1
        self.assertEqual(s.matrixScore(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)