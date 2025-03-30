# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two arrays of integers, fruits and baskets, each of length n, where
    fruits[i] represents the quantity of the ith type of fruit, and baskets[j]
    represents the capacity of the jth basket.

    From left to right, place the fruits according to these rules:
    * Each fruit type must be placed in the leftmost available basket with a
      capacity greater than or equal to the quantity of that fruit type.
    * Each basket can hold only one type of fruit.
    * If a fruit type cannot be placed in any basket, it remains unplaced.

    Return the number of fruit types that remain unplaced after all possible
    allocations are made.
    '''
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        answer = len(fruits)
        for f in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= f:
                    answer -= 1
                    baskets[i] *= -1
                    break
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [4,2,5]
        j = [3,5,4]
        o = 1
        self.assertEqual(s.numOfUnplacedFruits(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,6,1]
        j = [6,4,7]
        o = 0
        self.assertEqual(s.numOfUnplacedFruits(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)