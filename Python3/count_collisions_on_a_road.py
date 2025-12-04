# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n cars on an infinitely long road. The cars are numbered from 0 to
    n - 1 from left to right and car is present at a unique point.

    Given a 0-indexed string directions of length n. directions[i] can be either
    ['L', 'R', or 'S'] denoting whether the ith car is moving towards the left,
    towards the right, or staying at its current point respectively. Each moving
    car has the same speed.

    The number of collisions is calculated as follows:
    * When two cars moving in opposite directions collide with each other, the
      number of collisions increases by 2.
    * When a moving car collides with a stationary car, the number of collisions
      increases by 1.
    
    After a collision, the cars involved can no longer move and will stay at the
    point where they collided. Other than that, cars cannot change their state
    or direction of motion.
    '''
    # works, but lazy
    # could do better job counting instead of list
    def countCollisions(self, directions: str) -> int:
        answer = 0
        behind = []
        for d in directions:
            if d == 'S':
                if behind and behind[-1] == 'R':
                  # answer += behind.count('R')
                  answer += len(behind)
                behind = ['S']
            elif d == 'L':
                if len(behind):
                    answer += 1
                    # answer += behind.count('R')
                    if behind[-1] == 'R':
                        answer += len(behind)
                    behind = ['S']
            else:
                if behind and behind[-1] == 'S':
                    behind = ['R']
                else:
                    behind.append('R')
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "RLRSLL"
        o = 5
        self.assertEqual(s.countCollisions(i), o)

    def test_two(self):
        s = Solution()
        i = "LLRR"
        o = 0
        self.assertEqual(s.countCollisions(i), o)

    def test_three(self):
        s = Solution()
        i = "SRRRRRRLSRRRRRRL"
        o = 14
        self.assertEqual(s.countCollisions(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)