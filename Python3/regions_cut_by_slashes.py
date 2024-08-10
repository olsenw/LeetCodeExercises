# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists
    of a '/', '\\' blank space ' '. These characters divide the square into
    contiguous regions.

    Given the grid grid represented as string array, return the number of
    regions.

    Note that backslash characters are escaped, so a '\' is represented as '\\'. 
    '''
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        m = n * 3
        graph = [[0] * m for _ in range(m)]
        for i in range(n):
            for j in range(n):
                x,y = 3*i, 3*j
                if grid[i][j] == '/':
                    graph[x+2][y] = 1
                    graph[x+1][y+1] = 1
                    graph[x][y+2] = 1
                elif grid[i][j] == '\\':
                    graph[x][y] = 1
                    graph[x+1][y+1] = 1
                    graph[x+2][y+2] = 1
        answer = 0
        for i in range(m):
            for j in range(m):
                if graph[i][j] == 0:
                    answer += 1
                    q = deque([(i,j)])
                    while q:
                        x,y = q.popleft()
                        if x < 0 or x == m or y < 0 or y == m or graph[x][y]:
                            continue
                        graph[x][y] = 1
                        q.append((x-1,y))
                        q.append((x+1,y))
                        q.append((x,y-1))
                        q.append((x,y+1))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [" /","/ "]
        o = 2
        self.assertEqual(s.regionsBySlashes(i), o)

    def test_two(self):
        s = Solution()
        i = [" /","  "]
        o = 1
        self.assertEqual(s.regionsBySlashes(i), o)

    def test_three(self):
        s = Solution()
        i = ["/\\","\\/"]
        o = 5
        self.assertEqual(s.regionsBySlashes(i), o)

    def test_four(self):
        s = Solution()
        i = ["//","/ "]
        o = 3
        self.assertEqual(s.regionsBySlashes(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)