# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A matrix diagonal is a diagonal line of cells starting from some
    cell in either the topmost row or leftmost column and going in the
    bottom-right direction until reaching the matrix's end.

    Given an m x n matrix mat of integers sort each matrix diagonal in
    ascending order and return the resulting matrix.
    '''
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        # for r in mat:
        #     print(r)
        # print("sorting - left column")
        for i in reversed(range(m)):
            a = []
            k = i
            for j in range(n):
                if k == m:
                    break
                a.append(mat[k][j])
                k += 1
            a.sort()
            k = i
            for j in range(len(a)):
                mat[k][j] = a[j]
                k += 1
        # for r in mat:
        #     print(r)
        # print("sorting - top row")
        for j in range(1,n):
            a = []
            k = j
            for i in range(m):
                if k == n:
                    break
                a.append(mat[i][k])
                k += 1
            a.sort()
            k = j
            for i in range(len(a)):
                mat[i][k] = a[i]
                k += 1
        # for r in mat:
        #     print(r)
        return mat

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
        o = [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
        self.assertEqual(s.diagonalSort(i), o)

    def test_two(self):
        s = Solution()
        i = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
        o = [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
        self.assertEqual(s.diagonalSort(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)