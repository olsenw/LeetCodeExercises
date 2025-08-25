# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional, Tuple

class Solution:
    '''
    Given an m x n matrix mat, return an array of all the elements of the array
    in a diagonal order.
    '''
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat), len(mat[0])
        answer = []
        def right(i,j) -> Tuple[int,int]:
            while i >= 0 and j < n:
                answer.append(mat[i][j])
                i -= 1
                j += 1
            if j < n:
                i = 0
            if j == n:
                i += 2
                j = n - 1
            return i,j
        def left(i,j) -> Tuple[int,int]:
            while i < m and j >= 0:
                answer.append(mat[i][j])
                i += 1
                j -= 1
            if i < m:
                j = 0
            if i == m:
                i = m - 1
                j += 2
            return i,j
        i,j = 0,0
        while len(answer) < m * n:
            i,j = right(i,j)
            if len(answer) < m * n:
                i,j = left(i,j)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        o = [1,2,4,7,5,3,6,8,9]
        self.assertEqual(s.findDiagonalOrder(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[3,4]]
        o = [1,2,3,4]
        self.assertEqual(s.findDiagonalOrder(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
        o = [1,2,6,11,7,3,4,8,12,13,9,5,10,14,15]
        self.assertEqual(s.findDiagonalOrder(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,2],[3,4],[5,6],[7,8]]
        o = [1,2,3,5,4,6,7,8]
        self.assertEqual(s.findDiagonalOrder(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)