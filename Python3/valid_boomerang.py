# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array points where points[i] = [xi, yi] represents a point on the
    X-Y plane, return true if these points are a boomerang.

    A boomerang is a set of three points that are all distinct and not in a
    straight line.
    '''
    # vertical lines result in a division by zero
    def isBoomerang_fails(self, points: List[List[int]]) -> bool:
        s = set()
        m = set()
        for x,y in points:
            if (x,y) in s:
                return False
            for a,b in s:
                n = (b-y) / (a-x)
                if n in m:
                    return False
                m.add(n)
            s.add((x,y))
        return True

    # geeks for geeks article about determining if points are colinear
    # https://www.geeksforgeeks.org/maths/collinear-points/
    # basically check if triangle has area of zero
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # check for uniqueness
        if len(set((x,y) for x,y in points)) < len(points):
            return False
        # check if points colinear
        for i in range(len(points)-2):
            x1,y1 = points[i]
            for j in range(i+1, len(points)-1):
                x2,y2 = points[j]
                for k in range(j+1, len(points)):
                    x3,y3 = points[k]
                    if x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) == 0:
                        return False
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1],[2,3],[3,2]]
        o = True
        self.assertEqual(s.isBoomerang(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[2,2],[3,3]]
        o = False
        self.assertEqual(s.isBoomerang(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,0],[0,2],[2,1]]
        o = True
        self.assertEqual(s.isBoomerang(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)