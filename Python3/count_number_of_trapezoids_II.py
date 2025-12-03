# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import math
import sys
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array points where points[i] = [xi, yi] represents the
    coordinates of the ith point on the Cartesian plane.

    Return the number of unique trapezoids that can be formed by choosing any
    four distinct points from points.

    A trapezoid is a convex quadrilateral with at least one pair of parallel
    sides. Two lines are parallel if and only if they have the same slope.
    '''
    # does not account for colinear line segments
    def countTrapezoids_fails(self, points: List[List[int]]) -> int:
        # m = (y2 - y1) / (x2 - x1)
        slopes = Counter()
        for i in range(len(points)):
            x,y = points[i]
            for j in range(i + 1, len(points)):
                a,b = points[j]
                if x - a == 0:
                    slopes[(sys.maxsize, sys.maxsize)] += 1
                    continue
                slopes[divmod(y - b, x - a)] += 1
        answer = 0
        for i in slopes:
            answer += math.comb(slopes[i], 2)
        return answer

    # insufficient check for line segments existing on same line
    # colinear test only tells same orientation...
    def countTrapezoids_fails(self, points: List[List[int]]) -> int:
        points.sort()
        slopes = defaultdict(list)
        for i in range(len(points)):
            x,y = points[i]
            for j in range(i+1, len(points)):
                a,b = points[j]
                if x == a:
                    slopes[(sys.maxsize, sys.maxsize)].append((x,y,a,b))
                    continue
                slopes[divmod(y - b, x - a)].append((x,y,a,b))
        answer = 0
        for s in slopes:
            for i in range(len(slopes[s])):
                ax1,ay1,ax2,ay2 = slopes[s][i]
                avx,avy = ax2-ax1,ay2-ay1
                for j in range(i+1, len(slopes[s])):
                    bx1,by1,bx2,by2 = slopes[s][j]
                    
                    # check if same start or end point
                    if (ax1 == bx1 and ay1 == by1) or (ax2 == bx2 and ay2 == by2):
                        continue
                    
                    # check if colinear
                    bvx,bvy = bx2-bx1,by2-by1
                    if avx * bvy - avy * bvx != 0:
                        # valid trapezoid
                        answer += 1
            pass
        return answer

    # based on leetocde hints
    # closer
    # over counting is occurring (issue with counting parallelogram)
    def countTrapezoids_fails(self, points: List[List[int]]) -> int:
        points.sort()

        lines = defaultdict(list)
        for i in range(len(points)):
            x,y = points[i]
            for j in range(i+1, len(points)):
                a,b = points[j]
                if a - x == 0:
                    lines[(sys.maxsize, sys.maxsize)].append((x,y,a,b))
                    continue
                lines[divmod(y-b,x-a)].append((x,y,a,b))
                
        # only one pair of parallel lines
        trapezoids = 0
        # two pairs of parallel lines
        parallelogram = 0
        for l in lines:
            for i in range(len(lines[l])):
                ax1,ay1,ax2,ay2 = lines[l][i]
                for j in range(i+1, len(lines[l])):
                    bx1,by1,bx2,by2 = lines[l][j]

                    if ((ax1 == bx1 and ay1 == by1) or 
                        (ax1 == bx2 and ay1 == by2) or
                        (ax2 == bx1 and ay2 == by1) or 
                        (ax2 == bx2 and ay2 == by2)):
                        # skip as line segments share endpoint
                        continue

                    if (ax1 == bx2) or divmod(by2-ay1,bx2-ax1) == l:
                        # same line, flat shape
                        continue

                    trapezoids += 1

                    # check if parallelogram
                    if ((ax1 == bx1 and ax2 == bx2) or 
                        (ax1 != bx1 and ax2 != bx2 and 
                         divmod(by1-ay1,bx1-ax1) == divmod(by2-ay2,bx2-ax2))):
                        parallelogram += 1
        return trapezoids - (parallelogram // 2 + parallelogram % 2)

    # Leetcode editorial
    # https://leetcode.com/problems/count-number-of-trapezoids-ii/editorial/?envType=daily-question&envId=2025-12-03
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10 ** 9 + 7
        slopeIntercept = defaultdict(list)
        midpointSlope = defaultdict(list)
        answer = 0

        # calculate the sloper,intercept and midpoint,slope for every pair
        for i in range(n):
            x,y = points[i]
            for j in range(i+1, n):
                a,b = points[j]
                dx = x - a
                dy = y - b
                slope = inf
                intercept = x
                if x != a:
                    slope = (b-y) / (a-x)
                    intercept = (y * dx - x * dy) / dx
                mid = (x + a) * 10000 + (y + b)
                slopeIntercept[slope].append(intercept)
                midpointSlope[mid].append(slope)
        
        # count the number of trapezoids
        # two line segments with same slope
        for s in slopeIntercept.values():
            if len(s) == 1:
                continue

            c = Counter(s)

            total = 0
            for i in c.values():
                answer += total * i
                total += i
        
        # count the number of parallelograms
        # two midpoints with same slope
        for m in midpointSlope.values():
            if len(m) == 1:
                continue

            c = Counter(m)

            total = 0
            for i in c.values():
                answer -= total * i
                total += i
        
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
        o = 2
        self.assertEqual(s.countTrapezoids(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0],[1,0],[0,1],[2,1]]
        o = 1
        self.assertEqual(s.countTrapezoids(i), o)

    def test_three(self):
        s = Solution()
        i = [[95,98],[12,32],[88,98],[-29,60]]
        o = 0
        self.assertEqual(s.countTrapezoids(i), o)

    def test_four(self):
        s = Solution()
        i = [[0,0],[1,1],[-1,1],[2,2]]
        o = 0
        self.assertEqual(s.countTrapezoids(i), o)

    def test_five(self):
        s = Solution()
        i = [[0,0],[1,1],[0,1],[1,0]]
        o = 1
        self.assertEqual(s.countTrapezoids(i), o)

    def test_six(self):
        s = Solution()
        i = [[82,7],[82,-9],[82,-52],[82,78]]
        o = 0
        self.assertEqual(s.countTrapezoids(i), o)

    def test_seven(self):
        s = Solution()
        i = [[32,-8],[-78,-25],[72,-8],[-77,-25]]
        o = 1
        self.assertEqual(s.countTrapezoids(i), o)

    def test_eight(self):
        s = Solution()
        i = [[-70,-36],[8,-3],[41,-16],[95,-36],[-27,-69],[-7,-52],[8,-69]]
        o = 1
        self.assertEqual(s.countTrapezoids(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)