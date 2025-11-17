# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n, indicating that there is an n x n 0-indexed
    integer matrix mat filled with zeros.

    Also given a 2D integer array query. For each
    query[i] = [rowi, coli, row2i, col2i] do the following:
    * Add 1 to every element in the submatrix with the top left corner
      (row1i,col1i) and the bottom right corner (row2i, col2i). That is, add 1
      to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.
    
    Return the matrix mat after performing every query.
    '''
    def rangeAddQueries_fails(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * (n+1) for _ in range(n)]
        for x1,y1,x2,y2 in queries:
            mat[x1][y1] += 1
            mat[x1][y2+1] -= 1
            mat[x2][y1] += 1
            mat[x2][y2+1] -= 1
        print(mat)
        for i in range(n):
            s = 0
            for j in range(n):
                s += mat[i][j]
                mat[i][j] = s
        print(mat)
        return [r[:-1] for r in mat]

    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0] * (n+1) for _ in range(n)]
        for row1,col1,row2,col2 in queries:
            for row in range(row1,row2+1):
                mat[row][col1] += 1
                mat[row][col2+1] -= 1
        for i in range(n):
            for j in range(1,n+1):
                mat[i][j] += mat[i][j-1]
        return [row[:-1] for row in mat]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [[1,1,2,2],[0,0,1,1]]
        o = [[1,1,0],[1,2,1],[0,1,1]]
        self.assertEqual(s.rangeAddQueries(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [[0,0,1,1]]
        o = [[1,1],[1,1]]
        self.assertEqual(s.rangeAddQueries(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)