# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are some robots and factories on the X-axis. Given an integer array
    robot where robot[i] is the position of the ith robot. Also given is a 2D
    integer array factory where factory[j] = [positionj, limitj] indicates that
    positionj is the position of the jth factory and the jth factory can repair
    at most limitj robots.

    The positions of each robot are unique. The positions of each factory are
    also unique. Note that a robot can be in the same position as a factory
    initially.

    All the robots are initially broken; they keep moving in one direction. The
    direction could be the negative or the positive direction of the X-axis.
    When a robot reaches a factory that did not reach its limit, the factory
    repairs the robot, and it stops moving.

    At any moment, it is possible to set the initial direction of moving for
    some robot. The target is to minimize the total distance traveled by all the
    robots.

    Return the minimum total distance traveled by all the robots. The test cases
    are generated such that all the robots can be repaired.

    Note that
    * All robots move at the same speed.
    * If two robots move in the same direction, they will never collide.
    * If two robots move in opposite directions and they meet at some point,
      they do not collide. They cross each other.
    * If a robot passes by a factory that reached its limit, it crosses it as if
      it does not exist.
    * If the robot moved from a position x to a position y, the distance it
      moved is abs(y - x)
    '''
    # based on Leetcode editorial 
    # https://leetcode.com/problems/minimum-total-distance-traveled/editorial/?envType=daily-question&envId=2024-10-31
    def minimumTotalDistance_memory_exceeded(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        # flatten factories array for easier assignment
        factories = []
        for i,j in sorted(factory):
            factories.extend([i] * j)
        @cache
        def dp(i:int, j:int) -> int:
            # all the robots have been assigned
            if i == len(robot):
                return 0
            # no factories left to assign (failed path)
            if j == len(factories):
                return float('inf')
            # assign current robot to factory
            a = abs(robot[i] - factories[j]) + dp(i+1, j+1)
            # assign current robot to the next factory
            b = dp(i, j+1)
            return min(a,b)
        return dp(0, 0)

    # this works... wonder if cache causes a memory issue
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        # flatten factories array for easier assignment
        factories = []
        for i,j in sorted(factory):
            factories.extend([i] * j)
        # manual dp table
        dp = [[None] * (len(factories) + 1) for _ in range(len(robot) + 1)]
        def calc(i:int, j:int) -> int:
            if dp[i][j] is not None:
                return dp[i][j]
            if i == len(robot):
                dp[i][j] = 0
                return 0
            if j == len(factories):
                dp[i][j] = float('inf')
                return float('inf')
            a = abs(robot[i] - factories[j]) + calc(i+1, j+1)
            b = calc(i, j+1)
            dp[i][j] = min(a,b)
            return dp[i][j]
        return calc(0,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,4,6]
        j = [[2,2],[6,2]]
        o = 4
        self.assertEqual(s.minimumTotalDistance(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,-1]
        j = [[-2,1],[2,1]]
        o = 2
        self.assertEqual(s.minimumTotalDistance(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)