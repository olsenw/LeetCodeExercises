# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Water n plants in a garden with a watering can. The plants are arranged in a
    row and are labeled from 0 to n - 1 from left to right where the ith plant
    is located at x = 1. There is a river at x = -1 that can be used to refill
    the watering can at.

    Each plant needs a specific amount of water. Each plant is watered in the
    following way:
    * Water the plants in order from left to right.
    * After watering the current plant, if there is not enough water to
      completely water the next plant, return to the river ro fully refill the
      watering can.
    * The watering can cannot be refilled early.

    Initially the watering is at the river (ie, x = -1). It takes one step to
    move one unit on the x-axis.

    Given a 0-indexed integer array plants of n integers, where plants[i] is the
    amount of water the ith plant needs, and an integer capacity representing
    the watering can capacity, return the number of steps needed to water all
    the plants.
    '''
    # counts steps wrong
    def wateringPlants_fails(self, plants: List[int], capacity: int) -> int:
        answer = 0
        current = capacity
        for i,j in enumerate(plants):
            answer += 1
            if current < j:
                answer += i + i + 1 + 1
                current = capacity
            current -= j
        return answer

    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        answer = 0
        current = capacity - plants[0]
        for i in range(len(plants)-1):
            answer += 1
            if current < plants[i+1]:
                answer += i + i + 2
                current = capacity
            current -= plants[i+1]
        return answer + 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,2,3,3]
        j = 5
        o = 14
        self.assertEqual(s.wateringPlants(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,4,2,3]
        j = 4
        o = 30
        self.assertEqual(s.wateringPlants(i,j), o)

    def test_three(self):
        s = Solution()
        i = [7,7,7,7,7,7,7]
        j = 8
        o = 49
        self.assertEqual(s.wateringPlants(i,j), o)

    def test_four(self):
        s = Solution()
        i = [7,7]
        j = 8
        o = 4
        self.assertEqual(s.wateringPlants(i,j), o)

    def test_five(self):
        s = Solution()
        i = [3,2,4,2,1]
        j = 6
        o = 17
        self.assertEqual(s.wateringPlants(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)