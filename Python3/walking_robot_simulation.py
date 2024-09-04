# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A robot on an infinite XY-plane starts at point (0, 0) facing north. The
    robot can receive a sequence of these three possible types of commands:
    * -2: Turn left 90 degrees.
    * -1: Turn right 90 degrees.
    * 1 <= k <= 9: Move forward k units, one unit at a time.

    Some of the grid squares are obstacles. The ith obstacle is at grid point
    obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will
    instead stay in its current location and move on to the next command.

    Return the maximum Euclidean distance that the robot ever gets from the
    origin squared (ie, if the distance is 5, return 25).

    Notes:
    * North means +Y direction
    * East means +X direction
    * South means -Y direction
    * West means -X direction
    * There can be obstacle in [0,0].
    '''
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        answer = 0
        direction = 0
        x,y = 0,0
        obstacles = set((a,b) for a,b in obstacles)
        for c in commands:
            if c == -2:
                direction -= 1
                if direction == -1:
                    direction = 3
            elif c == -1:
                direction += 1
                if direction == 4:
                    direction = 0
            else:
                if direction == 0:
                    for _ in range(c):
                        if (x, y+1) not in obstacles:
                            y += 1
                elif direction == 1:
                    for _ in range(c):
                        if (x+1, y) not in obstacles:
                            x += 1
                elif direction == 2:
                    for _ in range(c):
                        if (x, y-1) not in obstacles:
                            y -= 1
                elif direction == 3:
                    for _ in range(c):
                        if (x-1, y) not in obstacles:
                            x -= 1
                answer = max(answer, x * x + y * y)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,-1,3], []
        o = 25
        self.assertEqual(s.robotSim(*i), o)

    def test_two(self):
        s = Solution()
        i = [4,-1,4,-2,4], [[2,4]]
        o = 65
        self.assertEqual(s.robotSim(*i), o)

    def test_three(self):
        s = Solution()
        i = [6,-1,-1,6], []
        o = 36
        self.assertEqual(s.robotSim(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)