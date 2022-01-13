# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There are some spherical balloons taped onto a flat wall that 
    represents the XY-plane. The balloons are represented as a 2D 
    integer array points where points[i] = [xstart, xend] denotes a 
    balloon whose horizontal diameter stretches between xstart and xend.
    The exact y-coordinates of the balloon are unknown.

    Arrows can be shot up directly vertically (in the positive y
    direction) from different points along the x-axis. A balloon with
    xstart and xend is burst by an arrow shot at x if xstart <= x <= 
    xend. There is no limit to the number of arrows that can be shot.
    An arrow keeps traveling infinitely, bursting any balloons in its
    path.

    Given the array points, return the minimum number of arrows that
    must be shot to burst all balloons.
    '''
    # O(nlogn) time (the sort is determining factor)
    def findMinArrowShots_sortX(self, points: List[List[int]]) -> int:
        points = sorted(points)
        ix = points[0][0]
        iy = points[0][1]
        arrow = 0
        for x,y in points:
            ix = max(ix, x)
            iy = min(iy, y)
            if iy < ix:
                ix = x
                iy = y
                arrow += 1
        return arrow + 1

    # O(nlogn) time (the sort is determining factor)
    # should be faster due to fewer computations in loop
    def findMinArrowShots_sortY(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[1])
        i = points[0][1]
        arrow = 0
        for x,y in points:
            if i < x:
                i = y
                arrow += 1
        return arrow + 1

    '''
    incorrect solutions for posterity
    got caught going down a poor line of thinking
    '''
    # very slow due to heap and having to check all launched arrows
    # Not even Correct
    def findMinArrowShots_heapq(self, points: List[List[int]]) -> int:
        import heapq
        h = []
        for x,y in points:
            heapq.heappush(h, (y-x, y, x))
        a = [heapq.heappop(h)[1]]
        for s,y,x in [heapq.heappop(h) for _ in range(len(h))]:
            for arrow in a:
                if x <= arrow <= y:
                    break
            else:
                a.append(y)
        return len(a)

    # also very slow due to the double loop (basically same as above)
    # Not even Correct
    def findMinArrowShots_sort(self, points: List[List[int]]) -> int:
        p = sorted([(y-x, y, x) for x,y in points])
        arrow = [p[0][1]]
        for _, y, x in p[1:]:
            for a in arrow:
                if x <= a <=y:
                    break
            else:
                arrow.append(y)
        return len(arrow)

    # Even slower... wow...
    # Not even Correct
    def findMinArrowShots_filter(self, points: List[List[int]]) -> int:
        p = sorted([[y-x, y, x] for x,y in points])
        a = 0
        for i in range(len(p)):
            if not p[i][0]:
                continue
            for j in range(i+1, len(p)):
                if not p[j][0]:
                    continue
                s = p[i]
                b = p[j]
                if b[2] <= s[1] <= b[1]:
                    a += 1
                    b[0] = 0
        return len(p) - a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[10,16],[2,8],[1,6],[7,12]]
        o = 2
        self.assertEqual(s.findMinArrowShots_sortX(i), o)
        self.assertEqual(s.findMinArrowShots_sortY(i), o)
        self.assertEqual(s.findMinArrowShots_heapq(i), o)
        self.assertEqual(s.findMinArrowShots_sort(i), o)
        self.assertEqual(s.findMinArrowShots_filter(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[3,4],[5,6],[7,8]]
        o = 4
        self.assertEqual(s.findMinArrowShots_sortX(i), o)
        self.assertEqual(s.findMinArrowShots_sortY(i), o)
        self.assertEqual(s.findMinArrowShots_heapq(i), o)
        self.assertEqual(s.findMinArrowShots_sort(i), o)
        self.assertEqual(s.findMinArrowShots_filter(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2],[2,3],[3,4],[4,5]]
        o = 2
        self.assertEqual(s.findMinArrowShots_sortX(i), o)
        self.assertEqual(s.findMinArrowShots_sortY(i), o)
        self.assertEqual(s.findMinArrowShots_heapq(i), o)
        self.assertEqual(s.findMinArrowShots_sort(i), o)
        self.assertEqual(s.findMinArrowShots_filter(i), o)

    def test_four(self):
        s = Solution()
        i = [[4,5],[1,3],[6,8],[0,4],[2,3],[4,8]]
        o = 3
        self.assertEqual(s.findMinArrowShots_sortX(i), o)
        self.assertEqual(s.findMinArrowShots_sortY(i), o)
        self.assertEqual(s.findMinArrowShots_heapq(i), o)
        self.assertEqual(s.findMinArrowShots_sort(i), o)
        self.assertEqual(s.findMinArrowShots_filter(i), o)

    def test_five(self):
        s = Solution()
        i = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
        o = 2
        self.assertEqual(s.findMinArrowShots_sortX(i), o)
        self.assertEqual(s.findMinArrowShots_sortY(i), o)
        # these ones fail...
        # self.assertEqual(s.findMinArrowShots_heapq(i), o)
        # self.assertEqual(s.findMinArrowShots_sort(i), o)
        # self.assertEqual(s.findMinArrowShots_filter(i), o)

    def time(self, s):
        i = [[i, i+1] for i in range(-10**5, 10**5, 2)]
        o = 10**5
        self.assertEqual(len(i), o)
        import time
        t = time.time_ns()
        a = s(i)
        print('sec ', (time.time_ns() - t) / 10**9)
        self.assertEqual(a, o)
    
    def test_time_works(self):
        self.time(Solution().findMinArrowShots_sortX)
        self.time(Solution().findMinArrowShots_sortY)
    
    # def test_time_heapq(self):
    #     self.time(Solution().findMinArrowShots_heapq)
    
    # def test_time_sort(self):
    #     self.time(Solution().findMinArrowShots_sort)
    
    # def test_time_thunks(self):
    #     self.time(Solution().findMinArrowShots_filter)

if __name__ == '__main__':
    unittest.main(verbosity=2)