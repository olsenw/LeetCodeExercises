# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from math import ceil
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There is a video game in which a city is being defended from a group of n
    monsters. Given a 0-indexed integer array dist of size n, where dist[i] is
    the initial distance in kilometers of the ith monster from the city.

    The monsters walk toward the city at a constant speed. The speed of each
    monster is given in an integer array speed of size n, where speed[i] is the
    speed of the ith monster in kilometers per minute.

    There is a weapon that, once fully charged, can eliminate a single monster.
    However, the weapon takes one minute to charge. The weapon is fully charged
    at the very start.

    The game is lost when any monster reaches the city. If a monster reaches the
    city at the exact moment the weapon is fully charged, it counts as a loss,
    and the game ends before the weapon can be used.

    Return the maximum number of monsters that can be eliminated before the game
    is lost, or n if all the monsters can be eliminated before reaching the
    city.
    '''
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = sorted(ceil(i / j) for i,j in zip(dist, speed))
        for i,j in enumerate(arrival):
            if i >= j:
                return i
        return len(dist)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,4]
        j = [1,1,1]
        o = 3
        self.assertEqual(s.eliminateMaximum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2,3]
        j = [1,1,1,1]
        o = 1
        self.assertEqual(s.eliminateMaximum(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3,2,4]
        j = [5,3,2]
        o = 1
        self.assertEqual(s.eliminateMaximum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)