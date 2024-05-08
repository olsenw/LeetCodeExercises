# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    There is a robot starting at the position (0,0), the origin, on a 2D plane.
    Given a sequence of its moves, judge if this robot ends up at (0,0) after it
    completes its moves.

    Given a string moves that represents the move sequence of the robot where
    moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left),
    'U' (up), and 'D' (down).

    Return true if the robot returns to the origin after it finishes all of its
    moves, or false otherwise.

    Note: the way that the robot is "facing" is irrelevant. 'R' will always make
    the robot move to the right once, 'L' will always make it move left, etc.
    Also, assume that the magnitude of the robot's movement is the same for each
    move.
    '''
    def judgeCircl_conditional(self, moves: str) -> bool:
        x,y = 0,0
        for m in moves:
            if m == 'L':
                x -= 1
            elif m == 'R':
                x += 1
            elif m == 'U':
                y += 1
            elif m == 'D':
                y -= 1
        return x == 0 and y == 0

    def judgeCircl(self, moves: str) -> bool:
        c = Counter(moves)
        return c['L'] == c['R'] and c['U'] == c['D']

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "UD"
        o = True
        self.assertEqual(s.judgeCircle(i), o)

    def test_two(self):
        s = Solution()
        i = "LL"
        o = False
        self.assertEqual(s.judgeCircle(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)