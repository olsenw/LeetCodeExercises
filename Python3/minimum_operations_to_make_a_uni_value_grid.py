# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer grid of size m x n and an integer x. In one operation it
    is possible to add x to or subtract x from any element in the grid.

    A uni-value grid is a grid where all the elements of it are equal.

    Return the minimum number of operations to make the grid uni-value. If it is
    note possible, return -1.
    '''
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        test = grid[0][0] % x
        flat = []
        for row in grid:
            for col in row:
                if col % x != test:
                    return -1
                flat.append(col)
        flat.sort()
        mid = flat[len(flat)//2]
        return sum(abs(f-mid)//x for f in flat)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[2,4],[6,8]]
        j = 2
        o = 4
        self.assertEqual(s.minOperations(i,j), o)

    def test_two(self):
        s = Solution()
        i = [[1,5],[2,3]]
        j = 1
        o = 5
        self.assertEqual(s.minOperations(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[1,2],[3,4]]
        j = 2
        o = -1
        self.assertEqual(s.minOperations(i,j), o)

    def test_four(self):
        s = Solution()
        i = [[2,2,2],[2,4,16],[16,16,16]]
        j = 2
        o = 28
        self.assertEqual(s.minOperations(i,j), o)

    def test_five(self):
        s = Solution()
        i = [[2,2,2],[2,4,16],[16,16,16]]
        j = 1
        o = 56
        self.assertEqual(s.minOperations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)