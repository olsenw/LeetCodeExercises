# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    On a 2D plane, there are n points with integer coordinates
    points[i] = [xi, yi]. Return the minimum time in seconds to visit all the
    points in the order given by points.

    Movement can be done using the following rules:
    * In 1 second:
      * move vertically by one unit
      * move diagonally sqrt(2) units
      * move horizontally by one unit
    * Points must be visited in the order they appear in the array.
    * It is possible to pass through points that appear later in the order, but
      doing so does not count as visiting the point.
    '''
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def d(a,b):
            x = abs(a[0] - b[0])
            y = abs(a[1] - b[1])
            return max(x,y)
        return sum(d(i,j) for i,j in zip(points, points[1:]))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1],[3,4],[-1,0]]
        o = 7
        self.assertEqual(s.minTimeToVisitAllPoints(i), o)

    def test_two(self):
        s = Solution()
        i = [[3,2],[-2,2]]
        o = 5
        self.assertEqual(s.minTimeToVisitAllPoints(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)