# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 0-indexed integer arrays player1 and player2, representing the
    number of pins that player 1 and player 2 hit in a bowling game,
    respectively.

    The bowling game consists of n turns, and the number of pins in each turn is
    exactly 10.

    Assume a player hits xi pins in the ith turn. the value of the ith turn for
    the player is:
    * 2xi if the player hits 10 pins in either (i-1)th or (i-2)th turn.
    * Otherwise, it is xi.

    The score of the player is the sum of the values of their n turns.

    Return
    * 1 if the score of player 1 is more than the score of player 2,
    * 2 if the score of player 2 is more than the score of player 1, and
    * 0 in case of a draw.
    '''
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        # def score(scorecard: List[int]) -> int:
        #     score = 0
        #     for i in range(len(scorecard)):
        #         m = 1 + (i > 1 and (scorecard[i-2] == 10 or scorecard[i-1] == 10))
        #         score += m * scorecard[i]
        #     return score
        def score(scorecard: List[int]) -> int:
            score = 0
            a,b = 0,0
            for i in range(len(scorecard)):
                m = 1 + (a == 10 or b == 10)
                score += m * scorecard[i]
                a = b
                b = scorecard[i]
            return score
        player1 = score(player1)
        player2 = score(player2)
        if player1 == player2:
            return 0
        elif player1 > player2:
            return 1
        else:
            return 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,10,3,2]
        j = [6,5,7,3]
        o = 1
        self.assertEqual(s.isWinner(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,5,7,6]
        j = [8,10,10,2]
        o = 2
        self.assertEqual(s.isWinner(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2,3]
        j = [4,1]
        o = 0
        self.assertEqual(s.isWinner(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,1,1,10,10,10,10]
        j = [10,10,10,10,1,1,1]
        o = 2
        self.assertEqual(s.isWinner(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)