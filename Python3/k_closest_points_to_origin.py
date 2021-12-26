# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of points where points[i] = [xi,yi] represents a
    point on the X-Y plane and an integer k, return the k closest points
    to the origin (0,0).

    The distance between two points is the Euclidean distance 
    (ie sqrt((x1-x2)^2 + (y1-y2)^2) ).
    '''
    # making use of min heap
    # O(n log(k)) n=num_elements k=size_heap
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        h = []
        for x,y in points:
            d = -1 * (x*x + y*y)
            if len(h) < k:
                heapq.heappush(h, (d, [x,y]))
            else:
                heapq.heappushpop(h, (d, [x,y]))
        return [j for i,j in h]
    
    # quick select algorithm (based on leetcode discsions)
    # O(n) time and O(1) space
    '''
    did not implement as it is Christmas day
    '''

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        p = [[1,3],[-2,2]]
        k = 1
        a = [[-2,2]]
        self.assertEqual(sorted(s.kClosest(p, k)), sorted(a))

    def test_two(self):
        s = Solution()
        p = [[3,3],[5,-1],[-2,4]]
        k = 2
        a = [[3,3],[-2,4]]
        self.assertEqual(sorted(s.kClosest(p, k)), sorted(a))

if __name__ == '__main__':
    unittest.main(verbosity=2)