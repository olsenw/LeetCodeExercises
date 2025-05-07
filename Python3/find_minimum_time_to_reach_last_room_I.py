# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a dungeon with n x m rooms arranged as a grid.

    Given a 2D array moveTime of size n x m, where moveTime[i][j] represents the
    minium time in seconds before it is possible to enter that room. Start from
    the room (0,0) at time t = 1 and can move to an adjacent room. Moving
    between adjacent rooms takes exactly one second.

    Return the minimum time to reach the room (n-1, m-1).

    Two rooms are adjacent if they share a common wall, either horizontally or
    vertically.
    '''
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m = len(moveTime), len(moveTime[0])
        visited = set()
        queue = [(0,0,0)]
        moveTime[0][0] = 0
        while queue:
            t,x,y = heapq.heappop(queue)
            if x == n - 1 and y == m - 1:
                return t
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if (a,b) not in visited and 0 <= a < n and 0 <= b < m:
                    heapq.heappush(queue, (1 + t if t > moveTime[a][b] else 1 + moveTime[a][b],a,b))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,4],[4,4]]
        o = 6
        self.assertEqual(s.minTimeToReach(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0,0],[0,0,0]]
        o = 3
        self.assertEqual(s.minTimeToReach(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,1],[1,2]]
        o = 3
        self.assertEqual(s.minTimeToReach(i), o)

    def test_four(self):
        s = Solution()
        i = [[15,58],[67,4]]
        o = 60
        self.assertEqual(s.minTimeToReach(i), o)

    def test_five(self):
        s = Solution()
        i = [[94,79,62,27,69,84],[6,32,11,82,42,30]]
        o = 72
        self.assertEqual(s.minTimeToReach(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)