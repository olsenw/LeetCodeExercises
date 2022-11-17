# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given the coordinate of two rectilinear rectangles in a 2D plane, return the
    total area covered by the two rectangles.
    
    The first rectangle is defined by its bottom-left corner (ax1,ay1) and its
    top-right corner (ax2,ay2).
    
    The second rectangle is defined by its bottom-left corner (bx1,by1) and its
    top-right corner (bx2,by2).
    '''
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # reduce the problem to 1d in x-axis and y-axis
        def computeLength(a,b,c,d):
            # a -> b is line segment 1
            # c -> d is line segment 2
            # contained/equal
            #   a -> c -> d -> b
            #   c -> a -> b -> d
            if a <= c < d <= b or c <= a < b <= d:
                return min(b,d) - max(a,c)
            # partial overlap
            #   a -> c -> b -> d
            #   c -> a -> d -> b
            if a <= c < b <= d or c <= a < d <= b:
                return min(b,d) - max(a,c)
            # no overlap
            #   a -> b ... c -> d
            #   c -> d ... a -> b
            return 0
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - computeLength(ax1, ax2, bx1, bx2) * computeLength(ay1,ay2,by1,by2)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-3,0,3,4,0,-1,9,2]
        o = 45
        self.assertEqual(s.computeArea(*i), o)

    def test_two(self):
        s = Solution()
        i = [-2,-2,2,2,-2,-2,2,2]
        o = 16
        self.assertEqual(s.computeArea(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)