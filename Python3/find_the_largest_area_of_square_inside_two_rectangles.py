# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There exist n rectangles in a 2D plane with edges parallel to the x and y
    axis. Given two 2D integer arrays bottomLeft and topRight where
    bottomLeft[i] = [ai, bi] and topRight = [ci, di] represent the bottom-left
    and top-right coordinates of the ith rectangle, respectively.

    Find the maximum area of a square that can fit inside the intersecting
    region of at least two rectangles. Return 0 if such a square does not exist.
    '''
    def largestSquareArea_fails(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        rectangles = list(range(len(bottomLeft)))
        rectangles.sort(key=lambda x: (bottomLeft[x][0],bottomLeft[x][1],topRight[x][0],topRight[x][1]))
        answer = 0
        for i in range(len(rectangles)):
            a,b = bottomLeft[rectangles[i]]
            c,d = topRight[rectangles[i]]
            for j in range(i+1, len(rectangles)):
                w,x = bottomLeft[rectangles[j]]
                y,z = topRight[rectangles[j]]
                if c <= w or d <= x:
                    break
                side = min((c-w), (d-x))
                answer = max(answer, side * side)
        return answer

    # sometimes brute force is the answer
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        answer = 0
        for i in range(len(bottomLeft)):
            x1,y1 = bottomLeft[i]
            x2,y2 = topRight[i]
            for j in range(i+1, len(bottomLeft)):
                a1,b1 = bottomLeft[j]
                a2,b2 = topRight[j]

                if x1 <= a1 < x2 or a1 <= x1 < a2:
                    if y1 <= b1 < y2 or b1 <= y1 < b2:
                        width = min(x2,a2) - max(x1,a1)
                        heigh = min(y2,b2) - max(y1,b1)
                        side = min(width, heigh)
                        answer = max(answer, side * side)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1],[2,2],[3,1]]
        j = [[3,3],[4,4],[6,6]]
        o = 1
        self.assertEqual(s.largestSquareArea(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[1,3],[1,5]]
        j = [[5,5],[5,7],[5,9]]
        o = 4
        self.assertEqual(s.largestSquareArea(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[1,1],[2,2],[1,2]]
        j = [[3,3],[4,4],[3,4]]
        o = 1
        self.assertEqual(s.largestSquareArea(i,j), o)

    def test_four(self):
        s = Solution()
        i = [[1,1],[3,3],[3,1]]
        j = [[2,2],[4,4],[4,2]]
        o = 0
        self.assertEqual(s.largestSquareArea(i,j), o)

    def test_five(self):
        s = Solution()
        i = [[1,2],[1,2]]
        j = [[4,5],[2,3]]
        o = 1
        self.assertEqual(s.largestSquareArea(i,j), o)

    def test_six(self):
        s = Solution()
        i = [[2,2],[1,3]]
        j = [[3,4],[5,5]]
        o = 1
        self.assertEqual(s.largestSquareArea(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)