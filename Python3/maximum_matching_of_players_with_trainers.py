# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array players, where players[i] represents the
    ability of the ith player. Also is a 0-indexed integer array trainers where
    trainers[i] represents the training capacity of the jth trainer.

    The ith player can match with the jth trainer if the player's ability is
    less than or equal to the trainer's training capacity. Additionally, the ith
    player can be matched at most with one trainer, and the jth trainer can be
    matched with at most one player.

    Return the maximum number of number of matching between players and trainers
    that satisfy these conditions.
    '''
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        answer = 0
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        j = 0
        for i in range(len(trainers)):
            while j < len(players) and trainers[i] < players[j]:
                j += 1
            if j == len(players):
                break
            answer += 1
            j += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,7,9]
        j = [8,2,5,8]
        o = 2
        self.assertEqual(s.matchPlayersAndTrainers(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1]
        j = [10]
        o = 1
        self.assertEqual(s.matchPlayersAndTrainers(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)