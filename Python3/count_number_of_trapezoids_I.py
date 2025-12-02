# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array points, where points[i] = [xi, yi] represents the
    coordinates of the ith point on the Cartesian plane.

    A horizontal trapezoid is a convex quadrilateral with at least one pair of
    horizontal sides (ie parallel to the x-axis). Two lines are parallel if and
    only if they have the same slope.

    Return the number of unique horizontal trapezoids that can be formed by
    choosing any four distinct points from points.

    Since the answer may be very large, return it modulo 10**9 + 7.
    '''
    def countTrapezoids_tle(self, points: List[List[int]]) -> int:
        m = 10**9 + 7
        horizontal = defaultdict(list)
        for x,y in points:
            horizontal[y].append(x)
        # rows = sorted(h for h in horizontal if len(horizontal[h] > 1))
        rows = [math.comb(len(horizontal[h]),2) for h in horizontal if len(horizontal[h]) > 1]
        answer = 0
        for i in range(len(rows)):
            for j in range(i+1, len(rows)):
                a = (rows[i] % m * rows[j] % m) % m
                answer = (answer % m + a % m) % m
        return answer

    def countTrapezoids_tle2(self, points: List[List[int]]) -> int:
        m = 10**9+7
        horizontal = Counter()
        for _,y in points:
            horizontal[y] += 1
        horizontal = [math.comb(horizontal[h], 2) for h in horizontal if horizontal[h] > 1]
        answer = 0
        for i in range(len(horizontal)):
            for j in range(i + 1, len(horizontal)):
                a = (horizontal[i] % m * horizontal[j] % m) % m
                answer = (answer % m + a % m) % m
        return answer

    def countTrapezoids(self, points: List[List[int]]) -> int:
        m = 10**9+7
        horizontal = Counter()
        for _,y in points:
            horizontal[y] += 1
        horizontal = [math.comb(horizontal[h], 2) for h in horizontal if horizontal[h] > 1]
        s = sum(horizontal)
        answer = 0
        for i in range(len(horizontal)):
            s -= horizontal[i]
            a = (horizontal[i] % m * s % m) % m
            answer = (answer % m + a % m) % m
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0],[2,0],[3,0],[2,2],[3,2]]
        o = 3
        self.assertEqual(s.countTrapezoids(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0],[1,0],[0,1],[2,1]]
        o = 1
        self.assertEqual(s.countTrapezoids(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,0],[2,0],[3,0],[1,2],[2,2],[3,2]]
        o = 9
        self.assertEqual(s.countTrapezoids(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)