# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    There is a game which consists of multiple characters, where each
    has two main properties; attack and defense. Given a 2D integer
    array properties where properties[i] = [attack_i, defense_i]
    represents the properties of the ith character in the game.

    A character is said to be weak if any other character has both
    attack and defense levels strictly greater than this character's
    attack and defense levels. More formally, a character i is said to
    be weak if there exists another character j where 
    attack_j > attack_i and defense_j > defense_i.

    Return the number of weak characters.
    '''
    def numberOfWeakCharacters_fails(self, properties: List[List[int]]) -> int:
        weak = 0
        properties.sort()
        # change to this to fix
        # properties.sort(key=lambda x: (x[0], -x[1]))
        monotonic = []
        for a,d in properties:
            while monotonic and monotonic[-1] < d:
                weak += 1
                monotonic.pop()
            monotonic.append(d)
        return weak

    # based off of discussion post by hong_xhao
    # https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/2551639/Python-5-Lines-Use-a-Stack
    # slightly different sort than my failing attempt
    # pushed on stack in order of largest to smallest defense for attack
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        mono = []
        properties.sort(key=lambda x: (x[0], -x[1]))
        for a,d in properties:
            while mono and d > mono[-1]:
                mono.pop()
            mono.append(d)
        return len(properties) - len(mono)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[5,5],[6,3],[3,6]]
        o = 0
        self.assertEqual(s.numberOfWeakCharacters(i), o)

    def test_two(self):
        s = Solution()
        i = [[2,2],[3,3]]
        o = 1
        self.assertEqual(s.numberOfWeakCharacters(i), o)

    def test_three(self):
        s = Solution()
        i = [[1,5],[10,4],[4,3]]
        o = 1
        self.assertEqual(s.numberOfWeakCharacters(i), o)

    def test_four(self):
        s = Solution()
        i = [[1,1],[2,1],[2,2],[1,2]]
        o = 1
        self.assertEqual(s.numberOfWeakCharacters(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)