# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq

class Solution:
    '''
    A city's skyline is the outer contour of the silhouette formed by all the
    buildings in that city when viewed from a distance. Given the locations and
    heights of all the buildings, return the skyline formed by these buildings
    collectively.

    The geometric information of each building is given in the array buildings
    where buildings[i] = [lefti, righti, heighti]:
    * lefti is the x coordinate of the left edge of the ith building.
    * righti is the x coordinate of the right edge of the ith building.
    * heighti is the height of the ith building.

    It is assumed all buildings are perfect rectangles grounded on an absolutely
    flat surface at height 0.

    The skyline should be represented as a list of "key points" sorted by their
    x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left
    endpoint of some horizontal segment in the skyline except the last point in
    the list, which always has a y-coordinate of 0 and is used to mark the
    skyline's termination where the rightmost building ends. Any ground between
    the leftmost and rightmost buildings should be part of the skyline's
    contour.

    Note: There must be no consecutive horizontal lines of equal height in the
    output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is
    not acceptable; the three lines of height 5 should be merged into one in the
    final output as such: [...,[2 3],[4 5],[12 7],...].
    '''
    def getSkyline_incomplete(self, buildings: List[List[int]]) -> List[List[int]]:
        # geometric data representing skyline
        sky = [[buildings[0][0], buildings[0][2]]]
        # heap that should be ordered by (height,ending) - pop if beyond ending
        heap = [(buildings[0][2],buildings[0][1])]
        # iterate through all the buildings
        for l,r,h in buildings[1:]:
            y,x = heap[0]
            while heap and heap[0][1] <= l:
                y,x = heapq.heappop(heap)
                if heap:
                    sky.append([x, heap[0][1]])
                else:
                    sky.append([x,0])
            heapq.heappush(heap,(h,r))
            if heap[0][0] >= y:
                sky.append([l,h])
        while len(heap) > 1:
            sky.append([heapq.heappop(heap)[1], heap[0][1]])
        if heap:
            sky.append([heapq.heappop(heap)[1],0])
        # remove bad points from sky...?
        skyline = []
        for i,j in sky:
            pass
        return skyline

    # from a leetcode discussion post that I can no longer find
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        interest = sorted([(l,-h,r) for l,r,h in buildings] + [(r,0,0) for _,r,_ in buildings])
        skyline = [[0,0]]
        heap = [[0, 2**31]]
        for l, h, r in interest:
            while heap[0][1] <= l:
                heapq.heappop(heap)
            if h:
                heapq.heappush(heap, [h,r])
            if skyline[-1][1] != -heap[0][0]:
                skyline.append([l, -heap[0][0]])
        return skyline[1:]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        o = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        self.assertEqual(s.getSkyline(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,2,3],[2,5,3]]
        o = [[0,3],[5,0]]
        self.assertEqual(s.getSkyline(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)