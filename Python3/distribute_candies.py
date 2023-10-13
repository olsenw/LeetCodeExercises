# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Alice has n candies, where the ith candy is of type candyType[i]. Alice
    noticed that she started to gain weight, so she visited a doctor.

    The doctor advised Alice to only eat n / 2 of the candies she has (n is
    always even). Alice likes her candies very much, and she wants to eat the
    maximum number of different types of candies while still following the
    doctor's advice.

    Given the integer array candyType of length n, return the maximum number of
    different types of candies she can eat if she only eats n / 2 of them.
    '''
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,2,2,3,3]
        o = 3
        self.assertEqual(s.distributeCandies(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2,3]
        o = 2
        self.assertEqual(s.distributeCandies(i), o)

    def test_three(self):
        s = Solution()
        i = [6,6,6,6]
        o = 1
        self.assertEqual(s.distributeCandies(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)