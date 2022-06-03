# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from itertools import accumulate

'''
Given a 2D matrix matrix, handle multiple queries of the following type:

* Calculate the sum of the elements of matrix inside the rectangle
  defined by its upper left corner (row1, col1) and lower right corner
  (row2, col2).

Implement the NumMatrix class:
'''
class NumMatrix_slow:
    '''
    Initializes the object with the integer matrix matrix.
    '''
    def __init__(self, matrix: List[List[int]]):
        self.matrix = [list(accumulate(i)) for i in matrix]

    '''
    Returns the sum of the elements of matrix inside of rectangle.
    '''
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        minus = 0
        if col1 > 0:
            for i in range(row1, row2 + 1):
                minus += self.matrix[i][col1 - 1]
        plus = 0
        for i in range(row1, row2 + 1):
            plus += self.matrix[i][col2]
        return plus - minus

class NumMatrix:
    '''
    Initializes the object with the integer matrix matrix.
    '''
    def __init__(self, matrix: List[List[int]]):
        self.matrix = [list(accumulate(i)) for i in matrix]
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                self.matrix[i][j] += self.matrix[i - 1][j]

    '''
    Returns the sum of the elements of matrix inside of rectangle.
    '''
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.matrix[row2][col2]
        b = self.matrix[row1 - 1][col2] if row1 else 0
        c = self.matrix[row2][col1 - 1] if col1 else 0
        d = self.matrix[row1 - 1][col1 - 1] if row1 and col1 else 0
        return a - b - c + d

class UnitTesting(unittest.TestCase):
    def test(self):
        m = [[3, 0, 1, 4, 2],
             [5, 6, 3, 2, 1],
             [1, 2, 0, 1, 5],
             [4, 1, 0, 1, 7],
             [1, 0, 3, 0, 5]]
        s = NumMatrix(m)
        self.assertEqual(s.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(s.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(s.sumRegion(1, 2, 2, 4), 12)
        self.assertEqual(s.sumRegion(0, 0, 4, 4), 58)

if __name__ == '__main__':
    unittest.main(verbosity=2)