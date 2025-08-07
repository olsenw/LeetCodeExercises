# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a game dungeon comprised of n x n rooms arranged in a grid.

    Given a 2D array fruits of size n x n, where fruits[i][j] represents the
    number of fruits in the room (i, j). Three children will play in the game
    dungeon, with initial positions at the corner rooms (0,0), (0, n-1),
    (n-1,0).

    The children will make exactly n-1 moves according to the following rules to
    reach the room (n-1, n-1):
    * The child starting from (0,0) must move from their current room (i,j) to
      one of the rooms (i+1, j+1), (i+1, j), and (i,j+1) if the target room
      exists.
    * The child starting from (0, n-1) must move from their current room (i,j)
      to one of the rooms (i+1, j-1), (i+1, j) and (i+1, j+1) if the target room
      exists.
    * The child starting from (n-1, 0) must move from their current room (i,j)
      to one of the rooms (i-1, j+1), (i,j+1), and (i+1, j+1) if the target room
      exists.

    When a child enters a room, they will collect all the fruits there. If two
    or more children enter the same room, only one child will collect the
    fruits, and the room will be empty after they leave.

    Return the maximum number of fruits the children can collect from the
    dungeon.
    '''
    # based on hints
    # 1) Child [0,0] has only one path the diagonal
    #    This is because each child can only make n-1 moves
    # 2) Other Children will not intersect the first child's path
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        # move diagonal
        a = sum(fruits[i][i] for i in range(n))
        # move down
        @cache
        def child2(i:int,j:int) -> int:
            if i == n-1 and j == n-1:
                return 0
            if i >= j or j == n:
                return float('-inf')
            return fruits[i][j] + max(child2(i+1,j-1),child2(i+1,j),child2(i+1,j+1))
        b = child2(0,n-1)
        # move right
        @cache
        def child3(i:int,j:int) -> int:
            if i == n-1 and j == n-1:
                return 0
            if i <= j or i == n:
                return float('-inf')
            return fruits[i][j] + max(child3(i-1,j+1),child3(i,j+1),child3(i+1,j+1))
        c = child3(n-1,0)
        return a + b + c

class UnitTesting(unittest.TestCase):
    '''
    Child One [0,0] (top-left)

    (i,j)   → (i,j+1)
       ↓    ↘
    (i+1,j)   (i+1,j+1)

    Child Two [0,n-1] (rop-right)

                (i,j)
              ↙   ↓   ↘
    (i+1,j-1)  (i+1,j)  (i+1, j+1)

    Child Three [n-1,0] (bottom-left)

            (i-1,j+1)
          ↗
    (i,j) → (i,j+1)
          ↘
            (i+1, j+1)
    '''

    def test_one(self):
        s = Solution()
        i = [[ 1, 2, 3, 4],
             [ 5, 6, 8, 7],
             [ 9,10,11,12],
             [13,14,15,16]]
        o = 100
        self.assertEqual(s.maxCollectedFruits(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,1],
             [1,1]]
        o = 4
        self.assertEqual(s.maxCollectedFruits(i), o)

    def test_three(self):
        s = Solution()
        i = [[ 1,99,99, 4],
             [99, 6, 8, 7],
             [99,10,11,12],
             [13,14,15,16]]
        o = 100
        self.assertEqual(s.maxCollectedFruits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)