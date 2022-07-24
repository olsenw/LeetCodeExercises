# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import bisect

class Solution:
    '''
    Write an efficient algorithm that searches for a value target in an
    m x n integer matrix. This matrix has the following properties:
    * Integers in each row are sorted in ascending order from left to
      right
    * Integers in each column are sorted in ascending order from top to
      bottom.
    '''
    # O(n^2)
    def searchMatrix_brute(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)

    # O(n log n)
    def searchMatrix_repeated_binary_search(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            i = bisect.bisect_left(row, target)
            if i < len(row) and row[i] == target:
                return True
        return False

    # O(m + n)
    # based on insight from karan_8082
    # https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/2324351/PYTHON-oror-EXPLAINED-oror
    # due to how matrix is sorted can determine how to progress
    def searchMatrix_linear(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        j = 0
        # iterate while within bounds of array
        while i >= 0 and j < len(matrix[0]):
            # found
            if matrix[i][j] == target:
                return True
            # value is greater so must be up
            elif matrix[i][j] > target:
                i -= 1
            # value is lesser so must be right
            else:
                j += 1
        return False

    '''
    There appear to be faster solutions that seem to be a variation on
    binary search. Where the binary search is done in two dimensions.

    Copied here for own notes
    https://leetcode.com/submissions/api/detail/240/python3/182/
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(row_start, col_start, row_end, col_end):
            if row_start > row_end or col_start > col_end:
                return False

            row_mid, col_mid = (row_start + row_end) // 2, (col_start + col_end) // 2
            pivot = matrix[row_mid][col_mid]
            if target == pivot:
                return True
            
            if_exist = False
            if target > pivot:
                if_exist = if_exist or search(row_mid + 1, col_mid + 1, row_end, col_end)
                if_exist = if_exist or search(row_start, col_mid + 1, row_mid, col_end)
                if_exist = if_exist or search(row_mid + 1, col_start, row_end, col_mid)    
            else:
                if_exist = if_exist or search(row_start, col_start, row_mid-1, col_mid-1)
                if_exist = if_exist or search(row_start, col_mid, row_mid-1, col_end)
                if_exist = if_exist or search(row_mid, col_start, row_end, col_mid-1) 
            
            return if_exist
        
        return search(0, 0, len(matrix)-1, len(matrix[0])-1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
        j = 5
        o = True
        self.assertEqual(s.searchMatrix(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
        j = 20
        o = False
        self.assertEqual(s.searchMatrix(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)