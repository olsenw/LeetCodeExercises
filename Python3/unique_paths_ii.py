# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an m x n integer array grid. There is a robot initially
    located at the top-left corner (ie grid[0][0]). The robot tries to
    move to the bottom-right corner (ie grid[m-1][n-1]). The robot can
    only move either down or right at any point in time.

    An obstacle and space are marked as 1 or 0 respectively in grid. A
    path that the robot takes cannot include any square that is an
    obstacle.

    Return the number of possible unique paths that the robot can take
    to reach the bottom-right corner.
    '''
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # base case top left
        obstacleGrid[0][0] = 0 if obstacleGrid[0][0] else 1
        # first row
        for i in range(1,n):
            if obstacleGrid[0][i]:
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1]
        # first column
        for i in range(1,m):
            if obstacleGrid[i][0]:
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]
        # rest of array
        for i in range(1,m):
            if i < n:
                for j in range(i,m):
                    if obstacleGrid[j][i]:
                        obstacleGrid[j][i] = 0
                    else:
                        obstacleGrid[j][i] = obstacleGrid[j - 1][i] + obstacleGrid[j][i - 1]
            for j in range(i + 1, n):
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0,0],[0,1,0],[0,0,0]]
        o = 2
        self.assertEqual(s.uniquePathsWithObstacles(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,1],[0,0]]
        o = 1
        self.assertEqual(s.uniquePathsWithObstacles(i), o)

    def test_three(self):
        s = Solution()
        i = [[1]]
        o = 0
        self.assertEqual(s.uniquePathsWithObstacles(i), o)

    def test_four(self):
        s = Solution()
        i = [[0]]
        o = 1
        self.assertEqual(s.uniquePathsWithObstacles(i), o)

    def test_five(self):
        s = Solution()
        i = [[0],[0]]
        o = 1
        self.assertEqual(s.uniquePathsWithObstacles(i), o)

    def test_six(self):
        s = Solution()
        i = [[0,0]]
        o = 1
        self.assertEqual(s.uniquePathsWithObstacles(i), o)

    def test_seven(self):
        s = Solution()
        i = [[0,1],[0,1],[0,1],[0,0],]
        o = 1
        self.assertEqual(s.uniquePathsWithObstacles(i), o)

    def test_seven(self):
        s = Solution()
        i = [[0,0,0,0],[1,1,1,0]]
        o = 1
        self.assertEqual(s.uniquePathsWithObstacles(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)