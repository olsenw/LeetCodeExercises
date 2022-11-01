# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a 2-D grid of size m x n representing a box, and given n balls. The
    box is open on the top and bottom sides.

    Each cell in the box has a diagonal board spanning two corners of the cell
    that can redirect a ball to the right or to the left.
    * A board that redirects the ball to the right spans the top-left corner to
      the bottom-right corner and is represented in the grid as 1.
    * A board that redirects the ball to the left spans the top-right corner to
      the bottom-left corner and is represented in the grid as -1.
    
    The ball is dropped at the top of each column of the box. Each ball can get
    stuck in the box or fall out of the bottom. A ball gets stuck if it hits a
    "V" shaped pattern between two boards or if a board redirects the ball into
    either wall of the box.

    Return an array answer of size n where answer[i] is the column that the ball
    falls out of at the bottom after dropping the ball from the ith column at
    the top, or -1 if the ball gets stuck in the box.
    '''
    # somewhere there is n issue/typo/logic mistake
    def findBall_simulation_fails(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        if n == 1:
            return [-1]
        answer = [i for i in range(n)]
        for i in range(m):
            step = [-1] * n
            for j in range(n):
                if answer[j] == -1:
                    continue
                elif answer[j] == 0:
                    if grid[i][0] == 1:
                        step[j] = 1
                elif answer[j] == n-1:
                    if grid[i][n-1] == -1:
                        step[j] = n - 2
                else:
                    c = answer[j]
                    if grid[i][c] == 1:
                        if grid[i][c+1] == 1:
                            step[j] = answer[j] + 1
                    else:
                        if grid[i][c-1] == -1:
                            step[j] = answer[j] - 1
            answer = step
        return answer

    # derived from leetcode simulation solution
    # https://leetcode.com/problems/where-will-the-ball-fall/solution/
    # sequentially simulates dropping ball into each column and seeing where it lands
    # simpler than trying to update all balls at once like above attempt
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        answer = [i for i in range(n)]
        for col in range(n):
            location = col
            for row in range(m):
                newLocation = location + grid[row][location]
                if newLocation < 0 or newLocation > n-1 or grid[row][location] != grid[row][newLocation]:
                    answer[col] = -1
                    break
                answer[col] = newLocation
                location = newLocation
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
        o = [1,-1,-1,-1,-1]
        self.assertEqual(s.findBall(i), o)

    def test_one_one(self):
        s = Solution()
        i = [[1,1,1,-1,-1]]
        o = [1,2,-1,-1,3]
        self.assertEqual(s.findBall(i), o)

    def test_one_two(self):
        s = Solution()
        i = [[1,1,1,-1,-1],[1,1,1,-1,-1]]
        o = [2,-1,-1,-1,-1]
        self.assertEqual(s.findBall(i), o)

    def test_one_three(self):
        s = Solution()
        i = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1]]
        o = [1,-1,-1,-1,-1]
        self.assertEqual(s.findBall(i), o)

    def test_two(self):
        s = Solution()
        i = [[-1]]
        o = [-1]
        self.assertEqual(s.findBall(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
        o = [0,1,2,3,4,-1]
        self.assertEqual(s.findBall(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,-1,-1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1],[-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,1],[1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1]]
        o = [-1,-1,1,-1,-1,-1,-1,10,11,-1,-1,12,13,-1,-1,-1,-1,-1,17,-1,-1,20,-1,-1,-1,-1,-1,-1,-1,-1,27,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        self.assertEqual(s.findBall(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)