# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array points where points[i] = [xi,yi] is the coordinates of the
    ith point on a 2D plane. Multiple points can have the same coordinates.

    Also given an array queries where queries[j] = [xj, yj, rj] describes a
    circle centered at (xj, yj) with a radius of rj.

    For each query queries[j], compute the number of points inside the jth
    circle. Points on the border of the circle are considered inside.

    Return an array answer, where answer[j] is the answer to the jth query.
    '''
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = [0] * len(queries)
        for x,y in points:
            for j in range(len(queries)):
                a,b,r = queries[j]
                answer[j] += r*r >= (a-x)*(a-x) + (b-y)*(b-y)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,3],[3,3],[5,3],[2,2]]
        j = [[2,3,1],[4,3,1],[1,1,2]]
        o = [3,2,2]
        self.assertEqual(s.countPoints(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[2,2],[3,3],[4,4],[5,5]]
        j = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
        o = [2,3,2,4]
        self.assertEqual(s.countPoints(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)