# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import singledispatchmethod
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Optional, Set, Tuple

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
    def solveSudoku_fails(self, board: List[List[str]]) -> None:
        n = 9
        s = math.isqrt(n)
        def options(i:int,j:int) -> Set[int]:
            answer = set("123456789")
            for k in range(n):
                # column
                answer.discard(board[k][j])
                # row
                answer.discard(board[i][k])
            # square
            a = s * (i // s)
            b = s * (j // s)
            for x in range(s):
                for y in range(s):
                    answer.discard(board[a + x][b+x])
            return list(answer)
        moves = []
        def fill() -> Tuple[int,int,List[int]]:
            a,b,guess = 0,0,list("123456789")
            for i in range(n):
                for j in range(n):
                    if board[i][j] != ".":
                        continue
                    g = options(i,j)
                    if len(g) == 1:
                        moves.append((False,i,j))
                        board[i][j] = g[0]
                    elif len(g) == 0:
                        raise ValueError("Invalid Board State")
                    elif len(g) < len(guess):
                        a,b,guess = i,j,g
            return a,b,guess
        missing = sum(board[i][j] == '.' for i in range(n) for j in range(n))
        def guess():
            if missing == len(moves):
                return
            m = len(moves)
            i,j,g = fill()
            while m < len(moves):
                m = len(moves)
                i,j,g = fill()
            for k in g:
                try:
                    board[i][j] = k
                    moves.append((True,i,j))
                    guess()
                except ValueError as e:
                    if str(e) != "Invalid Board State":
                        raise e
                    while moves[-1][0] == False:
                        _,a,b = moves.pop()
                        board[a][b] = "."
                    _,a,b = moves.pop()
                    board[a][b] = "."
            if missing != len(moves):
                raise ValueError("Invalid Board State")
            pass
        guess()
        return
    
    # brute force TLE
    def solveSudoku_tle(self, board: List[List[str]]) -> None:
        n = 9
        s = math.isqrt(n)
        def options(i:int,j:int) -> Set[int]:
            answer = set("123456789")
            for k in range(n):
                # column
                answer.discard(board[k][j])
                # row
                answer.discard(board[i][k])
            # square
            a = s * (i // s)
            b = s * (j // s)
            for x in range(s):
                for y in range(s):
                    answer.discard(board[a + x][b+x])
            if len(answer) == 0:
                raise ValueError("Invalid Board State")
            return list(answer)
        def fill(missing:int):
            if missing == 0:
                raise ValueError("Done")
            for i in range(n):
                for j in range(n):
                    if board[i][j] != ".":
                        continue
                    for k in options(i,j):
                        try:
                            board[i][j] = k
                            fill(missing - 1)
                        except ValueError as e:
                            if str(e) != "Invalid Board State":
                                raise e
                            board[i][j] = "."
        try:
            fill(sum(board[i][j] == "." for i in range(n) for j in range(n)))
        except ValueError as e:
            if str(e) != "Done":
                raise e
        return
        
    '''
    Based on 21ms code answer (which is really ~1200ms answer)
    [The answer is cheating by modifying the reported output at exit]

    Makes use of backtracking and reduced choices

    Base case is arriving at the bottom right corner and finding an answer.

    This is a working version of what I tried doing above
    '''
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        avai_col = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
        avai_row = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
        avai_subsquare = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    avai_row[i].remove(val)
                    avai_col[j].remove(val)
                    avai_subsquare[(int(i/3)*3) + int(j/3)].remove(val)

        def backtrack(i, j, board):
            if board[i][j] != '.':
                if i == 8 and j == 8:
                    return True
                elif  j < 8:
                    return backtrack(i, j + 1, board)
                elif i < 8 and j == 8:
                    return backtrack(i + 1, 0, board)
            
            avai_set = avai_row[i] & avai_col[j] & avai_subsquare[(i//3)*3 + j//3]
            for v in avai_set:
                board[i][j] = str(v)

                avai_row[i].remove(v)
                avai_col[j].remove(v)
                avai_subsquare[(int(i/3)*3) + int(j/3)].remove(v)

                if (i == 8 and j == 8) or (j < 8 and backtrack(i, j + 1, board)) or (i < 8 and j == 8 and backtrack(i + 1, 0, board)):
                    return True

                board[i][j] = '.'
                avai_row[i].add(v)
                avai_col[j].add(v)
                avai_subsquare[(int(i/3)*3) + int(j/3)].add(v)

        backtrack(0, 0, board)

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

    # def test_two(self):
    #     s = Solution()
    #     i = [[".","3",".",".","7",".",".",".","."],
    #          ["6",".",".","1",".","5",".",".","."],
    #          [".","9","8",".",".",".",".","6","."],
    #          ["8",".",".",".","6",".",".",".","3"],
    #          ["4",".",".","8",".","3",".",".","1"],
    #          ["7",".",".",".","2",".",".",".","6"],
    #          [".","6",".",".",".",".","2","8","."],
    #          [".",".",".","4","1","9",".",".","5"],
    #          [".",".",".",".",".",".",".","7","9"]]
    #     o = [["5","3","4","6","7","8","9","1","2"],
    #          ["6","7","2","1","9","5","3","4","8"],
    #          ["1","9","8","3","4","2","5","6","7"],
    #          ["8","5","9","7","6","1","4","2","3"],
    #          ["4","2","6","8","5","3","7","9","1"],
    #          ["7","1","3","9","2","4","8","5","6"],
    #          ["9","6","1","5","3","7","2","8","4"],
    #          ["2","8","7","4","1","9","6","3","5"],
    #          ["3","4","5","2","8","6","1","7","9"]]
    #     s.solveSudoku(i)
    #     self.assertEqual(i, o)

    # def test_three(self):
    #     s = Solution()
    #     i = [[".",".","4","6","7","8","9","1","2"],
    #          [".",".","2","1","9","5","3","4","8"],
    #          ["1","9","8","3","4","2","5","6","7"],
    #          ["8","5","9","7","6","1","4","2","3"],
    #          ["4","2","6","8","5","3","7","9","1"],
    #          ["7","1","3","9","2","4","8","5","6"],
    #          ["9","6","1","5","3","7","2","8","4"],
    #          ["2","8","7","4","1","9","6","3","5"],
    #          ["3","4","5","2","8","6","1","7","9"]]
    #     o = [["5","3","4","6","7","8","9","1","2"],
    #          ["6","7","2","1","9","5","3","4","8"],
    #          ["1","9","8","3","4","2","5","6","7"],
    #          ["8","5","9","7","6","1","4","2","3"],
    #          ["4","2","6","8","5","3","7","9","1"],
    #          ["7","1","3","9","2","4","8","5","6"],
    #          ["9","6","1","5","3","7","2","8","4"],
    #          ["2","8","7","4","1","9","6","3","5"],
    #          ["3","4","5","2","8","6","1","7","9"]]
    #     s.solveSudoku(i)
    #     self.assertEqual(i, o)

    # def test_four(self):
    #     s = Solution()
    #     i = [[".",".",".",".",".",".",".",".","."],
    #          [".","9",".",".","1",".",".","3","."],
    #          [".",".","6",".","2",".","7",".","."],
    #          [".",".",".","3",".","4",".",".","."],
    #          ["2","1",".",".",".",".",".","9","8"],
    #          [".",".",".",".",".",".",".",".","."],
    #          [".",".","2","5",".","6","4",".","."],
    #          [".","8",".",".",".",".",".","1","."],
    #          [".",".",".",".",".",".",".",".","."]]
    #     o = [["7","2","1","8","5","3","9","4","6"],
    #          ["4","9","5","6","1","7","8","3","2"],
    #          ["8","3","6","4","2","9","7","5","1"],
    #          ["9","6","7","3","8","4","1","2","5"],
    #          ["2","1","4","7","6","5","3","9","8"],
    #          ["3","5","8","2","9","1","6","7","4"],
    #          ["1","7","2","5","3","6","4","8","9"],
    #          ["6","8","3","9","4","2","5","1","7"],
    #          ["5","4","9","1","7","8","2","6","3"]]
        s.solveSudoku(i)
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)