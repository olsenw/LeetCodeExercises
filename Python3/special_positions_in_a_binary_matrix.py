# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n binary matrix mat, return the number of special positions in
    mat.

    A position (i, j) is called special if mat[i][j] == 1 and all other elements
    in row i and column j are 0 (rows and columns are 0-indexed).
    '''
    def numSpecial(self, mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        a = list(sum(m) for m in mat)
        b = list(sum(m) for m in zip(*mat))
        answer = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] and a[i] == b[j] == 1:
                    answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0,0],[0,0,1],[1,0,0]]
        o = 1
        self.assertEqual(s.numSpecial(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0,0],[0,1,0],[0,0,1]]
        o = 3
        self.assertEqual(s.numSpecial(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]
        o = 2
        self.assertEqual(s.numSpecial(i), o)

    def test_four(self):
        s = Solution()
        i = [[0,0],[0,0],[1,0]]
        o = 1
        self.assertEqual(s.numSpecial(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)