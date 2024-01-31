# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a map of a server center, represented as a m * n integer matrix grid,
    where 1 means that on that cell there is a server and 0 means that it is no
    server. Two servers are said to communicate if they are on the same row or
    on the same column.

    Return the number of servers that communicate with any other server.
    '''
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        r = [sum(r) for r in grid]
        c = [sum(c) for c in zip(*grid)]
        return sum(1 for i in range(m) for j in range(n) if grid[i][j] and (r[i] > 1 or c[j] > 1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,0],[0,1]]
        o = 0
        self.assertEqual(s.countServers(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,0],[1,1]]
        o = 3
        self.assertEqual(s.countServers(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
        o = 4
        self.assertEqual(s.countServers(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)