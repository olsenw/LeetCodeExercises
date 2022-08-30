# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an n x n 2D matrix representing an image, rotate the image by
    90 degrees (clockwise).

    Rotate the image in-place, do not allocate another 2D matrix for the
    rotation.
    '''
    def rotate_illegal(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        mat = [[0] * n for _ in range(n)]
        for a, i in zip(reversed(range(n)), range(n)):
            for b, j in zip(range(n), range(n)):
                mat[b][a] = matrix[i][j]
        # matrix = mat
        for i in range(n):
            for j in range(n):
                matrix[i][j] = mat[i][j]

    # rotate sets of four numbers
    # very finicky logic...
    # needed solution for help on details
    def rotate_direct(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-j-1]
                matrix[n-1-i][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = matrix[i][j]
                matrix[i][j] = temp

    # read solution for how to transpose and reflect
    def rotate_linear_algebra(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # rows become columns
        def transpose(mat):
            for i in range(n):
                for j in range(i + 1, n):
                    # swap
                    mat[j][i], mat[i][j] = mat[i][j], mat[j][i]
        # flips left to right
        def reflect(mat):
            for i in range(n):
                for j in range(n // 2):
                    # swap
                    mat[i][j], mat[i][-j-1] = mat[i][-j-1], mat[i][j]
        transpose(matrix)
        reflect(matrix)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        s.rotate(i)
        o = [[7,4,1],[8,5,2],[9,6,3]]
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        s.rotate(i)
        o = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)