# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n integer matrix mat and an integer k. The matrix rows are
    0-indexed.

    The following process happens k times:
    * Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
    * Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.

    Return true if the final modified matrix after k steps is identical to the
    original matrix and false otherwise.
    '''
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m,n = len(mat), len(mat[0])
        answer = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i % 2 == 1:
                    answer[i][j] = mat[i][(j - k) % n]
                else:
                    answer[i][j] = mat[i][(j + k) % n]
        return answer == mat

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        j = 4
        o = False
        self.assertEqual(s.areSimilar(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
        j = 2
        o = True
        self.assertEqual(s.areSimilar(i,j), o)

    def test_thee(self):
        s = Solution()
        i = [[2,2],[2,2]]
        j = 3
        o = True
        self.assertEqual(s.areSimilar(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)