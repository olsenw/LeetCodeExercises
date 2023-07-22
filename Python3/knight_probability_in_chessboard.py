# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    On an n x n chessboard, a knight starts at the cell (row, column) and
    attempts to make exactly k moves. The rows and columns are 0-indexed, so the
    top-left cell is (0,0), and the bottom-right cell is (n-1, n-1).

    A chess knight has eight possible moves it can make, as illustrated on
    LeetCode problem description. Each move is two cells in a cardinal
    direction, then one cell in an orthogonal direction.

    Each time the knight is to move, it chooses one of eight possible moves
    uniformly at random (even if the piece would go off the chessboard) and
    moves there.

    The knight continues moving until it has made exactly k moves or has moved
    off the chessboard.

    Return the probability that the knight remains on the board after it has
    stopped moving.
    '''
    def knightProbability_tle(self, n: int, k: int, row: int, column: int) -> float:
        off, on = 0, 0
        def dfs(r,c,d):
            nonlocal on,off
            if r < 0 or r >= n or c < 0 or c >= n:
                off += 8 ** (k - d)
                return
            if k == d:
                on += 1
                return
            dfs(r-2,c-1,d+1)
            dfs(r-2,c+1,d+1)
            dfs(r+2,c-1,d+1)
            dfs(r+2,c+1,d+1)
            dfs(r-1,c-2,d+1)
            dfs(r+1,c-2,d+1)
            dfs(r-1,c+2,d+1)
            dfs(r+1,c+2,d+1)
        dfs(row,column,0)
        return on / (off + on)

    def knightProbability_wrong(self, n: int, k: int, row: int, column: int) -> float:
        # chance of knight on move m being at (r,c)
        dp = [[[0.0] * n for _ in range(n)] for _ in range(k+1)]
        # always on board before being moved
        for i in range(n):
            for j in range(n):
                dp[0][i][j] = 1.0
        # calculate probability for each move based on last move
        for i in range(1,k+1):
            for j in range(n):
                for l in range(n):
                    for x,y in [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]:
                        if 0 <= j+x < n and 0 <= l+y < n:
                            dp[i][j][l] += dp[i-1][j+x][l+y]
        return sum(dp[k][i][j] for i in range(n) for j in range(n))

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]
        # chance of knight on move m being at (r,c)
        dp = [[[0.0] * n for _ in range(n)] for _ in range(k+1)]
        # always on board before being moved
        dp[0][row][column] = 1.0
        for moves in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for x,y in directions:
                        if 0 <= i - x < n and 0 <= j - y < n:
                            dp[moves][i][j] += dp[moves - 1][i - x][j - y]
                    dp[moves][i][j] /= 8
        return sum(dp[k][i][j] for i in range(n) for j in range(n))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3,2,0,0
        o = 0.06250
        self.assertEqual(s.knightProbability(*i), o)

    def test_two(self):
        s = Solution()
        i = 1,0,0,0
        o = 1.0
        self.assertEqual(s.knightProbability(*i), o)

    def test_three(self):
        s = Solution()
        i = 25,100,12,12
        o = 0.04743
        self.assertEqual(s.knightProbability(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)