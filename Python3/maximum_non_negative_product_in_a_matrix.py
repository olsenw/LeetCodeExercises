# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a m x n matrix grid. Initially start at the top-left corner (0,0), and
    in each step it is possible to move right or down in the matrix.

    Among all possible paths starting from the top-left corner (0,0) and ending
    in the bottom-right corner (m-1,n-1), find the path with the maximum
    non-negative product. The product of a path is the product of all integers
    in the grid cells visited along the path.

    Return the maximum non-negative product modulo 10^9 + 7. If the maximum
    product is negative, return -1.

    Notice that the modulo is performed after getting the maximum product.
    '''
    # this dfs search does not work due to flip flop of negative multiplication
    def maxProductPath_fails(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        def dfs(i:int,j:int) -> int:
            if i == m-1 and j == n-1:
                return grid[i][j]
            right = None
            down = None
            if i < m-1:
                down = grid[i][j] * dfs(i+1,j)
            if j < n-1:
                right = grid[i][j] * dfs(i,j+1)
            if down and right:
                return max(down, right)
            elif down:
                return down
            else:
                return right
        answer = dfs(0,0)
        return -1 if answer < 0 else answer

    # time limit exceeded
    # too large of space
    def maxProductPath_tle(self, grid: List[List[int]]) -> int:
        answer = -float('inf')
        m,n = len(grid), len(grid[0])
        def dfs(value:int, i:int, j:int) -> int:
            nonlocal answer
            if i == m-1 and j == n-1:
                answer = max(answer, grid[i][j] * value)
                return
            if i < m - 1:
                dfs(grid[i][j] * value, i+1, j)
            if j < n - 1:
                dfs(grid[i][j] * value, i, j+1)
            return
        dfs(1,0,0)
        return -1 if answer < 0 else answer % (10**9+7)

    # based on hint
    # fails incorrect answer
    def maxProductPath_fails(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        @cache
        def dfsMinimum(i:int,j:int) -> int:
            if i == m-1 and j == n-1:
                return grid[i][j]
            down = None
            left = None
            if i < m - 1:
                down = grid[i][j] * dfsMinimum(i+1,j)
                down = min(down,grid[i][j] * dfsMaximum(i+1,j))
            if j < n - 1:
                left = grid[i][j] * dfsMinimum(i,j+1)
                left = min(left, grid[i][j] * dfsMaximum(i,j+1))
            if down is not None and left is not None:
                return min(down,left)
            if down is not None:
                return down
            return left
        @cache
        def dfsMaximum(i:int,j:int) -> int:
            if i == m-1 and j == n-1:
                return grid[i][j]
            down = None
            left = None
            if i < m - 1:
                down = grid[i][j] * dfsMinimum(i+1,j)
                down = max(down,grid[i][j] * dfsMaximum(i+1,j))
            if j < n - 1:
                left = grid[i][j] * dfsMinimum(i,j+1)
                left = max(left, grid[i][j] * dfsMaximum(i,j+1))
            if down is not None and left is not None:
                return max(down,left)
            if down is not None:
                return down
            return left
        answer = dfsMaximum(0,0) % (10**9+7)
        return -1 if answer < 0 else answer

    def maxProductPath(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        @cache
        def dp(i:int,j:int) -> List[int]:
            if i == m-1 and j == n-1:
                return [grid[i][j]]*2
            aMax = -float('inf')
            aMin = float('inf')
            if i < m-1:
                x,y = dp(i+1,j)
                aMax = max(aMax, grid[i][j] * x, grid[i][j] * y)
                aMin = min(aMin, grid[i][j] * x, grid[i][j] * y)
            if j < n-1:
                x,y = dp(i,j+1)
                aMax = max(aMax, grid[i][j] * x, grid[i][j] * y)
                aMin = min(aMin, grid[i][j] * x, grid[i][j] * y)
            return [aMin,aMax]
        answer = max(dp(0,0))
        return -1 if answer < 0 else answer % (10**9+7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
        o = -1
        self.assertEqual(s.maxProductPath(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,-2,1],[1,-2,1],[3,-4,1]]
        o = 8
        self.assertEqual(s.maxProductPath(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,3],[0,-4]]
        o = 0
        self.assertEqual(s.maxProductPath(i), o)

    def test_four(self):
        s = Solution()
        i = [[-4,1,-1,4,1,-3,-2,1,3,-2,-4,-3,-3,-3],[2,-2,0,2,3,-3,0,-3,-2,-2,-4,1,1,-2],[4,-4,2,-3,-4,-4,-2,-3,2,0,-1,3,3,0],[2,2,4,-4,-1,-4,-1,-1,-3,2,0,2,1,-1],[0,0,-3,2,-4,-2,-1,0,1,-3,-3,0,3,1],[-4,2,-4,3,3,1,0,3,1,3,-2,-4,-2,0],[-3,-4,3,1,-3,-3,-1,-2,-3,-3,2,2,1,2],[-2,2,-3,4,1,-2,2,2,1,0,-3,0,3,0],[-4,-1,0,-3,2,2,2,-4,-4,3,-3,-4,-4,-4],[2,-2,3,1,-3,1,4,0,0,3,-4,3,1,3],[0,4,1,2,1,2,-3,-2,1,2,-1,-3,-1,-3],[4,0,4,-2,-3,2,-4,-1,1,3,0,-2,0,-2]]
        o = 205014489
        self.assertEqual(s.maxProductPath(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)