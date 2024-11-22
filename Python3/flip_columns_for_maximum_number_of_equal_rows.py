# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n binary matrix.

    Choose any number of columns in the matrix and flip every cell in that
    column (ie, Change the value of the cell from 0 to 1 or vice versa).

    Return the maximum number of rows that have all values equal after some
    number of flips.
    '''
    def maxEqualRowsAfterFlips_brute_fail(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        rows = [0] * len(m)
        for r in len(m):
            for c in len(n):
                if matrix[r][c] == 1:
                    rows[r] += 1 << c
        for k in range(1 << n):
            c = Counter()
            pass
        return

    # took a bit to understand what hint was saying
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        c = Counter()
        for i in matrix:
            number = 0
            for j in range(n):
                if i[j] == 1:
                    number += 1 << j
            c[number] += 1
        answer = 0
        mask = (1 << n) - 1
        for i in c:
            answer = max(answer, c[i] + c[(~i & mask)])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[1,1]]
        o = 1
        self.assertEqual(s.maxEqualRowsAfterFlips(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,1],[1,0]]
        o = 2
        self.assertEqual(s.maxEqualRowsAfterFlips(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,0,0],[0,0,1],[1,1,0]]
        o = 2
        self.assertEqual(s.maxEqualRowsAfterFlips(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)