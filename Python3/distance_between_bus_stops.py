# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A bus has n stops numbered from 0 to n - 1 that form a circle. The distance
    between all pairs of neighboring stops where distance[i] is the distance
    between the stops number i and (i + 1) % n.

    The bus goes along both directions ie clockwise and counterclockwise.

    Return the shortest distance between the given start and destination stops.
    '''
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        answer = float('inf')
        n = len(distance)
        # go right
        a = 0
        i = start
        while i != destination:
            a += distance[i]
            i += 1
            if i == n:
                i = 0
        answer = min(answer, a)
        # go left
        a = 0
        i = start - 1 if start > 0 else n - 1
        destination = destination - 1 if destination > 0 else n - 1
        while i != destination:
            a += distance[i]
            i -= 1
            if i < 0:
                i = n - 1
        answer = min(answer, a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        j = 0
        k = 1
        o = 1
        self.assertEqual(s.distanceBetweenBusStops(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        j = 0
        k = 2
        o = 3
        self.assertEqual(s.distanceBetweenBusStops(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3,4]
        j = 0
        k = 3
        o = 4
        self.assertEqual(s.distanceBetweenBusStops(i,j,k), o)


if __name__ == '__main__':
    unittest.main(verbosity=2)