# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

import heapq

class Solution:
    '''
    Given an integer array heights representing the heights of
    buildings, some bricks, and some ladders.

    A journey is started on building 0 and moves to the next building
    by possibly using bricks or ladders.

    While moving from building i to building i+1 (0-indexed):
    * If the current building's height is greater than or equal to the
      next building's height, neither bricks or ladders are needed.
    * If the current building's height is less than the next building's
      height, one ladder or (h[i+1] - h[i]) bricks are used.

    Return the furthest building index (0-indexed) that can be reached
    if all the bricks and ladders are used optimally.
    '''
    # does not optimally chooses where ladders should go
    def furthestBuilding_greedy_wrong(self, heights: List[int], bricks: int, ladders: int) -> int:
        for i in range(len(heights) - 1):
            h = heights[i + 1] - heights[i]
            if h >= 0:
                if bricks > h:
                    bricks -= h
                elif ladders:
                    ladders -= 1
                elif bricks == h:
                    bricks -= h
                else:
                    return i
        return len(heights) - 1

    # based on leetcode hints
    # uses heap to keep track of best ladder jumps
    # decrements bricks for every non ladder jump
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapq.heapify(heap)
        for i in range(len(heights) - 1):
            h = heights[i + 1] - heights[i]
            if h > 0:
                if len(heap) < ladders:
                    heapq.heappush(heap, h)
                elif heap and bricks:
                    bricks -= heapq.heappushpop(heap, h)
                    if bricks < 0:
                        return i
                elif bricks >= h:
                    bricks -= h
                else:
                    return i
        return len(heights) - 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        #   [- 5 - l *]
        #   [- l - 3 *]
        i = [4,2,7,6,9,14,12]
        j = 5
        k = 1
        o = 4
        self.assertEqual(s.furthestBuilding(i,j,k), o)

    def test_two(self):
        s = Solution()
        #   [l -- 5 - l  2 -- *]
        i = [4,12,2,7,3,18,20,3,19]
        j = 10
        k = 2
        o = 7
        self.assertEqual(s.furthestBuilding(i,j,k), o)

    def test_three(self):
        s = Solution()
        #   [-- 16 - *]
        i = [14,3,19,3]
        j = 17
        k = 0
        o = 3
        self.assertEqual(s.furthestBuilding(i,j,k), o)

    def test_four(self):
        s = Solution()
        #   [4 l l *]
        #   [l 1 1 1 1 *]
        i = [1,5,6,7,8,9]
        j = 4
        k = 2
        o = 5
        self.assertEqual(s.furthestBuilding(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)