# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from bisect import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a m x n matrix grid which is sorted in non-increasing order both
    row-wise and column-wise, return the number of negative numbers in grid.
    '''
    # brute force
    def countNegatives_brute(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    answer += 1
        return answer
    
    '''
    could also do binary search
    '''

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
        o = 8
        self.assertEqual(s.countNegatives(i), o)

    def test_two(self):
        s = Solution()
        i = [[3,2],[1,0]]
        o = 0
        self.assertEqual(s.countNegatives(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)