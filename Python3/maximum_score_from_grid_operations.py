# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D matrix grid of size n x n. Initially all cells of the the grid
    are colored white. In one operation, it is possible to select any cell of
    indices (i,j), and color black all the cells of the jth column starting from
    the top row down to the ith row.

    The grid score is the sum of all grid[i][j] such that cell (i,j) is white
    and it has a horizontally adjacent black cell.

    Return the maximum score that can be achieved after some number of
    operations.
    '''
    # based on leetcode editorial
    # https://leetcode.com/problems/maximum-score-from-grid-operations/editorial/?envType=daily-question&envId=2026-04-29
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # literal corner case (impossible to score)
        if n == 1:
            return 0
        # dp[column index][height current][height previous]
        dp = [[[0] * (n+1) for _ in range(n+1)] for _ in range(n)]
        prevMax = [[0] * (n+1) for _ in range(n+1)]
        prevSuffixMax = [[0] * (n+1) for _ in range(n+1)]
        # prefix sum columns
        colSum = [[0] * (n+1) for _ in range(n)]
        for j in range(n):
            for i in range(1,n+1):
                # note the rotation in indexing (down in grid, is right in colSum)
                colSum[j][i] = colSum[j][i-1] + grid[i-1][j]
        # precalculate
        for i in range(1,n):
            for currH in range(n+1):
                for prevH in range(n+1):
                    # able to include portion of column in i-1
                    if currH <= prevH:
                        additional = colSum[i][prevH] - colSum[i][currH]
                        dp[i][currH][prevH] = max(
                            dp[i][currH][prevH],
                            prevSuffixMax[prevH][0] + additional
                        )
                    # only able to add partial as current height blocks previous column
                    else:
                        additional = colSum[i-1][currH] - colSum[i-1][prevH]
                        dp[i][currH][prevH] = max(
                            dp[i][currH][prevH],
                            prevSuffixMax[prevH][currH],
                            prevMax[prevH][currH] + additional
                        )
            for currH in range(n+1):
                # calculate how much needs to be removed due to overlaps
                prevMax[currH][0] = dp[i][currH][0]
                for prevH in range(1,n+1):
                    penalty = colSum[i][prevH] - colSum[i][currH] if prevH > currH else 0
                    prevMax[currH][prevH] = max(
                        prevMax[currH][prevH - 1],
                        dp[i][currH][prevH] - penalty
                    )
                prevSuffixMax[currH][n] = dp[i][currH][n]
                for prevH in range(n-1,-1,-1):
                    prevSuffixMax[currH][prevH] = max(
                        prevSuffixMax[currH][prevH+1],
                        dp[i][currH][prevH]
                    )
        answer = 0
        for k in range(n+1):
            answer = max(
                answer,
                dp[n-1][n][k],
                dp[n-1][0][k]
            )
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]
        o = 11
        self.assertEqual(s.maximumScore(i), o)

    def test_two(self):
        s = Solution()
        i = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]
        o = 94
        self.assertEqual(s.maximumScore(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)