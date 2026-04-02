# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n grid. A robot starts at the top-left corner of the grid (0,0)
    and wants to reach the bottom-right corner (m-1, n-1). The robot can move
    either right or down at any point in time.

    The grid contains a value coins[i][j] in each cell:
    * If coins[i][j] >= 0, the robot gains that many coins.
    * If coins[i][j] < 0, the robot encounters a robber and the robber steals
      the absolute value of coins[i][j] coins.
    
    The robot has a special ability to neutralize robbers in at most two cells
    on its path, preventing them from stealing coins in those cells.

    Note: The robot's total coins can be negative.

    Return the maximum profit the robot can gain on the route.
    '''
    # too much memory used (solved 577 / 579)
    def maximumAmount_memory_limit_exceeded(self, coins: List[List[int]]) -> int:
        m,n = len(coins), len(coins[0])
        @cache
        def dp(i:int,j:int,robber:int) -> int:
            if i == m-1 and j == n-1:
                return 0
            answer = float('-inf')
            if i < m-1:
                answer = max(answer, coins[i+1][j] + dp(i+1,j,robber))
                if coins[i+1][j] < 0 and robber > 0:
                    # answer = max(answer, abs(coins[i+1][j]) + dp(i+1,j,robber-1))
                    answer = max(answer, dp(i+1,j,robber-1))
            if j < n-1:
                answer = max(answer, coins[i][j+1] + dp(i,j+1,robber))
                if coins[i][j+1] < 0 and robber > 0:
                    # answer = max(answer, abs(coins[i][j+1]) + dp(i,j+1,robber-1))
                    answer = max(answer, dp(i,j+1,robber-1))
            return answer
        dp.cache_clear()
        if coins[0][0] >= 0:
            return coins[0][0] + dp(0,0,2)
        # return max(coins[0][0] + dp(0,0,2), abs(coins[0][0]) + dp(0,0,1))
        return max(coins[0][0] + dp(0,0,2), dp(0,0,1))

    def maximumAmount_incomplete(self, coins: List[List[int]]) -> int:
        m,n,neutralize = len(coins), len(coins[0]), 3
        dp = [[[float('-inf')] * neutralize for _ in range(n)] for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                # end of the coins array
                if i == m-1 and j == n-1:
                    dp[i][j] = [
                        coins[i][j], # end of coins neutralized zero robbers
                        0, # end of coins neutralized one robber
                        coins[i][j], # end of coins neutralized two robbers
                    ]
                # last row in coins array
                elif i == m-1:
                    dp[i][j] = [
                        coins[i][j] + max()
                    ]
                # last column in coins array
                elif j == n-1:
                    dp[i][j]
                # all other locations
                else:
                    dp[i][j]
        return max(dp[0][0])

    def maximumAmount(self, coins: List[List[int]]) -> int:
        m,n,neutralize = len(coins), len(coins[0]), 3
        # dp = [[[float('-inf')] * neutralize for _ in range(n)] for _ in range(m)]
        dp = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = [
                        coins[i][j],
                        0,
                        0
                    ]
                elif i == 0:
                    dp[i][j] = [
                        coins[i][j] + dp[i][j-1][0],
                        max(coins[i][j] + dp[i][j-1][1], dp[i][j-1][0]),
                        max(coins[i][j] + dp[i][j-1][2], dp[i][j-1][1])
                    ]
                elif j == 0:
                    dp[i][j] = [
                        coins[i][j] + dp[i-1][j][0],
                        max(coins[i][j] + dp[i-1][j][1], dp[i-1][j][0]),
                        max(coins[i][j] + dp[i-1][j][2], dp[i-1][j][1])
                    ]
                else:
                    dp[i][j] = [
                        coins[i][j] + max(dp[i-1][j][0], dp[i][j-1][0]),
                        max(coins[i][j] + dp[i-1][j][1], coins[i][j] + dp[i][j-1][1], dp[i-1][j][0], dp[i][j-1][0]),
                        max(coins[i][j] + dp[i-1][j][2], coins[i][j] + dp[i][j-1][2], dp[i-1][j][1], dp[i][j-1][1])
                    ]
        return max(dp[-1][-1])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,-1],[1,-2,3],[2,-3,4]]
        o = 8
        self.assertEqual(s.maximumAmount(i), o)

    def test_two(self):
        s = Solution()
        i = [[10,10,10],[10,10,10]]
        o = 40
        self.assertEqual(s.maximumAmount(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)