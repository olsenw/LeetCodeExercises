# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array coordinates, coordinates[i] = [x, y] where [x,y] is
    represents the coordinate of a point. Check if these points make a straight
    line in the XY plane.
    '''
    # dumb implementation (passes tests)
    def checkStraightLine_passes(self, coordinates: List[List[int]]) -> bool:
        # y = m x + b
        a,b = coordinates[0]
        c,d = coordinates[-1]
        if c - a == 0:
            for x,y in coordinates:
                if x != a:
                    return False
            return True
        slope = (d - b) / (c - a) 
        intercept = b - slope * a
        for x,y in coordinates:
            test = slope * x + intercept - y
            if test < -0.0005 or test > 0.0005:
                return False
        return True

    # based on leetcode solution
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        rise = coordinates[1][1] - coordinates[0][1]
        run = coordinates[1][0] - coordinates[0][0]
        for i in range(2, len(coordinates)):
            a = coordinates[i][1] - coordinates[0][1]
            b = coordinates[i][0] - coordinates[0][0]
            if a * run != b * rise:
                return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
        o = True
        self.assertEqual(s.checkStraightLine(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
        o = False
        self.assertEqual(s.checkStraightLine(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,0],[0,1],[0,-1]]
        o = True
        self.assertEqual(s.checkStraightLine(i), o)

    def test_four(self):
        s = Solution()
        i = [[2,4],[2,5],[2,8]]
        o = True
        self.assertEqual(s.checkStraightLine(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)