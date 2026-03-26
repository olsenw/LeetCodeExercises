# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n matrix grid of positive integers. Determine if it is possible
    to make either one horizontal or one vertical cut on the grid such that:
    * Each of the two resulting sections formed by the cut is non-empty.
    * The sum of elements in both sections is equal, or can be made by
      discounting at most one single cell in total (from either section).
    * If a cell is discounted, the rest of the section must remain connected.

    Return true if such a partition exists; otherwise, return false.

    Note: A section is connected if every cell in it can be reached from any
    other cell by moving up,down,left, or right through other cells in the
    section.
    '''
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # solved horizontal case
        def solve(grid: List[List[int]]) -> bool:
            m,n = len(grid), len(grid[0])
            if m == 1:
                return False
            # adding a zero only works because problem constraints state values are in range 1 to 10^5
            totalFrequency = Counter([0])
            totalSum = 0
            for i in range(m):
                for j in range(n):
                    totalFrequency[grid[i][j]] += 1
                    totalSum += grid[i][j]
            currentFrequency = Counter()
            currentSum = 0
            # first row special case
            for j in range(n):
                totalFrequency[grid[0][j]] -= 1
                currentFrequency[grid[0][j]] += 1
                currentSum += grid[0][j]
            diff = totalSum - currentSum - currentSum
            # special case of only two rows
            if m == 2:
                return diff == 0 or -diff == grid[0][0] or -diff == grid[0][-1] or diff == grid[-1][0] or diff == grid[-1][-1]
            # check if single first row
            if n > 1 and (totalFrequency[diff] or -diff == grid[0][0] or -diff == grid[0][-1]):
                return True
            elif diff == 0 or diff == grid[1][0] or diff == grid[-1][-1]:
                return True
            # all other rows where guaranteed connected
            for i in range(1,m-2):
                for j in range(n):
                    totalFrequency[grid[i][j]] -= 1
                    currentFrequency[grid[i][j]] += 1
                    currentSum += grid[i][j]
                diff = totalSum - currentSum - currentSum
                if n > 1 and (totalFrequency[diff] or currentFrequency[-diff]):
                    return True
                elif diff == 0 or -diff == grid[0][0] or -diff == grid[i][0] or diff == grid[i+1][0] or diff == grid[-1][-1]:
                    return True
            # final row special case
            for j in range(n):
                totalFrequency[grid[-2][j]] -= 1
                currentFrequency[grid[-2][j]] += 1
                currentSum += grid[-2][j]
            diff = totalSum - currentSum - currentSum
            if n > 1 and (diff == 0 or currentFrequency[-diff] or diff == grid[-1][0] or diff == grid[-1][-1]):
                return True
            elif diff == 0 or -diff == grid[0][0] or -diff == grid[-2][-1]:
                return True
            return False
        # horizontal solve
        if solve(grid):
            return True
        # rotate array for vertical solve
        m,n = len(grid), len(grid[0])
        grid = [[grid[i][j] for i in range(m)] for j in range(n)]
        return solve(grid)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,4],[2,3]]
        o = True
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2],[3,4]]
        o = True
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2,4],[2,3,5]]
        o = False
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_four(self):
        s = Solution()
        i = [[4,1,8],[3,2,6]]
        o = False
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_five(self):
        s = Solution()
        i = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
        o = True
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_six(self):
        s = Solution()
        i = [[1,1,1],[1,1,1],[3,3,4]]
        o = True
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_seven(self):
        s = Solution()
        i = [[1,1,1],[1,1,1],[3,4,3]]
        o = False
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_eight(self):
        s = Solution()
        i = [[1,8,2],[1,1,1]]
        o = True
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_nine(self):
        s = Solution()
        i = [[29700],[29700]]
        o = True
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_ten(self):
        s = Solution()
        i = [[10,5,4,5]]
        o = False
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_eleven(self):
        s = Solution()
        i = [[100000],[86218],[100000]]
        o = True
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_twelve(self):
        s = Solution()
        i = [[4,4,4],[2,2,1],[1,1,1]]
        o = True
        self.assertEqual(s.canPartitionGrid(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)