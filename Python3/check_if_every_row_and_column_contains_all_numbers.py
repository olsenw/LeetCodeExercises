# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An n x n matrix is valid if every row and every column contains all the
    integers from 1 to n (inclusive).

    Given an n x n integer matrix matrix, return true if the matrix is valid.
    Otherwise, return false.
    '''
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for r in matrix:
            if len(set(r)) != n:
                return False
        for c in range(n):
            if len(set(matrix[r][c] for r in range(n))) != n:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[3,1,2],[2,3,1]]
        o = True
        self.assertEqual(s.checkValid(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1,1],[1,2,3],[1,2,3]]
        o = False
        self.assertEqual(s.checkValid(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)