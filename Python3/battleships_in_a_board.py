# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an m x n matrix board where each cell is a battleship 'X' or empty
    '.', return the number of battleships on board.

    Battleships can only be placed horizontally or vertically on board. In other
    words, they can only be made of the shape 1 x k (1 row, k columns) or (k
    rows, 1 column), where k can be of any size. At least one horizontal or
    vertical cell separates between two battleships (ie, there are no adjacent
    battleships).
    '''
    def countBattleships(self, board: List[List[str]]) -> int:
        m,n = len(board), len(board[0])
        answer = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    answer += 1
                    for a in range(i,m):
                        if board[a][j] == '.':
                            break
                        board[a][j] = '.'
                    for b in range(j + 1, n):
                        if board[i][b] == '.':
                            break
                        board[i][b] = '.'
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
        o = 2
        self.assertEqual(s.countBattleships(i), o)

    def test_two(self):
        s = Solution()
        i = [["."]]
        o = 0
        self.assertEqual(s.countBattleships(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)