# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n 1-indexed robots, each having a position on a line, health, and
    movement direction.

    Given a 0-indexed integer arrays positions, healths, and a string directions
    (directions[i] is either 'L' for left or 'R' for right). All integers in
    positions are unique.

    All robots start moving on the line simultaneously at the same speed in
    their given directions. If two robots ever share the same position while
    moving, they will collide.

    If two robots collide, the robot with lower health is removed from the line,
    and the health of the other robot decreases by one. The surviving robot
    continues in the same direction it was going. If both robots have the same
    health, they are both removed from the line.

    Determine the health of the robots that survive the collisions, in the same
    order that the robots were given, ie final health of robot 1 (if survived),
    final health of robot 2 (if survived), and so on. If there are no survivors,
    return an empty array.

    Return an array containing the health of the remaining robots (in the order
    they were given in the input), after no further collisions can occur.

    Note: the positions may be unsorted.
    '''
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        sort = sorted(range(len(positions)), key=lambda x: positions[x])
        living = set(range(len(positions)))
        pass
        for s in sort:
            if directions[s] == 'R':
                stack.append(s)
                continue
            while stack and healths[stack[-1]] < healths[s]:
                healths[s] -= 1
                living.remove(stack.pop())
            if stack and healths[stack[-1]] == healths[s]:
                living.remove(stack.pop())
                living.remove(s)
            elif stack:
                healths[stack[-1]] -= 1
                living.remove(s)
        return [healths[s] for s in range(len(positions)) if s in living]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,4,3,2,1]
        j = [2,17,9,15,10]
        k = "RRRRR"
        o = [2,17,9,15,10]
        self.assertEqual(s.survivedRobotsHealths(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = [3,5,2,6]
        j = [10,10,15,12]
        k = "RLRL"
        o = [14]
        self.assertEqual(s.survivedRobotsHealths(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = [1,2,5,6]
        j = [10,10,11,11]
        k = "RLRL"
        o = []
        self.assertEqual(s.survivedRobotsHealths(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)