# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise,
    return false.

    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the
    same elements.
    '''
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
        o = True
        self.assertEqual(s.isToeplitzMatrix(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[2,2]]
        o = False
        self.assertEqual(s.isToeplitzMatrix(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)