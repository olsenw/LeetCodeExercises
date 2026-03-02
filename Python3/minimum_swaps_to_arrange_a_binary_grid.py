# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an n x n binary grid, in one step it is possible to choose two
    adjacent rows of the grid and swap them.

    A grid is said to be valid if all the cells above the main diagonal are 
    zeros.

    Return the minimum number of steps needed to make the grid valid, or -1 if
    the grid cannot be valid.

    The main diagonal of a grid is the diagonal that starts at cell (1,1) and
    ends at cell (n,n).
    '''
    # based on hints
    # Will detect if possible answer
    # does not track the sorting steps needed
    def minSwaps_incorrect(self, grid: List[List[int]]) -> int:
        n = len(grid)
        answer = 0
        right = [0] * n
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    right[i] = j
        # right.sort()
        for i,j in enumerate(sorted(right)):
            if j > i:
                return -1
        return answer

    # based on LeetCode editorial
    # https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/editorial/?envType=daily-question&envId=2026-03-02
    # the big assumption is that allow rows prior to i are valid, and therefore
    # only need to swap a lower row to meet the diagonal condition
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # locate the rightmost 1 for each row in grid
        right = [-1] * n
        for i in range(n):
            for j in range(n-1,-1,-1):
                if grid[i][j] == 1:
                    right[i] = j
                    break
        # simulate the number of swaps needed
        answer = 0
        for i in range(n):
            # row to swap
            k = -1
            # find the first row that meets diagonal below i
            for j in range(i,n):
                if right[j] <= i:
                    answer += j - i
                    k = j
                    break
            # no row found unable to sort array
            if k == -1:
                return -1
            # swap rows as needed (bubble up)
            for j in range(k,i,-1):
                right[j], right[j-1] = right[j-1], right[j]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0,1],[1,1,0],[1,0,0]]
        o = 3
        self.assertEqual(s.minSwaps(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
        o = -1
        self.assertEqual(s.minSwaps(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,0,0],[1,1,0],[1,1,1]]
        o = 0
        self.assertEqual(s.minSwaps(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)