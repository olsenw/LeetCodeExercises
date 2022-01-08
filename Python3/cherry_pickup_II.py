# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a row x col matrix grid representing a field of cherries where
    grid[i][j] represents the number of cherries that you can collect 
    from the (i,j) cell.

    There are two robots that can collect cherries.
    - Robot one located at the top left corner (0,0)
    - Robot two located at the top right corner (0,col-1)

    These two robots can move in the following ways:
    - From cell (i,j), a robot can move to cells (i+1,j-1), (i+1,j), 
      (i+1,j+1).
    - When a robot passes through a cell it collects all the cherries,
      leaving the cell empty.
    - When both robots visit the same cell, only one may collect the 
      cherries in that cell.
    - Both robots must remain within the bounds of the grid.
    - Both robots must reach the final row of the grid.
    '''

    # derived from the bottom down dynamic programing solution
    # https://leetcode.com/problems/cherry-pickup-ii/solution/
    # O(m*n*n) time
    # O(n*n) space   did the state compression
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # length
        m = len(grid)
        # width
        n = len(grid[0])
        # dynamic programming initialized with zero (3d array m x n x n)
        # dp[row][col1][col2] is maximum number of cherries given robot1
        # is at (row,col1) and robot2 is at (row,col2)
        dp = [[0]*n for _ in range(n)]
        dp2 = [[0]*n for _ in range(n)]
        # need to start at bottom of grid (where robots end after
        # picking up all cherries)
        for row in reversed(range(m)):
            # reuse the dp arrays
            temp = dp
            dp = dp2
            dp2 = temp
            for col1 in range(n):
                for col2 in range(n):
                    # robot1 get cherries at current grid location
                    cherries = grid[row][col1]
                    # robot2 get cherries at current grid location
                    # only if robot1 and robot2 are at different spots
                    if col1 != col2:
                        cherries += grid[row][col2]
                    # assuming not at bottom of grid
                    # get the maximum possible cherries picked up after 
                    # robot1 and robot2 move (9 possible options)
                    if row < m -1:
                        cherries += max(
                            dp2[mv1][mv2]
                            # robot1 moves
                            for mv1 in [col1, col1+1, col1-1]
                            # robot2 moves
                            for mv2 in [col2, col2+1, col2-1]
                            # bounds checking
                            if 0 <= mv1 < n and 0 <= mv2 < n
                        )
                    # update number of cherries collected
                    dp[col1][col2] = cherries
        # return maximum cherries when robot1 starts at row 0 col 0 and 
        # robot2 starts at row 0 col width-1
        return dp[0][-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
        o = 24
        self.assertEqual(s.cherryPickup(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
        o = 28
        self.assertEqual(s.cherryPickup(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,0,1],[1,2,1],[2,1,2]]
        o = 9
        self.assertEqual(s.cherryPickup(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)