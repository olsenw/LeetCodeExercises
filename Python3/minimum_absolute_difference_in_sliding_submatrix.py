# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n integer matrix grid and an integer k.

    For every contiguous k x k submatrix of grid, compute the minimum absolute
    difference between any two distinct values within that submatrix.

    Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is
    the minimum absolute difference in the submatrix whose top-left corner is
    (i,j) in grid.

    Note: If all elements in the submatrix have the same value, the answer will
    be 0.

    A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all
    cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.
    '''
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        answer = []
        for i in range(m-k+1):
            answer.append([])
            for j in range(n-k+1):
                s = set()
                for x in range(k):
                    for y in range(k):
                        s.add(grid[i+x][j+y])
                s = sorted(s)
                a = 10**6
                for z in range(len(s)-1):
                    a = min(a,abs(s[z] - s[z+1]))
                answer[i].append(a if len(s) > 1 else 0)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,8],[3,-2]]
        j = 2
        o = [[2]]
        self.assertEqual(s.minAbsDiff(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[3,-1]]
        j = 1
        o = [[0,0]]
        self.assertEqual(s.minAbsDiff(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[1,-2,3],[2,3,5]]
        j = 2
        o = [[1,2]]
        self.assertEqual(s.minAbsDiff(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)