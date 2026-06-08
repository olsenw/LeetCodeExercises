# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array matrix of size n x n representing the adjacency
    matrix of an undirected graph with n vertices labeled from 0 to n-1.
    * matrix[i][j] = 1 indicates that there is an edge between vertices i and j.
    * matrix[i][j] = 0 indicates that there is no edge between vertices i and j.

    The degree of a vertex is the number of edges connected to it.

    Return an integer array ans of size n where ans[i] represents the degree of
    vertex i.
    '''
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(matrix[i]) for i in range(len(matrix))]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,1],[1,0,1],[1,1,0]]
        o = [2,2,2]
        self.assertEqual(s.findDegrees(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,1,0],[1,0,0],[0,0,0]]
        o = [1,1,0]
        self.assertEqual(s.findDegrees(i), o)

    def test_three(self):
        s = Solution()
        i = [[0]]
        o = [0]
        self.assertEqual(s.findDegrees(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)