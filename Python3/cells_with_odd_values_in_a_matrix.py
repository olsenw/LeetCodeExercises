# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an m x n matrix that is initialized to all 0's. There is also a 2D
    array indices where each indices[i] = [ri, ci] represents a 0-indexed
    location to perform some increment operations on the matrix.

    For each location indices[i], do both of the following:
    1. Increment all the cells on row ri.
    2. Increment all the cells on column ci.

    Given m, n and indices, return the number of odd-valued cells in the matrix
    after applying the increment to all locations in indices.
    '''
    # O(max(len(indices, m*n))) time
    # O(m + n + m*n) space
    def oddCells_correct(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for i,j in indices:
            rows[i] += 1
            cols[j] += 1
        answer = [[rows[i] + cols[j] for j in range(n)] for i in range(m)]
        s = 0
        for i in range(m):
            for j in range(n):
                s += answer[i][j] % 2
        return s

    # O(m + n + len(indices)) time
    # O(m + n) space
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for i,j in indices:
            rows[i] += 1
            cols[j] += 1
        rodd = sum(i % 2 for i in rows)
        codd = sum(i % 2 for i in cols)
        return (rodd * (n - codd)) + ((m - rodd) * codd)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = 3
        k = [[0,1],[1,1]]
        o = 6
        self.assertEqual(s.oddCells(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = 2
        k = [[1,1],[0,0]]
        o = 0
        self.assertEqual(s.oddCells(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)