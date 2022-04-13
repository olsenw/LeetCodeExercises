# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a positive integer n, generate an n x n matrix filled with
    elements from 1 to n^2 in spiral order.
    '''
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for _ in range(n)]
        i, j = 0, 0
        start, end = 0, n
        num = 1
        while start < end:
            for j in range(start, end):
                m[i][j] = num
                num += 1
            for i in range(start + 1, end):
                m[i][j] = num
                num += 1
            for j in range(end - 2, start - 1, -1):
                m[i][j] = num
                num += 1
            for i in range(end - 2, start, -1):
                m[i][j] = num
                num += 1
            start += 1
            end -= 1
        return m

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = [[1]]
        self.assertEqual(s.generateMatrix(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = [[1,2],[4,3]]
        self.assertEqual(s.generateMatrix(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = [[1,2,3],[8,9,4],[7,6,5]]
        self.assertEqual(s.generateMatrix(i), o)

    def test_four(self):
        s = Solution()
        i = 4
        o = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
        self.assertEqual(s.generateMatrix(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)