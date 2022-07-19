# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer numRows, return the first numRows of Pascal's
    triangle.

    In Pascal's triangle each number is the sum of the two numbers
    directly above it.

    Leetcode has a neat animated graphic.
    '''
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[1]]
        for i in range(1, numRows):
            a.append([1] + [a[i-1][j] + a[i-1][j+1] for j in range(i-1)] + [1])
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        o = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        self.assertEqual(s.generate(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = [[1]]
        self.assertEqual(s.generate(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)