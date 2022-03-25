# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A company is planning to interview 2n people. Given the array costs
    where costs[i] = [aCosti, bCosti] is the cost of flying the ith
    person to city a and city b respectively.

    Return the minimum cost to fly every person to a city such that
    exactly n people arrive in each city.
    '''
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # send all 2n candidate to city a
        a = sum([a for a,b in costs])
        # calculate savings for flying candidates to b instead of a
        # sort by savings (negative is saving, positive is expense)
        # only need n of these candidates
        # sum the savings for flying to b instead of a
        b = sum(sorted([b-a for a,b in costs])[:len(costs)//2])
        # send 2n to a plus the savings send n to b
        return a + b

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[10,20],[30,200],[400,50],[30,20]]
        o = 110
        self.assertEqual(s.twoCitySchedCost(i), o)

    def test_two(self):
        s = Solution()
        i = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
        o = 1859
        self.assertEqual(s.twoCitySchedCost(i), o)

    def test_three(self):
        s = Solution()
        i = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
        o = 3086
        self.assertEqual(s.twoCitySchedCost(i), o)

    def test_four(self):
        s = Solution()
        i = [[70,311],[74,927],[732,711],[126,583],[857,118],[97,928],[975,843],[175,221],[284,929],[816,602],[689,863],[721,888]]
        o = 4723
        self.assertEqual(s.twoCitySchedCost(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)