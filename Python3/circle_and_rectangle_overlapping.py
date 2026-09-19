# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a circle represented as (radius, xCenter, yCenter) and an axis aligned
    rectangle represented as (x1,y1,x2,y2), where (x1,y1) are the coordinates of
    the bottom-left corner, and (2,y2) are the coordinates of the top-right
    corner of the rectangle.

    Return true if the circle and rectangle are overlapped otherwise return
    false. In other words, check if there is any point (xi, yi) that belongs to 
    the circle and the rectangle at the same time.
    '''
    def checkOverlap_incomplete(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # recenter the problem so circle is at the origin
        x1 -= xCenter
        x2 -= xCenter
        y1 -= yCenter
        y2 -= yCenter
        # find which side of rectangle is closer to circle
        favorLeft = abs(x1) <= abs(x2)
        favorDown = abs(y1) <= abs(y2)
        a = x1,y1
        b = x2,y2
        # fancy math from wolfram MathWorld
        # https://mathworld.wolfram.com/Circle-LineIntersection.html
        drSquared = (b[0]-a[0])**2 - (b[1]-a[1])**2
        D = a[0] * b[1] - b[0] * a[1]
        discriminant = radius**2
        return

    def checkOverlap_parameterized(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # parameterized equation for circle
        # x = h + r cos t
        # y = k + r sin t
        # where t is the parameter [0,2π], (h,k) is center of circle, r is the radius
        return

    # only works when square is fully contained in a quadrant
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # recenter the problem so circle is at the origin
        x1 -= xCenter
        x2 -= xCenter
        y1 -= yCenter
        y2 -= yCenter
        # if crosses x axis and crosses y axis default in circle
        if x1 <= 0 <= x2 and y1 <= 0 <= y2:
            return True
        # if crosses y axis and close enough to x axis
        if x1 <= 0 <= x2:
            if abs(y1) <= radius or abs(y2) <= radius:
                return True
            return False
        # if crosses x axis 
        if y1 <= 0 <= y2:
            if abs(x1) <= radius or abs(x2) <= radius:
                return True
            return False
        radius *= radius
        # distance two points
        # d = sqrt((x2-x1)^2 + (y2-y1)^2)
        # so radius^2 >= (x2-x1)^2 + (y2-y1)^2
        # try solving for x or y 
        x = x1 if abs(x1) <= abs(x2) else x2
        y = y1 if abs(y1) <= abs(y2) else y2
        return radius >= x*x + y*y

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1,0,0,1,-1,3,1
        o = True
        self.assertEqual(s.checkOverlap(*i), o)

    def test_two(self):
        s = Solution()
        i = 1,1,1,1,-3,2,-1
        o = False
        self.assertEqual(s.checkOverlap(*i), o)

    def test_three(self):
        s = Solution()
        i = 1,0,0,-1,0,0,1
        o = True
        self.assertEqual(s.checkOverlap(*i), o)

    def test_four(self):
        s = Solution()
        i = 4,8,2,0,0,1,5
        o = False
        self.assertEqual(s.checkOverlap(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)