# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n matrix of character box representing a side-view of a box.
    Each cell of the box is one of the following.
    * A stone '#'
    * A stationary obstacle '*'
    * Empty '.'

    The box is rotated 90 degrees clockwise, causing some of the stones to fall
    due to gravity. Each stone falls down until it lands on an obstacle, another
    stone, or the bottom of the box. Gravity does not affect the obstacles'
    positions, and the inertia from the box's rotation does not affect the
    stones' horizontal positions.

    It is guaranteed that each stone in box rests on an obstacle; another stone,
    or the bottom of the box.

    Return an n x m matrix representing the box after the rotation described
    above.
    '''
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m,n = len(box), len(box[0])
        height = [n - 1] * m
        answer = [["."] * m for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(m):
                # stone
                if box[j][i] == '#':
                    answer[height[j]][j] = '#'
                    height[j] -= 1
                # blocker
                elif box[j][i] == "*":
                    height[j] = i
                    answer[height[j]][j] = '*'
                    height[j] -= 1
        return [r[::-1] for r in answer]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["#",".","#"]]
        o = [["."],
         ["#"],
         ["#"]]
        self.assertEqual(s.rotateTheBox(i), o)

    def test_two(self):
        s = Solution()
        i = [["#",".","*","."],
              ["#","#","*","."]]
        o = [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
        self.assertEqual(s.rotateTheBox(i), o)

    def test_three(self):
        s = Solution()
        i = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
        o = [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
        self.assertEqual(s.rotateTheBox(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)