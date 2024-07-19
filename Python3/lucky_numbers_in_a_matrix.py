# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n matrix of distinct numbers, return all lucky numbers in the
    matrix in any order.

    A lucky number is an element of the matrix such that it is the minimum
    element in its row and maximum in its column.
    '''
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        small = [min(i) for i in matrix]
        big = [max(matrix[i][j] for i in range(m)) for j in range(n)]
        return [matrix[i][j] for i in range(m) for j in range(n) if matrix[i][j] == big[j] and matrix[i][j] == small[i]]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[3,7,8],[9,11,13],[15,16,17]]
        o = [15]
        self.assertEqual(s.luckyNumbers(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
        o = [12]
        self.assertEqual(s.luckyNumbers(i), o)

    def test_three(self):
        s = Solution()
        i = [[7,8],[1,2]]
        o = [7]
        self.assertEqual(s.luckyNumbers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)