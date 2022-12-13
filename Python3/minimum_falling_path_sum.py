# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an n x n array of integers matrix, return the minimum sum of any
    falling path through matrix.
    
    A falling path starts at any element in the first row and chooses the
    element in the next row that is either directly below or diagonally
    left/right. Specifically, the next element from position (roc,col) will be
    (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
    '''
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1,n):
            pass
            for j in range(n):
                a = matrix[i-1][j-1] if j - 1 >= 0 else 10001
                b = matrix[i-1][j]
                c = matrix[i-1][j+1] if j + 1 < n else 10001
                matrix[i][j] += min(a, b, c)
        return min(matrix[-1])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,1,3],[6,5,4],[7,8,9]]
        o = 13
        self.assertEqual(s.minFallingPathSum(i), o)

    def test_two(self):
        s = Solution()
        i = [[-19,57],[-40,-5]]
        o = -59
        self.assertEqual(s.minFallingPathSum(i), o)

    def test_three(self):
        s = Solution()
        i = [[1]]
        o = 1
        self.assertEqual(s.minFallingPathSum(i), o)

    def test_four(self):
        s = Solution()
        i = [[100] * 100 for _ in range(100)]
        o = 10000
        self.assertEqual(s.minFallingPathSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)