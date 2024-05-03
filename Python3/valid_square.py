# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given the coordinates of four points in 2D space, p1, p2, p3, and p4, return
    true if the four points construct a square.

    The coordinate of a point pi is represented as [xi, yi]. The input is not
    given in any order.

    A valid square has four equal sides with positive length and four equal
    angles (90-degree angles).
    '''
    # does not account for rotated squares
    def validSquare_fails(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p1,p2,p3,p4 = sorted([p1,p2,p3,p4])
        if not (p1[0] == p2[0] and p1[1] == p3[1]):
            return False
        if not (p4[0] == p3[0] and p4[1] == p2[1]):
            return False
        if not (p3[0] - p1[0] > 0 and p3[0] - p1[0] == p4[0] - p2[0] == p2[1] - p1[1] == p4[1] - p3[1]):
            return False
        return True

    # Pythagorean Theorem a^2 + b^2 = c^2 for a right triangle
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p1,p2,p3,p4 = sorted([p1,p2,p3,p4])
        # triangle one p1,p2,p3 (p1 is 90 degree, others are 45)
        a = (p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1])
        b = (p3[0] - p1[0]) * (p3[0] - p1[0]) + (p3[1] - p1[1]) * (p3[1] - p1[1])
        c = (p3[0] - p2[0]) * (p3[0] - p2[0]) + (p3[1] - p2[1]) * (p3[1] - p2[1])
        if a + b != c or a != b:
            return False
        # triangle two p2,p3,p4 (p4 is 90 degree, others are 45)
        e = (p4[0] - p3[0]) * (p4[0] - p3[0]) + (p4[1] - p3[1]) * (p4[1] - p3[1])
        f = (p4[0] - p2[0]) * (p4[0] - p2[0]) + (p4[1] - p2[1]) * (p4[1] - p2[1])
        g = (p3[0] - p2[0]) * (p3[0] - p2[0]) + (p3[1] - p2[1]) * (p3[1] - p2[1])
        if e + f != g or e != f:
            return False
        # check if hypotenuse are equal
        if c != g:
            return False
        # check if two sides are equal and greater than zero
        if a != e or a == 0:
            return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0],[1,1],[1,0],[0,1]]
        o = True
        self.assertEqual(s.validSquare(*i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0],[1,1],[1,0],[0,12]]
        o = False
        self.assertEqual(s.validSquare(*i), o)

    def test_three(self):
        s = Solution()
        i = [[1,0],[-1,0],[0,1],[0,-1]]
        o = True
        self.assertEqual(s.validSquare(*i), o)

    def test_four(self):
        s = Solution()
        i = [[0,0],[1,0],[0,2],[1,2]]
        o = False
        self.assertEqual(s.validSquare(*i), o)

    def test_five(self):
        s = Solution()
        i = [[0,0],[0,0],[0,0],[0,0]]
        o = False
        self.assertEqual(s.validSquare(*i), o)

    def test_six(self):
        s = Solution()
        i = [[0,0],[1,0],[2,0],[3,0]]
        o = False
        self.assertEqual(s.validSquare(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)