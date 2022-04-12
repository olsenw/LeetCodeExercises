# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    According to Wikipedia's article: "The Game of Life, also known
    simply as Life, is a cellular automation devised by the British
    mathematician John Horton Conway in 1970."

    The board is made up of an m x n grid of cells, where each cell has
    an initial state: live (represented by a 1) or dead (represented by
    a 0). Each cell interacts with its eight neighbors (horizontal,
    vertcal, diagonal) using the following four rules (taken from
    Wikipedia article):
    
    1) Any live cell with fewer than two live neighbors dies as if
       caused by under-population.
    2) Any live cell with two or three live neighbors lives on to the
       next generation.
    3) Any live cell with more than three live neighbors dies, as if by
       over-population.
    4) Any dead cell with exactly three live neighbors becomes a live
       cell as if by reproduction.

    The next state is created by applying the above rules simultaneously
    to every cell in the current state, where births and deaths occur
    simultaneously. Given the current state of the m x n grid board,
    return the next state.
    '''
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        update = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                g = board[i-1][j-1]
                update[i-1][j-1] += g
                update[i-1][j] += g
                update[i-1][j+1] += g

                update[i][j-1] += g
                update[i][j+1] += g

                update[i+1][j-1] += g
                update[i+1][j] += g
                update[i+1][j+1] += g
        # replace values on board
        for i in range(1,m+1):
            for j in range(1,n+1):
                # 1) under-population
                if update[i][j] < 2:
                    board[i-1][j-1] = 0
                # 2) lives on
                # 3) over-population
                elif update[i][j] > 3:
                    board[i-1][j-1] = 0
                # 4) reproduction
                elif update[i][j] == 3:
                    board[i-1][j-1] = 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        s.gameOfLife(i)
        o = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = [[1,1],[1,0]]
        s.gameOfLife(i)
        o = [[1,1],[1,1]]
        self.assertEqual(i, o)

    def test_three(self):
        s = Solution()
        i = [[1]]
        s.gameOfLife(i)
        o = [[0]]
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)