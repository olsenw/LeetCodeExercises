# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    On an infinate plane a robot intially stands at (0,0) and faces 
    North. The robot can receive one of three instructions:
    - "G" : go straight 1 unit (ie in direction facing)
    - "L" : turn 90 degrees to the left
    - "R" : turn 90 degrees to the right

    The robot performs the instructions given in order and repeats them
    forever.

    Return True if and only if there exists a circle in the plane such
    that the robot never leaves the circle.
    '''
    def isRobotBounded(self, instructions: str) -> bool:
        # position of the robot
        turtle = [0,0]

        # directions robot can face
        direction = {
            "N": ((0,1), "W", "E"),
            "E": ((1,0), "N", "S"),
            "S": ((0,-1), "E", "W"),
            "W": ((-1,0), "S", "N")
            }

        # direction robot is facing
        facing = "N"

        # do one iteration of instructions
        for i in instructions:
            # turn robot left
            if i == 'L':
                facing = direction[facing][1]
            # turn robot right
            elif i == 'R':
                facing = direction[facing][2]
            # move robot 1 unit direction it is facing
            else:
                turtle[0] += direction[facing][0][0]
                turtle[1] += direction[facing][0][1]
        
        # distance from (0,0) robot traveled
        traveledsquared = turtle[0] * turtle[0] + turtle[1] + turtle[1]
        
        # print(turtle, facing, traveledsquared)

        # if robot did not move from initial position
        # if robot is not facing direction it started facing
        return True if traveledsquared == 0 or facing != "N" else False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "GGLLGG"
        o = True
        self.assertEqual(s.isRobotBounded(i), o)

    def test_two(self):
        s = Solution()
        i = "GG"
        o = False
        self.assertEqual(s.isRobotBounded(i), o)

    def test_three(self):
        s = Solution()
        i = "GL"
        o = True
        self.assertEqual(s.isRobotBounded(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)