# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a m x n matrix of ones and zeros, return how many square submatrices
    have all ones.
    '''
    # idea was to brute force calc all square sizes
    def countSquares_incomplete(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        for square in range(1,min(m,n)):
            s = 0
            for i in range(m):
                for j in range(n):
                    pass
                    # for x,y
        return

    # based on LeetCode solution
    # https://leetcode.com/problems/count-square-submatrices-with-all-ones/editorial/?envType=daily-question&envId=2024-10-27
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        @cache
        def solve(i:int,j:int) -> int:
            if i >= m or j >= n:
                return 0
            if matrix[i][j] == 0:
                return 0
            right = solve(i, j+1)
            diag = solve(i+1,j+1)
            down = solve(i+1,j)
            return 1 + min(right, diag, down)
        return sum(solve(i,j) for i in range(m) for j in range(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [
            [0,1,1,1],
            [1,1,1,1],
            [0,1,1,1]
        ]
        o = 15
        self.assertEqual(s.countSquares(i), o)

    def test_two(self):
        s = Solution()
        i = [
            [1,0,1],
            [1,1,0],
            [1,1,0]
        ]
        o = 7
        self.assertEqual(s.countSquares(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)