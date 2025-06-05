# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of points on the X-Y plane points where points[i] = [xi, yi],
    return the area of the largest triangle that can be formed by any
    three-different points. Answers withing 10^-5 of the actual answer will be
    accepted.
    '''
    # math is sensitive and will be inaccurate
    def largestTriangleArea_sensitive(self, points: List[List[int]]) -> float:
        def distance(a:List[int], b:List[int]) -> float:
            x = b[0] - a[0]
            y = b[1] - a[1]
            return math.sqrt(x * x + y * y)
        def area(a:List[int], b:List[int], c:List[int]) -> float:
            s = sorted([distance(a,b), distance(a,c), distance(b,c)])
            return (s[0] * s[1]) / 2
        n = len(points)
        answer = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    answer = max(answer, area(points[i], points[j], points[k]))
        return answer

    # https://www.mathopenref.com/coordtrianglearea.html
    def largestTriangleArea(self, points: List[List[int]]) -> int:
        n = len(points)
        answer = 0.0
        for i in range(n):
            ax, ay = points[i]
            for j in range(i + 1, n):
                bx, by = points[j]
                for k in range(j + 1, n):
                    cx, cy = points[k]
                    area = abs((ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) / 2)
                    answer = max(answer, area)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0],[0,1],[1,0],[0,2],[2,0]]
        o = 2.0
        self.assertEqual(s.largestTriangleArea(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0],[0,0],[0,1]]
        o = 0.5
        self.assertEqual(s.largestTriangleArea(i), o)

    def test_three(self):
        s = Solution()
        i = [[4,6],[6,5],[3,1]]
        o = 5.5
        self.assertEqual(s.largestTriangleArea(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)