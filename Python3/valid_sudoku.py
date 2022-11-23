# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
    validated according to the following rules:
    * Each row must contain the digits 1-9 without repetition.
    * Each column must contain the digits 1-9 without repetition.
    * Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
      without repetition.
    
    Note:
    * A Sudoku board (partially filled) could be valid but is not necessarily
      solvable.
    * Only the filled cells need to be validated according to the mentioned
      rules.
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        # validate rows
        for row in range(m):
            check = 0
            for col in range(n):
                if board[row][col] == '.':
                    continue
                num = 1 << (ord(board[row][col]) - ord('1'))
                if check & num:
                    return False
                check |= num
        # validate columns
        for col in range(n):
            check = 0
            for row in range(m):
                if board[row][col] == '.':
                    continue
                num = 1 << (ord(board[row][col]) - ord('1'))
                if check & num:
                    return False
                check |= num
        # validate squares
        for row in range(0, m, 3):
            for col in range(0, n, 3):
                check = 0
                for i in range(3):
                    for j in range(3):
                        if board[row + i][col + j] == '.':
                            continue
                        num = 1 << (ord(board[row + i][col + j]) - ord('1'))
                        if check & num:
                            return False
                        check |= num
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        o = True
        self.assertEqual(s.isValidSudoku(i), o)

    def test_two(self):
        s = Solution()
        i = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
        o = False
        self.assertEqual(s.isValidSudoku(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)