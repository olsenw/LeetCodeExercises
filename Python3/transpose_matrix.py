# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a 2D integer array matrix, return the transpose of matrix.

    The transpose of a matrix is the matrix flipped over its main
    diagonal, switching the matrix's row and column indices.
    '''
    def transpose_list(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        return [[matrix[j][i] for j in range(m)] for i in range(n)]

    # works on leetcode (there it does not return tuples in list)
    # * is unpack operator allowing a list to be turned into arguments
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        o = [[1,4,7],[2,5,8],[3,6,9]]
        self.assertEqual(s.transpose(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3],[4,5,6]]
        o = [[1,4],[2,5],[3,6]]
        self.assertEqual(s.transpose(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)