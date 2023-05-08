# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a square matrix mat, return the sum of the matrix diagonals.

    Only include the sum of all the elements on the primary diagonal and all the
    elements on the secondary diagonal that are not part of the primary
    diagonal.
    '''
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = mat[n // 2][n // 2] if n % 2 else 0
        return sum(mat[i][i] for i in range(n)) + sum(mat[n-1-i][i] for i in range(n)) - m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],
             [4,5,6],
             [7,8,9]]
        o = 25
        self.assertEqual(s.diagonalSum(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1,1,1],
             [1,1,1,1],
             [1,1,1,1],
             [1,1,1,1]]
        o = 8
        self.assertEqual(s.diagonalSum(i), o)

    def test_three(self):
        s = Solution()
        i = [[5]]
        o = 5
        self.assertEqual(s.diagonalSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)