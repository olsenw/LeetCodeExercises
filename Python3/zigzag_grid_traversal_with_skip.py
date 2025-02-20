# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n 2D array grid of positive integers.

    Traverse grid in a zigzag pattern while skipping every alternate cell.

    Zigzag pattern traversal is defined as following the below actions:
    * Start at the top-left cell (0, 0).
    * Move right within a row until the end of the row is reached.
    * Drop down to the next row, then traverse left until the beginning of the
      row is reached.
    * Continue alternating between right and left traversal until every row has
      been traversed.

    Note that it is required to skip every alternate cell during the traversal.

    Return an array of integers result containing, in order, the value of the
    cells visited during the zigzag traversal with skips.
    '''
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid), len(grid[0])
        skip = False
        left = False
        answer = []
        for i in range(m):
            r = range(n-1,-1,-1) if left else range(n)
            for j in r:
                if not skip:
                    answer.append(grid[i][j])
                skip = not skip
            left = not left
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2],[3,4]]
        o = [1,4]
        self.assertEqual(s.zigzagTraversal(i), o)

    def test_two(self):
        s = Solution()
        i = [[2,1],[2,1],[2,1]]
        o = [2,1,2]
        self.assertEqual(s.zigzagTraversal(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        o = [1,3,5,7,9]
        self.assertEqual(s.zigzagTraversal(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)