# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two integers, x and y, which represent the current position on a
    Cartesian grid: (x,y). Also given is an array points where each
    points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is
    valid if it shares the same x-coordinate or the same y coordinate as the
    current location.

    Return the index (0-indexed) of the valid point with the smallest manhattan
    distance from the current position. If there are multiple return the valid
    point with the smallest index. If there are no valid points, return -1.

    The Manhattan distance between two points (x1, y1) and (x2, y2) is
    abs(x1 - x2) + abs(y1 - y2).
    '''
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def manhattan(a:int,b:int) -> int:
            return abs(x - a) + abs(y - b)
        index = -1
        m = float('inf')
        for i in range(len(points)):
            a,b = points[i]
            if a == x or b == y:
                c = manhattan(a,b)
                if c < m:
                    m = c
                    index = i
        return index

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = 4
        k = [[1,2],[3,1],[2,4],[2,3],[4,4]]
        o = 2
        self.assertEqual(s.nearestValidPoint(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 4
        k = [[3,4]]
        o = 0
        self.assertEqual(s.nearestValidPoint(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 3
        j = 4
        k = [[2,3]]
        o = -1
        self.assertEqual(s.nearestValidPoint(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)