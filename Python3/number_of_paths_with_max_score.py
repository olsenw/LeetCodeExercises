# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a square board of characters. It is possible to move on the board
    starting at the bottom right square marked with the character 'S'.

    The goal is to reach the top left square marked with the character 'E'. The
    rest of the squares are labeled either with a numeric character 1,2,...,9 or
    with an obstacle 'X'. In one move it is possible to go up, left or up-left
    (diagonally) only if there is no obstacle there.

    Return a list of two integers: the first integer is the maximum sum of
    numeric characters that can be collected, and the second is the number of
    such paths that can be taken to reach the maximum sum (modulo 10^9 + 7).

    In case there is no path, return [0,0]
    '''
    # based on hints
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        board = [[(int(board[i][j]) if board[i][j].isdigit() else (-1 if board[i][j] == 'X' else 0)) for j in range(n)] for i in range(n)]
        maximumSum = [[-1] * n for _ in range(n)]
        maximumSum[0][0] = 0
        for j in range(1,n):
            if board[0][j] == -1 or maximumSum[0][j-1] == -1:
                maximumSum[0][j] = -1
            else:
                maximumSum[0][j] = board[0][j] + maximumSum[0][j-1]
        for i in range(1,n):
            for j in range(n):
                if board[i][j] == -1:
                    maximumSum[i][j] = -1
                    continue
                if j == 0:
                    if maximumSum[i-1][j] == -1:
                        maximumSum[i][j] = -1
                    else:
                        maximumSum[i][j] = board[i][j] + maximumSum[i-1][j]
                    continue
                v = max(maximumSum[i][j-1], maximumSum[i-1][j-1], maximumSum[i-1][j])
                if v == -1:
                    maximumSum[i][j] = -1
                else:
                    maximumSum[i][j] = board[i][j] + v
        m = 10**9 + 7
        numberPaths = [[0 for j in range(n)] for i in range(n)]
        numberPaths[0][0] = 1
        for j in range(1,n):
            numberPaths[0][j] = numberPaths[0][j-1] if board[0][j] > -1 else 0
        for i in range(1,n):
            for j in range(n):
                if board[i][j] == -1:
                    continue
                if j == 0:
                    numberPaths[i][j] = numberPaths[i-1][j] if board[i][j] > -1 else 0
                    continue
                t = maximumSum[i][j] - board[i][j]
                if maximumSum[i][j-1] == t:
                    numberPaths[i][j] = (numberPaths[i][j] + numberPaths[i][j-1]) % m
                if maximumSum[i-1][j-1] == t:
                    numberPaths[i][j] = (numberPaths[i][j] + numberPaths[i-1][j-1]) % m
                if maximumSum[i-1][j] == t:
                    numberPaths[i][j] = (numberPaths[i][j] + numberPaths[i-1][j]) % m
        return [max(maximumSum[n-1][n-1],0), numberPaths[n-1][n-1]]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["E23","2X2","12S"]
        o = [7,1]
        self.assertEqual(s.pathsWithMaxScore(i), o)

    def test_two(self):
        s = Solution()
        i = ["E12","1X1","21S"]
        o = [4,2]
        self.assertEqual(s.pathsWithMaxScore(i), o)

    def test_three(self):
        s = Solution()
        i = ["E11","XXX","11S"]
        o = [0,0]
        self.assertEqual(s.pathsWithMaxScore(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)