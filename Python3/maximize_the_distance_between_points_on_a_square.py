# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer side, representing the edge length of a square with corners
    at (0,0), (0,side), (side,0), (side,side) on a Cartesian plane.

    Also given a positive integer k and a 2D integer array points, where
    points[i] = [xi, yi] represents the coordinate of a point lying on the
    boundary of the square.

    Select k elements among points such that the minimum Manhattan distance
    between any two points is maximized.

    Return the maximum possible minimum Manhattan distance between the selected
    k points.

    The Manhattan Distance between two cells (xi, yi) and (xj, yj) is
    |xi - xj| + |yi - yj|.
    '''
    # based on hints
    # close but not there
    # the clockwise unwrapping of the square is clunky
    # the check function is unable to selectively skip a point (need to test starting at each point)
    def maxDistance_fails(self, side: int, points: List[List[int]], k: int) -> int:
        # points on the square in clockwise order
        clockwise = []
        clockwise.extend(sorted((x for x in points if x[0] == 0), key=lambda x:x[1]))
        if clockwise and clockwise[-1] == [0,side]:
            clockwise.pop()
        clockwise.extend(sorted((x for x in points if x[1] == side), key=lambda x:x[0]))
        if clockwise and clockwise[-1] == [side,side]:
            clockwise.pop()
        clockwise.extend(sorted((x for x in points if x[0] == side), key=lambda x:-x[1]))
        if clockwise and clockwise[-1] == [side,0]:
            clockwise.pop()
        clockwise.extend(sorted((x for x in points if x[1] == 0), key=lambda x:-x[0]))
        if clockwise and clockwise[-1] != [0,0]:
            clockwise.append(clockwise[0])
        def manhattan(a:List[int], b:List[int]) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        # the minimum possible Manhattan distance (in clockwise order) is point left or right current point
        # can greedily select points that meet the minimum distance
        # fails (it is possible to select a point, skip point, then select)
        def check(d:int) -> int:
            answer = 0
            for i in range(1, len(clockwise) - 1):
                x = manhattan(clockwise[i-1], clockwise[i])
                y = manhattan(clockwise[i], clockwise[i+1])
                if x >= d and y >= d:
                    answer += 1
            x = manhattan(clockwise[0], clockwise[1])
            y = manhattan(clockwise[0], clockwise[-2])
            if x >= d and y >= d:
                answer += 1
            return answer
        # binary search the maximum possible minimum Manhattan distance
        answer = 0
        i,j = 0, 2 * side
        while i <= j:
            m = (i + j) // 2
            if check(m) >= k:
                answer = m
                i = m + 1
            else:
                j = m - 1
        return answer

    # based on leetcode solution
    # https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/editorial/?envType=daily-question&envId=2026-04-25
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # unwrap the square into a 1D clockwise array
        clockwise = []
        for x,y in points:
            if x == 0:
                clockwise.append(y)
            elif y == side:
                clockwise.append(side + x)
            elif x == side:
                clockwise.append(3 * side - y)
            else:
                clockwise.append(4 * side - x)
        clockwise.sort()
        # total perimeter of square
        p = side * 4
        # test if possible to greedy select k points
        def check(m:int) -> bool:
            # starting point clockwise
            for start in clockwise:
                # last possible selectable point
                end = start + p - m
                cur = start
                # attempt to greedy select k points starting at point start
                for _ in range(k-1):
                    i = bisect.bisect_left(clockwise, cur + m)
                    # ran out of points or too far away from cur (limit of Manhattan distance)
                    if i == len(clockwise) or clockwise[i] > end:
                        cur = -1
                        break
                    cur = clockwise[i]
                if cur >= 0:
                    return True
            return False

        # binary search to find the maximum minimum Manhattan distance
        i,j = 1, side
        answer = 0
        while i <= j:
            m = (i + j) // 2
            if check(m):
                i = m + 1
                answer = m
            else:
                j = m - 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = [[0,2],[2,0],[2,2],[0,0]]
        k = 4
        o = 2
        self.assertEqual(s.maxDistance(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [[0,0],[1,2],[2,0],[2,2],[2,1]]
        k = 4
        o = 1
        self.assertEqual(s.maxDistance(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 2
        j = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]]
        k = 5
        o = 1
        self.assertEqual(s.maxDistance(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 15
        j = [[15,6],[0,13],[13,0],[10,0]]
        k = 4
        o = 3
        self.assertEqual(s.maxDistance(i,j,k), o)

    def test_five(self):
        s = Solution()
        i = 42
        j = [[6,42],[41,0],[42,7],[42,32]]
        k = 4
        o = 8
        self.assertEqual(s.maxDistance(i,j,k), o)

    def test_six(self):
        s = Solution()
        i = 4
        j = [[4,4],[3,4],[2,0],[4,3],[4,0]]
        k = 4
        o = 2
        self.assertEqual(s.maxDistance(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)