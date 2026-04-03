# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an endless straight line populated with some robots and walls.
    Given integer arrays robots, distance, and walls:
    * robots[i] is the position of the ith robot.
    * distance[i] is the maximum distance the ith robot's bullet can travel.
    * walls[j] is the position of the jth wall.

    Every robot has one bullet that can either fire to the left or the right at
    most distance[i] meters.

    A bullet destroys every wall in its path that lies within its range. Robots
    are fixed obstacles: if a bullet hits another robot before reaching a wall,
    it immediately stops at that robot and cannot continue.

    Return the maximum number of unique walls that can be destroyed by the
    robots.

    Notes:
    * A wall and a robot may share the same position; the wall can be destroyed
      by the robot at that position.
    * Robots are not destroyed by bullets.
    '''
    def maxWalls_fails(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        robotOrder = sorted(range(len(robots)), key=lambda x:robots[x])
        walls.sort()
        # i is the robot being considered
        # j is the leftmost undestroyed wall (no robot in way)
        @cache
        def dp(i:int,j:int) -> int:
            # no more robots or no more walls
            if i >= len(robots) or j >= len(walls):
                return 0
            answer = 0
            robotLocation = robots[robotOrder[i]]
            robotShootDistance = distance[robotOrder[i]]
            # shoot left
            wLeft = bisect.bisect_left(walls, robotLocation - robotShootDistance, j)
            wRight = bisect.bisect(walls, robotLocation)
            answer = max(answer, wRight - wLeft + dp(i+1,wRight))
            # shoot right
            wLeft = bisect.bisect_left(walls, robotLocation)
            wRight = bisect.bisect(walls, min(robotLocation + robotShootDistance, robots[robotOrder[i+1]] if i+1 < len(robots) else float('inf')))
            answer = max(answer, wRight - wLeft + dp(i+1,wRight))
            return answer
        return dp(0,0)

    # based on editorial
    # https://leetcode.com/problems/maximum-walls-destroyed-by-robots/editorial/?envType=daily-question&envId=2026-04-03
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        # number of walls that ith robot can hit going left
        attackLeft = [0] * n
        # number of walls that ith robot can hit going right
        attackRight = [0] * n
        # number of walls between the i-1 and ith robot
        betweenWalls = [0] * n
        # map robot to distance it can shoot (works because robot position is unique)
        robotsDistance = {robots[i]:distance[i] for i in range(n)}
        # sort position of robots and walls
        robots.sort()
        walls.sort()
        # 
        for i in range(n):
            # get right most index of walls <= position robot[i]
            pos1 = bisect.bisect(walls, robots[i])
            # get left most index of walls <= position robot[i]
            pos2 = bisect.bisect_left(walls, robots[i])
            # If there is a robot to left
            if i >= 1:
                # shoot range left (can be bounded by position of i-1 robot)
                leftBound = max(
                    robots[i] - robotsDistance[robots[i]],
                    robots[i-1] + 1
                )
                leftPos = bisect.bisect_left(walls, leftBound)
            # base case no robot to left
            else:
                leftPos = bisect.bisect_left(walls, robots[i] - robotsDistance[robots[i]])
            # how many walls that can be destroyed left of robot[i]
            attackLeft[i] = pos1 - leftPos
            # If there is a robot to right
            if i < n-1:
                rightBound = min(
                    robots[i] + robotsDistance[robots[i]],
                    robots[i+1] - 1
                )
                rightPos = bisect.bisect(walls, rightBound)
            # base case no robot to right
            else:
                rightPos = bisect.bisect(walls, robots[i] + robotsDistance[robots[i]])
            # how many walls that can be destroyed right of robot[i]
            attackRight[i] = rightPos - pos2
            # no robot to left of robot[0] (so unable to calculate walls between i-1 and i)
            if i == 0:
                continue
            # calculate number of walls between robots i-1 and i
            pos3 = bisect.bisect_left(walls, robots[i-1])
            betweenWalls[i] = pos1 - pos3
        # dynamic programming
        # memoized as relations rely on one back
        subLeft, subRight = attackLeft[0], attackRight[0]
        for i in range(1,n):
            # best answer when shooting left for robot i
            currentLeft = max(
                # robot[i-1] shot left, robot[i] shot left
                subLeft + attackLeft[i],
                # robot[i-1] shot right, robot[i] shot left
                subRight - attackRight[i-1] + min(attackLeft[i] + attackRight[i-1], betweenWalls[i])
            )
            # best answer when shooting right for robot i
            currentRight = max(
                # robot[i-1] shot left, robot[i] shot right
                subLeft + attackRight[i],
                # robot[i-1] shot right, robot[i] shot left
                subRight + attackRight[i]
            )
            # update memoized dp
            subLeft,subRight = currentLeft,currentRight
        return max(subLeft,subRight)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4]
        j = [3]
        k = [1,10]
        o = 1
        self.assertEqual(s.maxWalls(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [10,2]
        j = [5,1]
        k = [5,2,7]
        o = 3
        self.assertEqual(s.maxWalls(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,2]
        j = [100,1]
        k = [10]
        o = 0
        self.assertEqual(s.maxWalls(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = [4]
        j = [3]
        k = [10]
        o = 0
        self.assertEqual(s.maxWalls(i,j,k), o)

    def test_five(self):
        s = Solution()
        i = [63,56,40,45,4,9,44,69,55,26,73,15,12,60,43,39,37,74,36,34,13,23,66,14,11,42,72,3,57,10,53,8,70,17,58,61,30,32]
        j = [8,7,4,8,9,5,2,4,5,2,6,9,5,9,5,3,7,6,9,2,8,7,4,3,5,1,7,5,1,3,5,3,5,4,8,7,6,4]
        k = [6,22,50,52,20,9,23,75,26,21,60,58,41,28,30]
        o = 15
        self.assertEqual(s.maxWalls(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)