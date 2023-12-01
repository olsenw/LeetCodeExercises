# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two n x n binary matrices mat and target, return True if it is
    possible to make mat equal to target by rotating mat in 90-degree
    increments, or false otherwise.
    '''
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rotate(arr):
            return [[mat[j][i] for j in range(n-1,-1,-1)] for i in range(n)]
        def test(a,b):
            for i,j in zip(a,b):
                if i != j:
                    return False
            return True
        if test(mat,target):
            return True
        mat = rotate(mat)
        if test(mat,target):
            return True
        mat = rotate(mat)
        if test(mat,target):
            return True
        mat = rotate(mat)
        if test(mat,target):
            return True
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1],[1,0]]
        j = [[1,0],[0,1]]
        o = True
        self.assertEqual(s.findRotation(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[0,1],[1,1]]
        j = [[1,0],[0,1]]
        o = False
        self.assertEqual(s.findRotation(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[0,0,0],[0,1,0],[1,1,1]]
        j = [[1,1,1],[0,1,0],[0,0,0]]
        o = True
        self.assertEqual(s.findRotation(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)