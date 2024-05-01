# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    In MATLAB, there is a handy function called reshape which can reshape an
    m x n matrix into a new one with a different size r x c keeping its original
    data.

    Given an m x n matrix mat and two integers r and c representing the number
    of rows and the number of columns of the wanted reshaped matrix.

    The reshaped matrix should be filled with all the elements of the original
    matrix in the same row-traversing order as they were.

    If the reshape operation with given parameters is possible and legal, output
    the new reshaped matrix; Otherwise, output the original matrix.
    '''
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat
        shape = [[0] * c for _ in range(r)]
        a,b = 0,0
        for i in range(m):
            for j in range(n):
                shape[a][b] = mat[i][j]
                b += 1
                if b == c:
                    a += 1
                    b = 0
        return shape

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[3,4]]
        j = 1
        k = 4
        o = [[1,2,3,4]]
        self.assertEqual(s.matrixReshape(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[3,4]]
        j = 2
        k = 4
        o = [[1,2],[3,4]]
        self.assertEqual(s.matrixReshape(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)