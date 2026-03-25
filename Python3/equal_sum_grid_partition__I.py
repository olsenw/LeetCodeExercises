# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n matrix grid of positive integers. Determine if it possible to
    make either one horizontal or one vertical cut on the grid such that:
    * Each of the two resulting sections formed by the cut is non-empty.
    * The sum of the elements in both sections is equal.

    Return true if such a partition exists; otherwise return false.
    '''
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n = len(grid), len(grid[0])
        prefix = [sum(grid[0])]
        for i in range(1,m):
            prefix.append(prefix[-1] + sum(grid[i]))
        for i in range(m-1):
            if prefix[i] == prefix[-1] - prefix[i]:
                return True
        prefix = []
        p = 0
        for j in range(n):
            for i in range(m):
                p += grid[i][j]
            prefix.append(p)
        for i in range(n-1):
            if prefix[i] == prefix[-1] - prefix[i]:
                return True
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,4],[2,3]]
        o = True
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,3],[2,4]]
        o = False
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_three(self):
        s = Solution()
        i = [[2,1],[3,4]]
        o = True
        self.assertEqual(s.canPartitionGrid(i), o)

    def test_four(self):
        s = Solution()
        i = [[100000,100000,92687]]
        o = False
        self.assertEqual(s.canPartitionGrid(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)