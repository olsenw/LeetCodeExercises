# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

# https://leetcode.com/problems/separate-squares-ii/editorial/?envType=daily-question&envId=2026-01-14
class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)
    
    def update(self, qleft, qright, qval, left, right, pos):
        if self.xs[right + 1] <= qleft or self.xs[left] >= qright:
            return
        if qleft <= self.xs[left] and self.xs[right + 1] <= qright:
            self.count[pos] += qval
        else:
            mid = (left + right) // 2
            self.update(qleft, qright, qval, left, mid, pos * 2 + 1)
            self.update(qleft, qright, qval, mid + 1, right, pos * 2 + 2)
        if self.count[pos] > 0:
            self.covered[pos] = self.xs[right + 1] - self.xs[left]
        else:
            if left == right:
                self.covered[pos] = 0
            else:
                self.covered[pos] = self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2]

    def query(self):
        return self.covered[0]

class Solution:
    '''
    Given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents
    the coordinates of the bottom-left point and the side length of a square
    parallel to the x-axis.

    Find the minimum y-coordinate value of a horizontal line such that the total
    area covered by squares above the line equals the total area covered by 
    squares below the line.

    Answers within 10^-5 of the actual answer will be accepted.

    Note: Squares may overlap. Overlapping areas should be counted only once.
    '''
    # based on Leetcode editorial
    # https://leetcode.com/problems/separate-squares-ii/editorial/?envType=daily-question&envId=2026-01-14
    def separateSquares(self, squares: List[List[int]]) -> float:
        # go through all the squares and find where squares overlap
        events = []
        xs_set = set()
        for x,y,l in squares:
            events.append((y, 1, x, x+l))
            events.append((y+l, -1, x, x+l))
            xs_set.update([x, x+l])
        xs = sorted(xs_set)
        events.sort()
        
        # create segment tree to track overlapping x intervals
        seg_tree = SegmentTree(xs)
        
        psum = []
        widths = []
        total_area = 0.0
        prev_y = events[0][0]

        # calculate the total area at each y coordinate of squares
        for y, delta, xl, xr in events:
            length = seg_tree.query()
            total_area += length * (y - prev_y)
            # line scan x axis
            seg_tree.update(xl, xr, delta, 0, seg_tree.n - 1, 0)
            # record prefix sums and widths
            psum.append(total_area)
            widths.append(seg_tree.query())
            prev_y = y
        
        # calculate total area (half rounded up)
        target = (total_area + 1) // 2
        # find the first position greater than or equal to target using binary search
        i = bisect.bisect_left(psum, target) - 1
        # get the corresponding area, width, and height
        area = psum[i]
        width = widths[i]
        height = events[i][0]

        return height + (total_area - area * 2) / (width * 2.0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0,1],[2,2,1]]
        o = 1.0
        self.assertAlmostEqual(s.separateSquares(i), o, 5)

    def test_two(self):
        s = Solution()
        i = [[0,0,2],[1,1,1]]
        o = 1.0
        self.assertAlmostEqual(s.separateSquares(i), o, 5)

    def test_three(self):
        s = Solution()
        i = [[15,21,2],[19,21,3]]
        o = 22.3
        self.assertAlmostEqual(s.separateSquares(i), o, 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)