# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n matrix mat and an integer threshold, return the maximum
    side-length of a square with a sum less than or equal to threshold or return
    0 if there is no such square.
    '''
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if not any(any(c <= threshold for c in r) for r in mat):
            return 0
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1,n):
                mat[i][j] += mat[i][j-1]
        pass
        for i in range(1,m):
            for j in range(n):
                mat[i][j] += mat[i-1][j]
        pass
        def possible(side:int) -> bool:
            for i in range(m - side + 1):
                for j in range(n - side + 1):
                    a = mat[i+side-1][j+side-1]
                    if i > 0:
                        a -= mat[i-1][j+side-1]
                    if j > 0:
                        a -= mat[i+side-1][j-1]
                    if i > 0 and j > 0:
                        a += mat[i-1][j-1]
                    if a <= threshold:
                        return True
            return False
        i,j = 1,min(m,n)
        while i < j:
            k = (i + j) // 2 + (i + j) % 2
            if possible(k):
                i = k
            else:
                j = k - 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
        j = 4
        o = 2
        self.assertEqual(s.maxSideLength(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
        j = 1
        o = 0
        self.assertEqual(s.maxSideLength(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]]
        j = 40184
        o = 2
        self.assertEqual(s.maxSideLength(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)