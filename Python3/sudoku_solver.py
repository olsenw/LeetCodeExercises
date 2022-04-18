# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional, Tuple

from collections import deque
from copy import deepcopy

class Board:

    values = {1 << i : str(i + 1) for i in range(9)}

    def __init__(self, board: List[List[str]]):
        self.b = [[0 if j == '.' else 1 << int(j) - 1 for j in i] for i in board]
        self.r = [self.row(i) for i in range(9)]
        self.c = [self.col(i) for i in range(9)]
        self.s = [self.box(i) for i in range(9)]
    
    # returns bit mask of all values in row
    def row(self, n: int) -> int:
        m = 0b111111111
        for i in range(9):
            m ^= self.b[n][i]
        return m

    # returns bit mask of all values in column
    def col(self, n: int) -> int:
        m = 0b111111111
        for i in range(9):
            m ^= self.b[i][n]
        return m

    # returns bit mask of all values in box
    def box(self, n: int) -> int:
        x = (n // 3) * 3
        y = (n % 3) * 3
        m = 0b111111111
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                m ^= self.b[i][j]
        return m

    # is the board in a solved state
    def solved(self):
        return sum(self.r) + sum(self.c) + sum(self.s) == 0

    # attempt to fill obvious options
    def fill(self):
        filled = False
        test = True
        while test:
            test = False
            for i in range(9):
                for j in range(9):
                    if self.b[i][j] not in Board.values:
                        k = i // 3 * 3 + j // 3
                        m = self.r[i] & self.c[j] & self.s[k]
                        if m in Board.values:
                            self.place(i,j,k,m)
                            # print(i+1,j+1,k+1,'->',v[m])
                            test = True
            filled = filled or test
        return filled
    
    # place a value on the board, updates accordingly
    def place(self, i, j, k, m):
        self.b[i][j] = m
        self.r[i] = Board.row(self,i)
        self.c[j] = Board.col(self,j)
        self.s[k] = Board.box(self,k)
    
    # returns an encouraged location and possible guesses
    def guesses(self) -> Optional[Tuple[int, int, List[int]]]:
        def bits(n: int) -> int:
            c = 0
            while n > 0:
                c += n & 1
                n >>= 1
            return c
        x, y, z, g, b = 0, 0, 0, 0, 10
        for i in range(9):
            for j in range(9):
                if self.b[i][j] not in Board.values:
                    k = i // 3 * 3 + j // 3
                    m = self.r[i] & self.c[j] & self.s[k]
                    l = bits(m)
                    if 0 < l < b:
                        x, y, z, g, b = i, j, k, m, l
        if 1 < b < 10:
            l = [1 << i for i in range(9) if 1 << i & g]
            return (x,y,z,l)
        return None

class Solution:
    '''
    Write a program to solve a Sudoku puzzle by filling the empty cells.

    A sudoku solution must satisfy all of the following rules:
    1) Each of the digits 1-9 must occur exactly once in each row.
    2) Each of the digits 1-9 must occur exactly once in each column.
    3) Each of the digits 1-9 must occur exactly once in each of the 9
       3x3 sub-boxes of the grid.
    
    The '.' character indicates empty cells.

    The test cases all have a unique solution.
    '''
    def solveSudoku(self, board: List[List[str]]) -> None:
        # create initial board class
        b = Board(board)
        # stack for guesses
        s = deque()
        # keep going until solution is found
        while not b.solved():
            # if unable to fill take a guess
            if not b.fill():
                g = b.guesses()
                # make a new guess
                if g:
                    x, y, z, g = g
                    s.append((deepcopy(b), x, y, z, g[1:]))
                    b.place(x,y,z,g[0])
                # next guess
                else:
                    while s:
                        b, x, y, z, g = s.pop()
                        if g:
                            s.append((deepcopy(b), x, y, z, g[1:]))
                            b.place(x,y,z,g[0])
                            break
                    else:
                        # puzzle fails
                        break
        # update board so that it reflects solution
        for i in range(9):
            for j in range(9):
                board[i][j] = Board.values[b.b[i][j]] if b.b[i][j] in Board.values else '.'

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
        o = [["5","3","4","6","7","8","9","1","2"],
             ["6","7","2","1","9","5","3","4","8"],
             ["1","9","8","3","4","2","5","6","7"],
             ["8","5","9","7","6","1","4","2","3"],
             ["4","2","6","8","5","3","7","9","1"],
             ["7","1","3","9","2","4","8","5","6"],
             ["9","6","1","5","3","7","2","8","4"],
             ["2","8","7","4","1","9","6","3","5"],
             ["3","4","5","2","8","6","1","7","9"]]
        s.solveSudoku(i)
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = [[".","3",".",".","7",".",".",".","."],
             ["6",".",".","1",".","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".",".",".",".","7","9"]]
        o = [["5","3","4","6","7","8","9","1","2"],
             ["6","7","2","1","9","5","3","4","8"],
             ["1","9","8","3","4","2","5","6","7"],
             ["8","5","9","7","6","1","4","2","3"],
             ["4","2","6","8","5","3","7","9","1"],
             ["7","1","3","9","2","4","8","5","6"],
             ["9","6","1","5","3","7","2","8","4"],
             ["2","8","7","4","1","9","6","3","5"],
             ["3","4","5","2","8","6","1","7","9"]]
        s.solveSudoku(i)
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)