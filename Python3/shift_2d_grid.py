# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# used to chain together iterators
from itertools import chain

class Solution:
    '''
    Given a 2D grid of size m x n and an integer k, shift grid k times.

    In one shift operation:
    * Element at grid[i][j] moves to grid[i][j + 1].
    * Element at grid[i][n - 1] moves to grid[i + 1][0].
    * Element at grid[m - 1][n - 1] moves to grid[0][0].

    Return the 2D grid after applying the shift operation k times
    '''
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # dimensions of array
        m = len(grid)
        n = len(grid[0])
        # length flattened array
        mn = m * n
        # adjust k for redundant shifts
        k %= mn
        # copy
        a = [[0] * n for _ in range(m)]
        for g in chain.from_iterable(grid):
            x = k // n
            y = k % n
            a[x][y] = g
            k = k + 1 if k + 1 < mn else 0
        return a

    def shiftGrid_alt(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flatten = list(chain.from_iterable(grid))
        k %= len(flatten)
        f = chain(flatten[-k:], flatten[:-k])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = next(f)
        return grid
    
    # copied from leetcode sample submissions 156ms
    # saved because this seems to be faster than using itertools
    def shiftGrid_leetcode(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r = len(grid)
        c = len(grid[0])
        flatten = [i for j in grid for i in j]
        k%=len(flatten)
        flatten = flatten[-k:] + flatten[:-k]
        f = 0
        for i in range(r):
            for j in range(c):
                grid[i][j] = flatten[f]
                f += 1
        return grid

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        j = 1
        o = [[9,1,2],[3,4,5],[6,7,8]]
        self.assertEqual(s.shiftGrid(i, j), o)
        self.assertEqual(s.shiftGrid_alt(i, j), o)

    def test_two(self):
        s = Solution()
        i = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
        j = 4
        o = [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
        self.assertEqual(s.shiftGrid(i, j), o)
        self.assertEqual(s.shiftGrid_alt(i, j), o)

    def test_three(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        j = 9
        o = [[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(s.shiftGrid(i, j), o)
        self.assertEqual(s.shiftGrid_alt(i, j), o)

    def test_four(self):
        s = Solution()
        i = [[1],[2],[3],[4],[7],[6],[5]]
        j = 23
        o = [[6],[5],[1],[2],[3],[4],[7]]
        self.assertEqual(s.shiftGrid(i, j), o)
        self.assertEqual(s.shiftGrid_alt(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)