# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer matrix grid of size n x m, where each element is either
    0, 1, or 2.

    A V-shaped diagonal segment is defied as:
    * The segment starts with 1.
    * The segments elements follow this infinite sequence: 2, 0, 2, 0, ...
    * The segment:
        * Starts along a diagonal direction (top-left to bottom-right,
          bottom-right to top-left, top-right to bottom-left, or bottom-left to
          top-right)
        * Continues the sequence in the same diagonal direction.
        * Makes at most one clockwise 90-degree turn to another diagonal
          direction while maintaining the sequence.
    
    Return the length of the longest V-shaped diagonal segment. If no valid
    segment exists, return 0.
    '''
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        # from cell grid[i][j] and going in a direction
        # 1, 2, 3, 4 -> up-left, up right, down right, down left
        # 5, 6, 7, 8 -> same but allow 90 degree clockwise turn
        @cache
        def dfs(i:int, j:int, dir:int) -> int:
            answer = 1
            target = 0 if grid[i][j] == 2 else 2
            if (dir == 1 or dir == 5) and i > 0 and j > 0 and grid[i-1][j-1] == target:
                answer = max(answer, 1 + dfs(i-1,j-1,dir))
            if dir == 5 and i > 0 and j < n - 1 and grid[i-1][j+1] == target:
                answer = max(answer, 1 + dfs(i-1,j+1,2))
            if (dir == 2 or dir == 6) and i > 0 and j < n - 1 and grid[i-1][j+1] == target:
                answer = max(answer, 1 + dfs(i-1,j+1,dir))
            if dir == 6 and i < m - 1 and j < n - 1 and grid[i+1][j+1] == target:
                answer = max(answer, 1 + dfs(i+1,j+1,3))
            if (dir == 3 or dir == 7) and i < m - 1 and j < n - 1 and grid[i+1][j+1] == target:
                answer = max(answer, 1 + dfs(i+1,j+1,dir))
            if dir == 7 and i < m - 1 and j > 0 and grid[i+1][j-1] == target:
                answer = max(answer, 1 + dfs(i+1,j-1,4))
            if (dir == 4 or dir == 8) and i < m - 1 and j > 0 and grid[i+1][j-1] == target:
                answer = max(answer, 1 + dfs(i+1,j-1,dir))
            if dir == 8 and i > 0 and j > 0 and grid[i-1][j-1] == target:
                answer = max(answer, 1 + dfs(i-1,j-1,1))
            return answer
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                a = 1
                if i > 0 and j > 0 and grid[i-1][j-1] == 2:
                    a = max(a, 1 + dfs(i-1,j-1,5))
                if i > 0 and j < n - 1 and grid[i-1][j+1] == 2:
                    a = max(a, 1 + dfs(i-1,j+1,6))
                if i < m - 1 and j < n - 1 and grid[i+1][j+1] == 2:
                    a = max(a, 1 + dfs(i+1,j+1,7))
                if i < m - 1 and j > 0 and grid[i+1][j-1] == 2:
                    a = max(a, 1 + dfs(i+1,j-1,8))
                answer = max(answer, a)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
        o = 5
        self.assertEqual(s.lenOfVDiagonal(i), o)

    def test_two(self):
        s = Solution()
        i = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
        o = 4
        self.assertEqual(s.lenOfVDiagonal(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
        o = 5
        self.assertEqual(s.lenOfVDiagonal(i), o)

    def test_four(self):
        s = Solution()
        i = [[1]]
        o = 1
        self.assertEqual(s.lenOfVDiagonal(i), o)

    def test_five(self):
        s = Solution()
        i = [[0,1,0,0,0,0,0],[2,1,1,2,1,2,2],[1,1,1,2,2,1,0]]
        o = 5
        self.assertEqual(s.lenOfVDiagonal(i), o)

    def test_six(self):
        s = Solution()
        i = [[0,0,2,2,0,1,0,1,1,0,2,0,1],
             [1,1,1,1,0,0,0,2,2,1,2,1,2],
             [0,0,1,1,2,1,0,0,2,1,0,2,0]]
        o = 4
        self.assertEqual(s.lenOfVDiagonal(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)