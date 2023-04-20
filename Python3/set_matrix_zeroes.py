# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    # O(n) space for the set
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        marked = set()
        for i in range(m):
            clear = False
            for j in range(n):
                if matrix[i][j] == 0:
                    for x in range(i):
                        matrix[x][j] = 0
                    for y in range(j):
                        matrix[i][y] = 0
                    clear = True
                    marked.add(j)
                if clear or j in marked:
                    matrix[i][j] = 0

    # O(1) space LeetCode
    # https://leetcode.com/problems/set-matrix-zeroes/editorial/
    # mark left column and top row as flag for zeroing
    def setZeroes_leet(self, matrix: List[List[int]]) -> None:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,1],[1,0,1],[1,1,1]]
        o = [[1,0,1],[0,0,0],[1,0,1]]
        s.setZeroes(i)
        self.assertEqual(i, o)


    def test_two(self):
        s = Solution()
        i = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        o = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
        s.setZeroes(i)
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)