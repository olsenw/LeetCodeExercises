# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a convex n-sided polygon where each vertex has an integer value. Also
    given an integer array values where values[i] is the value of the ith vertex
    in clockwise order.

    Polygon triangulation is a process where a polygon is divided into a set of
    triangles and the vertices of each triangle must also be vertices of the
    original polygon. Note that no other shapes other than triangles are allowed
    in the division. This process with result in n - 2 triangles.

    Triangulate the polygon. For each triangle, the weight of that triangle is
    the product of the values at its vertices. The total score of the
    triangulation is the sum of these weights over all n - 2 triangles.

    Return the minimum possible score that can be achieved with some
    triangulation of the polygon.
    '''
    # having trouble figuring out the indices and how to divide
    def minScoreTriangulation_stalled_out(self, values: List[int]) -> int:
        n = len(values)
        @cache
        def dp(i:int,j:int):
            if j - i + 1 == 3:
                return values[i] * values[i-1] * values[j]
            if j - i + 1 < 3:
                return 0
            answer = float('inf')
            for a in range(i,j+1):
                b = a + 1 if a < j else i
                for c in range(b+1,j+1):
                    t = values[a] * values[b] + values[c]
                    answer = min(answer, t)
                for c in range(i, a):
                    t = values[a] * values[b] + values[c]
                    answer = min(answer, t)
            return answer
        return dp(0, n-1)

    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        @cache
        def dp(i:int, j:int) -> int:
            if j - i + 1 == 3:
                return values[i] * values[i+1] * values[j]
            if j - i + 1 < 3:
                return 0
            answer = float('inf')
            for k in range(i+1, j):
                t = values[i] * values[k] * values[j]
                a = t + dp(i,k) + dp(k,j)
                answer = min(answer, a)
            return answer
        return dp(0, n-1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = 6
        self.assertEqual(s.minScoreTriangulation(i), o)

    def test_two(self):
        s = Solution()
        i = [3,7,4,5]
        o = 144
        self.assertEqual(s.minScoreTriangulation(i), o)

    def test_three(self):
        s = Solution()
        i = [1,3,1,4,1,5]
        o = 13
        self.assertEqual(s.minScoreTriangulation(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)