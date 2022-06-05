# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    The n-queens puzzle is the problem of placing n queens on an n x n
    chessboard such that no two queens attack each other.

    Given an integer n, return the number of distinct solutions to the
    n-queens puzzle.
    '''
    # revised version of n_queens solution
    def totalNQueens_revised(self, n: int) -> int:
        a = 0
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
                a += 1
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

    # based on discussion post by constantine786
    # https://leetcode.com/problems/n-queens-ii/discuss/2111513/Python-Solution-with-Explanation
    # basically looking at this for how to index the diagonals instead
    # of having to keep the whole board for tracking
    # also neat way of returning answer through the call stack
    def totalNQueens(self, n: int) -> int:
        # visited columns
        c = set()
        # visited down right diagonals (row - col == diagonal)
        d = set()
        # visited down left diagonals (row + col == diagonal)
        a = set()
        def backtrack(placed):
            nonlocal c,d,a
            if placed == n:
                return 1
            r = 0
            for i in range(n):
                if not (i in c or (placed - i) in d or (placed + i) in a):
                    c.add(i)
                    d.add(placed - i)
                    a.add(placed + i)
                    r += backtrack(placed + 1)
                    c.remove(i)
                    d.remove(placed - i)
                    a.remove(placed + i)
            return r
        return backtrack(0)


class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = 1
        self.assertEqual(s.totalNQueens(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = 0
        self.assertEqual(s.totalNQueens(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = 0
        self.assertEqual(s.totalNQueens(i), o)

    def test_four(self):
        s = Solution()
        i = 4
        o = 2
        self.assertEqual(s.totalNQueens(i), o)

    def test_five(self):
        s = Solution()
        i = 5
        o = 10
        self.assertEqual(s.totalNQueens(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)