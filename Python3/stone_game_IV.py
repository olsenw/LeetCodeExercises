# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

# for sqrt
import math
class Solution:
    '''
    Alice and Bob take turns playing a game, with Alice playing first.

    Initially, there are n stones in a pile. On each player's turn, that
    player makes a move consisting of removing any non-zero square
    number of stones in the pile.
    
    Also, if a player cannot make a move, he/she loses the game.

    Given a positive inter n, return true if and only if Alice wins the
    game otherwise false, assuming both players play optimally.
    '''
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        for i in range(1,n+1):
            l = [not dp[i - j*j] for j in range(1, int(math.sqrt(i))+1) if j*j <= i]
            dp[i] = max(l)
        # print(n,dp[-1],dp)
        return dp[-1]

    def winnerSquareGame_2(self, n: int) -> bool:
        dp = [False] * (n+1)
        for i in range(1,n+1):
            for j in range(1, int(math.sqrt(i))+1):
                j *= j
                if j <= i and not dp[i-j]:
                    dp[i] = True
                    break
        return dp[-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = True
        self.assertEqual(s.winnerSquareGame(i), o)
        self.assertEqual(s.winnerSquareGame_2(i), o)

    def test_two(self):
        s = Solution()
        i = 2
        o = False
        self.assertEqual(s.winnerSquareGame(i), o)
        self.assertEqual(s.winnerSquareGame_2(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = True
        self.assertEqual(s.winnerSquareGame(i), o)
        self.assertEqual(s.winnerSquareGame_2(i), o)

    def test_four(self):
        s = Solution()
        i = 4
        o = True
        self.assertEqual(s.winnerSquareGame(i), o)
        self.assertEqual(s.winnerSquareGame_2(i), o)

    def test_five(self):
        s = Solution()
        i = 5
        o = False
        self.assertEqual(s.winnerSquareGame(i), o)
        self.assertEqual(s.winnerSquareGame_2(i), o)

    def test_six(self):
        s = Solution()
        i = 6
        o = True
        self.assertEqual(s.winnerSquareGame(i), o)
        self.assertEqual(s.winnerSquareGame_2(i), o)

    def test_seven(self):
        s = Solution()
        i = 7
        o = False
        self.assertEqual(s.winnerSquareGame(i), o)
        self.assertEqual(s.winnerSquareGame_2(i), o)

    def test_eight(self):
        s = Solution()
        i = 8
        o = True
        self.assertEqual(s.winnerSquareGame(i), o)
        self.assertEqual(s.winnerSquareGame_2(i), o)

    def test_nine(self):
        s = Solution()
        i = 9
        o = True
        self.assertEqual(s.winnerSquareGame(i), o)
        self.assertEqual(s.winnerSquareGame_2(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)