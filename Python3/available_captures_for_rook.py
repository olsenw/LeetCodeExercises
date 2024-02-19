# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number
    of white bishops 'B', black pawns 'p', and empty squares '.'.

    When the rook moves, it chooses one of four cardinal directions (north,
    east, south, or west), then moves in that direction until it chooses to
    stop, reaches the edge of the board, captures a black pawn, or is blocked by
    a white bishop. A rook is considered attacking a pawn if the rook can
    capture the pawn on the rook's turn. The number of available captures for
    the white rook is the number of pawns that the rook is attacking.

    Return the number of available captures for the white rook.
    '''
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = 8
        def rook():
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 'R':
                        return i,j
        answer = 0
        a,b = rook()
        # north
        for i in range(a - 1, -1, -1):
            if board[i][b] == 'p':
                answer += 1
                break
            elif board[i][b] == 'B':
                break
        # south
        for i in range(a + 1, n):
            if board[i][b] == 'p':
                answer += 1
                break
            elif board[i][b] == 'B':
                break
        # East
        for j in range(b - 1, -1, -1):
            if board[a][j] == 'p':
                answer += 1
                break
            elif board[a][j] == 'B':
                break
        # West
        for j in range(b + 1, n):
            if board[a][j] == 'p':
                answer += 1
                break
            elif board[a][j] == 'B':
                break
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
        o = 3
        self.assertEqual(s.numRookCaptures(i), o)

    def test_two(self):
        s = Solution()
        i = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
        o = 0
        self.assertEqual(s.numRookCaptures(i), o)

    def test_three(self):
        s = Solution()
        i = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
        o = 3
        self.assertEqual(s.numRookCaptures(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)