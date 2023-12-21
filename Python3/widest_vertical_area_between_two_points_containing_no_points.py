# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given n points on a 2D plane where points[i] = [xi,yi]. Return the widest
    vertical area between two points such that there are no points are inside
    the area.

    A vertical are is an area fixed-width extending infinitely along the y-axis
    (ie of infinite height). The widest vertical area is the one with the
    maximum width.

    Note that points on the edge of a vertical area are not considered included
    in the area.
    '''
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(set(x for x,_ in points))
        answer = 0
        for i in range(len(points) - 1):
            answer = max(answer, points[i + 1] - points[i])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[8,7],[9,9],[7,4],[9,7]]
        o = 1
        self.assertEqual(s.maxWidthOfVerticalArea(i), o)

    def test_two(self):
        s = Solution()
        i = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
        o = 3
        self.assertEqual(s.maxWidthOfVerticalArea(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,1],[1,2],[1,3]]
        o = 0
        self.assertEqual(s.maxWidthOfVerticalArea(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)