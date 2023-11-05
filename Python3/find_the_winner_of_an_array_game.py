# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array arr of distinct integers and an integer k.

    A game will be played between the first two elements of the array (ie arr[0]
    and arr[1]). In each round of the game, we compare arr[0] with arr[1], the
    larger integer wins and remains at position 0, and the smaller integer moves
    to the end of the array. The game ends when an integer wins k consecutive
    rounds.

    Return the integer which will win the game.

    It is guaranteed that there will be a winner of the game.
    '''
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        queue = deque(arr[1:])
        wins = 0
        m = max(arr)
        while wins < k and winner != m:
            contestant = queue.popleft()
            if winner < contestant:
                queue.append(winner)
                winner = contestant
                wins = 1
            else:
                queue.append(contestant)
                wins += 1
        return winner

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,1,3,5,4,6,7]
        j = 2
        o = 5
        self.assertEqual(s.getWinner(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,2,1]
        j = 10
        o = 3
        self.assertEqual(s.getWinner(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,11,22,33,44,55,66,77,88,99]
        j = 1000000000
        o = 99
        self.assertEqual(s.getWinner(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)