# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary matrix matrix of size m x n, where it is possible to
    rearrange the columns of the matrix in any order.

    Return the area of the largest submatrix within matrix where every element
    of the submatrix is 1 after reordering the columns optimally.
    '''
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        hint = [[0] * n for _ in range(m)]
        for j in range(n):
            hint[0][j] = matrix[0][j]
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j]:
                    hint[i][j] = 1 + hint[i-1][j]
        def fit(row: list[int]):
            check = sorted(((b,a) for a,b in enumerate(row)), reverse=True)
            x = check[0][0]
            answer = x
            for i in range(n):
                x = min(x, check[i][0])
                answer = max(answer, x * (i + 1))
            return answer
        answer = 0
        for i in range(m):
            answer = max(answer, fit(hint[i]))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0,1],[1,1,1],[1,0,1]]
        o = 4
        self.assertEqual(s.largestSubmatrix(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0,1,0,1]]
        o = 3
        self.assertEqual(s.largestSubmatrix(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,1,0],[1,0,1]]
        o = 2
        self.assertEqual(s.largestSubmatrix(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)