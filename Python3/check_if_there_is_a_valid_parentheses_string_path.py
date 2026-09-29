# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A parentheses string is a non-empty string consisting only of '(' and ')'.
    It is valid if any of the following condition is true:
    * It is ().
    * It can be written as AB (A concatenated with B), where A and B are valid
      parentheses strings.
    * It can be written as (A), where A is a valid parentheses string.

    Given an m x n matrix of parentheses grid. A valid parentheses string path
    in the grid is a path satisfying all of the following conditions:
    * The path starts from the upper left cell (0, 0).
    * The path ends at the bottom right cell (m-1, n-1).
    * The path only ever moves down or right.
    * The resulting parentheses formed by the path is valid.

    Return true if there exists a valid parentheses string path in the grid.
    Otherwise, return false.
    '''
    def hasValidPath_fails(self, grid: list[list[str]]) -> bool:
        m,n = len(grid)-1, len(grid[0])-1
        # left,right = 0,0
        @cache
        def dfs(i,j,left,right) -> bool:
            # nonlocal left, right
            if i == m and j == n:
                return left == right
            if grid[i][j] == '(':
                left += 1
            else:
                right += 1
            if left < right:
                return False
            answer = False
            if j < n:
                answer |= dfs(i,j+1,left,right)
            if i < m:
                answer |= dfs(i+1,j,left,right)
            if grid[i][j] == '(':
                left -= 1
            else:
                right -= 1
            return answer
        return dfs(0,0,0,0)

    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m,n = len(grid)-1, len(grid[0])-1
        @cache
        def dfs(i,j,open) -> bool:
            open += 1 if grid[i][j] == '(' else -1
            if open < 0:
                return False
            if i == m and j == n:
                return open == 0
            if j < n and dfs(i,j+1,open):
                return True
            if i < m and dfs(i+1,j,open):
                return True
            return False
        return dfs(0,0,0)

'''
Can improve run time by adding early termination conditions

Start: Check for impossible puzzles

DFS: Check if possible to complete closing brackets

See other Leetcode solutions for examples
'''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
        o = True
        self.assertEqual(s.hasValidPath(i), o)

    def test_two(self):
        s = Solution()
        i = [[")",")"],["(","("]]
        o = False
        self.assertEqual(s.hasValidPath(i), o)

    def test_three(self):
        s = Solution()
        i = [["("] * 100 for _ in range(100)]
        o = False
        self.assertEqual(s.hasValidPath(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)