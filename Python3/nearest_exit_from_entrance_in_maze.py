# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an m x n matrix maze (0-indexed) with empty cells (represented as '.')
    and walls (represented as '+'). Also given the entrance to the maze, where
    entrance = [row, col] denotes the row and column of the cell to initially
    start from.

    In a single step it is possible to move one cell up, down, left, or right.
    It is not possible to step into a cell containing a wall or to step out of
    the maze. The goal is to find the nearest exit from the entrance. An exit is
    defined as an empty cell that is at the border of the maze. The entrance
    does not count as an exit.

    Return the number of steps in the shortest path from the entrance to the
    nearest exit, or -1 if no such path exists.
    '''
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze), len(maze[0])
        q = deque([(entrance[0],entrance[1],0)])
        v = {(entrance[0],entrance[1])}
        while q:
            x,y,d = q.popleft()
            if (x == 0 or y == 0 or x == m-1 or y == n-1) and d > 0:
                return d
            if x > 0 and maze[x-1][y] == '.' and (x-1,y) not in v:
                v.add((x-1,y))
                q.append((x-1,y,d+1))
            if x < m-1 and maze[x+1][y] == '.' and (x+1,y) not in v:
                v.add((x+1,y))
                q.append((x+1,y,d+1))
            if y > 0 and maze[x][y-1] == '.' and (x,y-1) not in v:
                v.add((x,y-1))
                q.append((x,y-1,d+1))
            if y < n-1 and maze[x][y+1] == '.' and (x,y+1) not in v:
                v.add((x,y+1))
                q.append((x,y+1,d+1))
        return -1

    def nearestExit_alt(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze), len(maze[0])
        q = deque([(entrance[0],entrance[1],0)])
        v = set()
        while q:
            x,y,d = q.popleft()
            if (x,y) in v or maze[x][y] == '+':
                continue
            v.add((x,y))
            if x == 0 or x == m-1 or y == 0 or y == n-1:
                if d > 0:
                    return d
            if x > 0:
                q.append((x-1,y,d+1))
            if x < m-1:
                q.append((x+1,y,d+1))
            if y > 0:
                q.append((x,y-1,d+1))
            if y < n-1:
                q.append((x,y+1,d+1))
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
        j = [1,2]
        o = 1
        self.assertEqual(s.nearestExit(i,j), o)

    def test_two(self):
        s = Solution()
        i = [["+","+","+"],[".",".","."],["+","+","+"]]
        j = [1,0]
        o = 2
        self.assertEqual(s.nearestExit(i,j), o)

    def test_three(self):
        s = Solution()
        i = [[".","+"]]
        j = [0,0]
        o = -1
        self.assertEqual(s.nearestExit(i,j), o)

    def test_four(self):
        s = Solution()
        i = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
        j = [0,1]
        o = 12
        self.assertEqual(s.nearestExit(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)