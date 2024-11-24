# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an n x n integer matrix. The following operation can be performed any
    number of times:
    * Choose any two adjacent elements of matrix and multiply each of them by
      -1.
    
    Two elements are considered adjacent if and only if they share a border.

    Maximize the summation of the matrix's elements after using the operation.
    '''
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        s = sum(sum(abs(i) for i in r) for r in matrix)
        m = min(min(abs(i) for i in r) for r in matrix)
        if m == 0:
            return s
        n = sum(sum(i < 0 for i in r) for r in matrix)
        return s - m - m if n % 2 else s
        # z = any(any(i == 0 for i in r) for r in matrix)
        # if z:
        #     return s
        # n = sum(sum(i < 0 for i in r) for r in matrix)
        # if n % 2:
        #     m = max(max((i for i in r if i < 0), default=-10**5-1) for r in matrix)
        #     return s + m + m
        # return s
        # return s + m if n % 2 else s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,-1],[-1,1]]
        o = 4
        self.assertEqual(s.maxMatrixSum(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3],[-1,-2,-3],[1,2,3]]
        o = 16
        self.assertEqual(s.maxMatrixSum(i), o)

    def test_three(self):
        s = Solution()
        i = [[-1,0,-1],[-2,1,3],[3,2,2]]
        o = 15
        self.assertEqual(s.maxMatrixSum(i), o)

    def test_four(self):
        s = Solution()
        i = [[2,9,3],[5,4,-4],[1,7,1]]
        o = 34
        self.assertEqual(s.maxMatrixSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)