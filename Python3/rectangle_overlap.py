# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An axis-aligned rectangle is represented as a list [x1, y1, x2, y2] where
    (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the
    coordinate of its top-right corner. Its top and bottom edges are parallel to
    the X-axis, and its left and right edges are parallel to the Y-axis.

    Two rectangles overlap if the area of their intersection is positive. To be
    clear, two rectangles that only touch at the corner or edges do not overlap.

    Given two axis-aligned rectangles rec1 and rec2, return true if they
    overlap, otherwise return false.
    '''
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2 = rec1
        a1,b1,a2,b2 = rec2
        # return (a <= w < b or w <= b < x) and (c <= y < d or y <= c < z)
        return (x1 <= a1 < x2 or a1 <= x1 < a2) and (y1 <= b1 < y2 or b1 <= y1 < b2)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,0,2,2]
        j = [1,1,3,3]
        o = True
        self.assertEqual(s.isRectangleOverlap(i,j), o)

    def test_two(self):
        s = Solution()
        i = [0,0,1,1]
        j = [1,0,2,1]
        o = False
        self.assertEqual(s.isRectangleOverlap(i,j), o)

    def test_three(self):
        s = Solution()
        i = [0,0,1,1]
        j = [2,2,3,3]
        o = False
        self.assertEqual(s.isRectangleOverlap(i,j), o)

    def test_four(self):
        s = Solution()
        i = [7,8,13,15]
        j = [10,8,12,20]
        o = True
        self.assertEqual(s.isRectangleOverlap(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)