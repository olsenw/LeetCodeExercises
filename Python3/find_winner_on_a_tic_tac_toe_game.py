# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of 
    Tic-tac-toe are:
    * Players take turns placing characters into empty squares ' '.
    * The first player A always places 'X' characters, while the second player 
      player B always places 'O' characters.
    * 'X' and 'O' characters are always placed into empty squares, never on
      filled ones.
    * The game ends when there are three of the same (non-empty) character
      filling any row, column, or diagonal.
    * The game also ends if all squares are non-empty.
    * No more moves can be played if the game is over.

    Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that
    the ith move will be played on grid[rowi][coli], return the winner of the
    game if it exists (A or B). In case the games ends in a draw return "Draw".
    If there are still movements to play return "Pending".

    Assume that moves is valid (ie it follows the rules of Tic-Tac-Toe), the
    grid is initially empty and A will play first.
    '''
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[' '] * 3 for _ in range(3)]
        def win(turn:str) -> bool:
            for i in range(3):
                if all(grid[i][j] == turn for j in range(3)):
                    return True
                if all(grid[j][i] == turn for j in range(3)):
                    return True
            if all(grid[i][i] == turn for i in range(3)):
                return True
            if all(grid[2-i][i] == turn for i in range(3)):
                return True
            return False
        turn = 'A'
        for i,j in moves:
            grid[i][j] = turn
            if win(turn):
                return turn
            if turn == 'A':
                turn = 'B'
            else:
                turn = 'A'
        return "Draw" if len(moves) == 9 else "Pending"

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,0],[2,0],[1,1],[2,1],[2,2]]
        o = "A"
        self.assertEqual(s.tictactoe(i), o)

    def test_two(self):
        s = Solution()
        i = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
        o = "B"
        self.assertEqual(s.tictactoe(i), o)

    def test_three(self):
        s = Solution()
        i = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
        o = "Draw"
        self.assertEqual(s.tictactoe(i), o)

    def test_four(self):
        s = Solution()
        i = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2]]
        o = "Pending"
        self.assertEqual(s.tictactoe(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)