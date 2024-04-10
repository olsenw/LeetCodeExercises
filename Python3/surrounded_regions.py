# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n matrix board containing 'X' and 'O', capture all regions that
    are 4 directionally surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in the surrounded
    region.
    '''
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        examined = set()
        def bfs(a:int, b:int) -> tuple[set, bool]:
            captured = True
            visited = set()
            queue = deque([(a,b)])
            while queue:
                i,j = queue.popleft()
                if (i,j) in visited or board[i][j] == 'X':
                    continue
                visited.add((i,j))
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    captured = False
                if i > 0:
                    queue.append((i-1,j))
                if i < m - 1:
                    queue.append((i+1,j))
                if j > 0:
                    queue.append((i,j-1))
                if j < n - 1:
                    queue.append((i,j+1))
            return visited, captured
        for i in range(m):
            for j in range(n):
                if (i,j) not in examined and board[i][j] == 'O':
                    a,b = bfs(i,j)
                    examined.update(a)
                    if b:
                        for x,y in a:
                            board[x][y] = 'X'

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        o = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        s.solve(i)
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = [["X"]]
        o = [["X"]]
        s.solve(i)
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)