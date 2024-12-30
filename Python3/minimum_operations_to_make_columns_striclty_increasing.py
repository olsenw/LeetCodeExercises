# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a m x n matrix grid consisting of non-negative integers.

    In one operation it is possible to increment the value of grid[i][j] by one.

    Return the minimum number of operations needed to make all columns of grid
    strictly increasing.
    '''
    def minimumOperations(self, grid: List[List[int]]) -> int:
        answer = 0
        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if grid[i-1][j] >= grid[i][j]:
                    increment = grid[i-1][j] - grid[i][j] + 1
                    grid[i][j] += increment
                    answer += increment
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[3,2],[1,3],[3,4],[0,1]]
        o = 15
        self.assertEqual(s.minimumOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [[3,2,1],[2,1,0],[1,2,3]]
        o = 12
        self.assertEqual(s.minimumOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)