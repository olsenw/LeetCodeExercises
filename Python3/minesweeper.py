# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n char matrix board representing the game board where:
    * 'M' represents an unrevealed mine,
    * 'E' represents an unrevealed empty square,
    * 'B' represents a revealed blank square that no adjacent mines (ie, above,
      below, left, right, and 4 diagonals),
    * digit ('1' to '8') represents how many mines are adjacent to this revealed
      square, and
    * 'X' represents a revealed mine.

    Given an integer array click where click = [clickr, clickc] represents the
    next click position among all the unrevealed squares ('M' or 'E').

    Return the board after revealing this position according to the following
    rules:
    1. If a mine 'M' is revealed, then the game is over. Change it to 'X'.
    2. If an empty square 'E' with no adjacent mines is revealed, then change it
       to a revealed blank 'B' and all of its adjacent unrevealed squares should
       be revealed recursively.
    3. If an empty square 'E' with at least one adjacent mine is revealed, then
       change it to a digit ('1' to '8') representing the number of adjacent
       mines.
    4. Return the board when no more squares will be revealed.
    '''
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m,n = len(board), len(board[0])
        visited = set()
        q = deque([click])
        while q:
            x,y = q.popleft()
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if board[x][y] == 'M':
                board[x][y] = 'X'
                continue
            c = 0
            e = []
            for i,j in [(x-1,y-1),(x,y-1),(x+1,y-1),
                        (x-1,y),          (x+1,y),
                        (x-1,y+1),(x,y+1),(x+1,y+1)]:
                if 0 <= i < m and 0 <= j < n:
                    if board[i][j] == 'M':
                        c += 1
                    if c == 0:
                        e.append((i,j))
            if c == 0:
                board[x][y] = 'B'
                q.extend(e)
            else:
                board[x][y] = str(c)
        return board

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
        j = [3,0]
        o = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
        self.assertEqual(s.updateBoard(i,j), o)

    def test_two(self):
        s = Solution()
        i = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
        j = [1,2]
        o = [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
        self.assertEqual(s.updateBoard(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)