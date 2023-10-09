# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given n points in the plane that are all distinct, where
    points[i] = [xi + yi]. A boomerang is a tuple of points (i, j, k) such that
    the distance between i and j equals the distance between i and k (the order 
    of the tuple matters).

    Return the number of boomerangs.
    '''
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        answer = 0
        for i,(x,y) in enumerate(points):
            h = Counter()
            for j,(a,b) in enumerate(points):
                if i == j:
                    continue
                h[(a-x)*(a-x)+(b-y)*(b-y)] += 1
            for c in h:
                answer += h[c] * (h[c] - 1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0],[1,0],[2,0]]
        o = 2
        self.assertEqual(s.numberOfBoomerangs(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[2,2],[3,3]]
        o = 2
        self.assertEqual(s.numberOfBoomerangs(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,1]]
        o = 0
        self.assertEqual(s.numberOfBoomerangs(i), o)

    def test_four(self):
        s = Solution()
        i = [[0,0],[1,0],[2,0],[1,1]]
        o = 8
        self.assertEqual(s.numberOfBoomerangs(i), o)

    def test_five(self):
        s = Solution()
        i = [[0,0],[1,0],[2,0],[1,1],[2,2],[3,3],[3,0],[0,3],[6,3]]
        o = 44
        self.assertEqual(s.numberOfBoomerangs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)