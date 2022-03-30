# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Write an efficient algorithm that searches for a value target in an
    m x n integer matrix. This matrix has the following properties:
    * Integers in each row are sorted from left to right.
    * The first integer of each row is greater than the last integer of 
      the previous row.
    '''
    # two binary searches
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        while i < j:
            m = (i + j) // 2
            if matrix[m][-1] < target:
                i = m + 1
            else:
                j = m
        r = i
        i = 0
        j = len(matrix[0]) - 1
        while i < j:
            m = (i + j) // 2
            if matrix[r][m] < target:
                i = m + 1
            else:
                j = m
        return matrix[r][i] == target

    # treat 2d array as single flattened array
    def searchMatrix_flatten(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        i = 0
        j = width * height - 1
        while i < j:
            m = (i + j) // 2
            r = m // width
            c = m % width
            if matrix[r][c] < target:
                i = m + 1
            else:
                j = m
        r = i // width
        c = i % width
        return matrix[r][c] == target

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        j = 3
        o = True
        self.assertEqual(s.searchMatrix(i,j), o)
        self.assertEqual(s.searchMatrix_flatten(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        j = 13
        o = False
        self.assertEqual(s.searchMatrix(i,j), o)
        self.assertEqual(s.searchMatrix_flatten(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[1]]
        j = 2
        o = False
        self.assertEqual(s.searchMatrix(i,j), o)
        self.assertEqual(s.searchMatrix_flatten(i,j), o)

    def test_four(self):
        s = Solution()
        i = [[1]]
        j = 1
        o = True
        self.assertEqual(s.searchMatrix(i,j), o)
        self.assertEqual(s.searchMatrix_flatten(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)