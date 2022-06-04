# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    The n queens puzzle is the problem of placing n queens on an n x n
    chessboard such that no two queens attack each other.

    Given an integer n, return all distinct solutions to the n-queens
    puzzle. The answer may be returned in any order.

    Each solution contains a distinct board configuration of the
    n-queens' placement, where 'Q' and '.' both indicate a queen and an
    empty space, respectively.
    '''
    def solveNQueens_works(self, n: int) -> List[List[str]]:
        a = []
        def backtrack(board, x, y, remain):
            nonlocal a
            # mark threatened squares
            for i in range(n):
                board[x][i] = 1
                board[i][y] = 1
            for i,j in zip(range(x + 1, n), range(y + 1, n)):
                board[i][j] = 1
            for i,j in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
                board[i][j] = 1
            for i,j in zip(range(x + 1, n), range(y - 1, -1, -1)):
                board[i][j] = 1
            for i,j in zip(range(x - 1, -1, -1), range(y + 1, n)):
                board[i][j] = 1
            # mark (x,y) as being a Queen
            board[x][y] = 2
            # add solution to list of solutions
            if not remain:
                sol = []
                for b in board:
                    s = ""
                    for c in b:
                        s += 'Q' if c == 2 else '.'
                    sol.append(s)
                a.append(sol)
            # backtrack on possible locations
            for i in range(y + 1, n):
                if board[x][i] == 0:
                    backtrack([b[:] for b in board], x, i, remain - 1)
            for i in range(x + 1, n):
                for j in range(n):
                    if board[i][j] == 0:
                        backtrack([b[:] for b in board], i, j, remain - 1)
        # is there a possible solution where row one does not have queen?
        for i in range(n):
            for j in range(n):
                backtrack([[0] * n for _ in range(n)], i, j, n-1)
        return a

    def solveNQueens(self, n: int) -> List[List[str]]:
        a = []
        def backtrack(board, x, y, remain):
            nonlocal a
            # mark threatened squares
            for i in range(n):
                board[i][y] = 1
            for i,j in zip(range(x + 1, n), range(y + 1, n)):
                board[i][j] = 1
            for i,j in zip(range(x + 1, n), range(y - 1, -1, -1)):
                board[i][j] = 1
            # mark (x,y) as being a Queen
            board[x][y] = 2
            # add solution to list of solutions
            if not remain:
                sol = []
                for b in board:
                    s = ""
                    for c in b:
                        s += 'Q' if c == 2 else '.'
                    sol.append(s)
                a.append(sol)
            # backtrack on possible locations
            x += 1
            if x == n:
                return
            for i in range(n):
                if board[x][i] == 0:
                    backtrack([b[:] for b in board], x, i, remain - 1)
        for i in range(n):
            backtrack([[0] * n for _ in range(n)], 0, i, n-1)
        return a

class UnitTesting(unittest.TestCase):
    def t(self, i, o):
        s = Solution()
        # a = s.solveNQueens_works(i)
        a = s.solveNQueens(i)
        self.assertEqual(len(a), len(o))
        for e in o:
            self.assertEqual(e in a, True)

    def test_one(self):
        i = 1
        o = [["Q"]]
        self.t(i,o)

    def test_two(self):
        s = Solution()
        i = 2
        o = []
        self.t(i,o)

    def test_three(self):
        s = Solution()
        i = 3
        o = []
        self.t(i,o)

    def test_four(self):
        s = Solution()
        i = 4
        o = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        self.t(i,o)

    def test_five(self):
        s = Solution()
        i = 5
        o = [['Q....', '..Q..', '....Q', '.Q...', '...Q.'],
             ['Q....', '...Q.', '.Q...', '....Q', '..Q..'],
             ['.Q...', '...Q.', 'Q....', '..Q..', '....Q'],
             ['.Q...', '....Q', '..Q..', 'Q....', '...Q.'],
             ['..Q..', 'Q....', '...Q.', '.Q...', '....Q'],
             ['..Q..', '....Q', '.Q...', '...Q.', 'Q....'],
             ['...Q.', 'Q....', '..Q..', '....Q', '.Q...'],
             ['...Q.', '.Q...', '....Q', '..Q..', 'Q....'],
             ['....Q', '.Q...', '...Q.', 'Q....', '..Q..'],
             ['....Q', '..Q..', 'Q....', '...Q.', '.Q...']]
        self.t(i,o)


if __name__ == '__main__':
    unittest.main(verbosity=2)