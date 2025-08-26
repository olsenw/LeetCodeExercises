# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D 0-indexed integer array dimensions.
    
    For all indices i, o <= i < dimensions.length, dimensions[i][0] represents
    the length and dimensions[i][1] represents the width of the rectangle i.

    Return the area of the rectangle having the longest diagonal. If there are
    multiple rectangles with the longest diagonal, return the area of the
    rectangle having the maximum area.
    '''
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        answer = 0
        diagonal = 0
        for i,j in dimensions:
            d = i * i + j * j
            if diagonal < d:
                diagonal = d
                answer = i * j
            elif diagonal == d:
                answer = max(answer, i * j)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[9,3],[8,6]]
        o = 48
        self.assertEqual(s.areaOfMaxDiagonal(i), o)

    def test_two(self):
        s = Solution()
        i = [[3,4],[4,3]]
        o = 12
        self.assertEqual(s.areaOfMaxDiagonal(i), o)

    def test_three(self):
        s = Solution()
        i = [[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]
        o = 20
        self.assertEqual(s.areaOfMaxDiagonal(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)