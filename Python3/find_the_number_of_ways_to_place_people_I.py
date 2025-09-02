# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional, Tuple

class Solution:
    '''
    Given a 2D array points of size n x 2 representing integer coordinates of
    some points on a 2D plane, where points[i] = [xi, yi].

    Count the number of pairs of points (A, B) where:
    * A is the upper left side of B, and
    * There are no other points in the rectangle (or line) they make (including
      the border)
    
    Return the count.
    '''
    def numberOfPairs(self, points: List[List[int]]) -> int:
        def test(x:Tuple[int,int], y:Tuple[int,int], point:Tuple[int,int]) -> bool:
            if x[0] <= point[0] <= y[0]:
                return y[1] <= point[1] <= x[1]
            return False
        answer = 0
        points.sort(key=lambda x: (x[0],-x[1]))
        for i,x in enumerate(points):
            for j,y in enumerate(points[i+1:], i+1):
                # if not any(test(x,y,z) for k,z in enumerate(points[i+1:j], i+1)):
                #     answer += 1
                if x[1] < y[1]:
                    continue
                yes = 1
                for k,z in enumerate(points[i+1:j],i+1):
                    if test(x,y,z):
                        yes = 0
                        break
                answer += yes
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1],[2,2],[3,3]]
        o = 0
        self.assertEqual(s.numberOfPairs(i), o)

    def test_two(self):
        s = Solution()
        i = [[6,2],[4,4],[2,6]]
        o = 2
        self.assertEqual(s.numberOfPairs(i), o)

    def test_three(self):
        s = Solution()
        i = [[3,1],[1,3],[1,1]]
        o = 2
        self.assertEqual(s.numberOfPairs(i), o)

    def test_four(self):
        s = Solution()
        i = [[0,0],[0,3]]
        o = 1
        self.assertEqual(s.numberOfPairs(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)