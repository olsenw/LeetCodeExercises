# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is an n x n grid, with the top-left cell at (0, 0) and the
    bottom-right cell a (n-1, n-1). Given the integer n and an integer array
    startPos where startPos = [startrow, startcol] indicates that a robot
    initially at cell (startrow, startcol).

    Also given is a 0-indexed string s of length m where s[i] is the ith
    instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up),
    and 'D' (move down).

    The robot can begin executing from the ith instruction in s. It executes the
    instructions one by one towards the end of s but it stops if either of these
    conditions is met:
    * The next instruction will move the robot off the grid.
    * There are no more instructions left to execute.

    Return an array answer of length m where answer[i] is the number of
    instructions the robot can execute if the robot begins executing from the
    ith instruction in s.
    '''
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        answer = []
        for i in range(len(s)):
            x,y = startPos
            count = 0
            for c in s[i:]:
                if c == 'U':
                    x -= 1
                elif c == 'D':
                    x += 1
                elif c == 'L':
                    y -= 1
                elif c == 'R':
                    y += 1
                if 0 <= x < n and 0 <= y < n:
                    count += 1
                else:
                    break
            answer.append(count)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = [0,1]
        k = "RRDDLU"
        o = [1,5,4,3,1,0]
        self.assertEqual(s.executeInstructions(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = [1,1]
        k = "LURD"
        o = [4,1,0,0]
        self.assertEqual(s.executeInstructions(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = [0,0]
        k = "LRUD"
        o = [0,0,0,0]
        self.assertEqual(s.executeInstructions(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)