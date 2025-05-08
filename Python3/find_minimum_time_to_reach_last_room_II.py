# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import heapq
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a dungeon with n x m rooms arranged as a grid.

    Given a 2D array moveTime of size n x m, where moveTime[i][j] represents the
    minimum time in seconds before it is possible to enter a that room. Start
    from room (0,0) at time t = 0 and it is possible to move to an adjacent
    room. Moving between adjacent rooms takes one-second for one move and two
    seconds for the next, alternating between the two.

    Return the minimum time to reach the room (n-1, m-1).

    Two rooms are adjacent if they share a common wall, either horizontally or
    vertically.
    '''
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        queue = [(0,True,0,0)]
        visited = set()
        while queue:
            time, segment, x, y = heapq.heappop(queue)
            if x == n - 1 and y == m - 1:
                return time
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= i < n and 0 <= j < m:
                    heapq.heappush(queue, ((2-segment)+max(time,moveTime[i][j]),not segment,i,j))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,4],[4,4]]
        o = 7
        self.assertEqual(s.minTimeToReach(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0,0,0],[0,0,0,0]]
        o = 6
        self.assertEqual(s.minTimeToReach(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,1],[1,2]]
        o = 4
        self.assertEqual(s.minTimeToReach(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)