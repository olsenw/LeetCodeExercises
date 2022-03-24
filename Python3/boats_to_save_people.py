# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array people where people[i] is the weight of the ith
    person and an infinite number of boats where each boat can carry
    a maximum weight of limit. Each boat carries at most two people at
    the same time, provided the sum of the weight of those people is at
    most limit.

    Return the minimum number of boats to carry every given person.
    '''
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people = sorted(people, reverse=True)
        i = 0
        j = len(people) - 1
        # fat people first (ie those who hit the limit by themselves)
        while i < len(people) and people[i] >= limit:
            i += 1
            boats += 1
        # try putting two people on boats
        while i < len(people) and i < j:
            if people[i] + people[j] <= limit:
                j -= 1
            boats += 1
            i += 1
        return boats + (i == j)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2]
        j = 3
        o = 1
        self.assertEqual(s.numRescueBoats(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,2,2,1]
        j = 3
        o = 3
        self.assertEqual(s.numRescueBoats(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3,5,3,4]
        j = 5
        o = 4
        self.assertEqual(s.numRescueBoats(i,j), o)

    def test_four(self):
        s = Solution()
        i = [6,6,5,1,5]
        j = 6
        o = 4
        self.assertEqual(s.numRescueBoats(i,j), o)

    def test_four(self):
        s = Solution()
        i = [1,1,1,1,1]
        j = 2
        o = 3
        self.assertEqual(s.numRescueBoats(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)