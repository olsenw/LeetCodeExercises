# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a wooden plank of length n unit. Some ants are walking on the plank,
    each ant moves with a speed of 1 unit per second. Some of the ants move to
    the left, the others move to the right.

    When two ants moving in two different directions meet at some point, they
    change their directions and continue moving again. Assume changing
    directions does not take any additional time.

    When an ant reaches one end of the plank at a time t, it falls off of the
    plank immediately.

    Given an integer n and two integer arrays left and right, the positions of
    the ants moving to the left and the right, return the moment when the last
    ant(s) fall off of the plank.
    '''
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left, default=0),max((n - r for r in right), default=0))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        j = [4,3]
        k = [0,1]
        o = 4
        self.assertEqual(s.getLastMoment(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 7
        j = []
        k = [0,1,2,3,4,5,6,7]
        o = 7
        self.assertEqual(s.getLastMoment(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 7
        j = [0,1,2,3,4,5,6,7]
        k = []
        o = 7
        self.assertEqual(s.getLastMoment(i,j,k), o)

    def test_four(self):
        s = Solution()
        i = 7
        j = [1,3,5,7]
        k = [0,2,4,6]
        o = 7
        self.assertEqual(s.getLastMoment(i,j,k), o)

    def test_five(self):
        s = Solution()
        i = 20
        j = [4,7,15]
        k = [9,3,13,10]
        o = 17
        self.assertEqual(s.getLastMoment(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)