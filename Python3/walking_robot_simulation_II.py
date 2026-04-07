# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

'''
A width x height grid on an XY-plane with the bottom-left cell at (0,0) and
the top-right cell at (width - 1, height - 1). The grid is aligned with the
four cardinal directions ("North", "East", "South", and "West"). A robot is
initially at cell (0,0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each
step, it does the following:
1. Attempts to move forward one cell in the direction it is facing.
2. If the cell the robot is moving is out of bounds, the robot instead turns
90 degrees counterclockwise and retries the step.

After the robot finishes moving the number of steps required, it stops and
awaits the next instruction.

Implement the robot class
'''
class Robot:
    '''
    Initializes the width x height grid with the robot at (0,0) facing "East".
    '''
    def __init__(self, width: int, height: int):
        self.m = height
        self.n = width
        self.loop = (2 * height) + (2 * (width - 2))
        self.x = 0
        self.y = 0
        self.dir = "South"
        self.moved = False
    
    '''
    Instructs the robot to move forward num steps.
    '''
    def step(self, num: int) -> None:
        num %= self.loop
        if num == 0:
            self.moved = True
        elif self.dir == "East":
            if self.x < self.n - 1:
                self.x += 1
                self.step(num-1)
            else:
                self.dir = "North"
                self.step(num)
        elif self.dir == "West":
            if self.x > 0:
                self.x -= 1
                self.step(num-1)
            else:
                self.dir = "South"
                self.step(num)
        elif self.dir == "North":
            if self.y < self.m - 1:
                self.y += 1
                self.step(num-1)
            else:
                self.dir = "West"
                self.step(num)
        elif self.dir == "South":
            if self.y > 0:
                self.y -= 1
                self.step(num-1)
            else:
                self.dir = "East"
                self.step(num)
        else:
            return

    '''
    Returns the current cell the robot is at, as an array of length 2, [x, y].
    '''
    def getPos(self) -> List[int]:
        return [self.x, self.y]

    '''
    Returns the current direction of the robot, "North", "East", "South", or
    "West".
    '''
    def getDir(self) -> str:
        return self.dir if self.moved else "East"

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Robot(6,3)
        s.step(2)
        s.step(2)
        self.assertEqual(s.getPos(), [4,0])
        self.assertEqual(s.getDir(), "East")
        s.step(2)
        s.step(1)
        s.step(4)
        self.assertEqual(s.getPos(), [1,2])
        self.assertEqual(s.getDir(), "West")

if __name__ == '__main__':
    unittest.main(verbosity=2)