# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer mass, which represents the original mass of a planet. Also
    given an integer array asteroids, where asteroids[i] is the mass of the ith
    asteroid.

    It is possible to arrange for the planet to collide with the asteroids in
    any arbitrary order. If the mass of the planet is greater than or equal to
    the mass of asteroid, the asteroid is destroyed and the planet gains the
    mass of the asteroid. Otherwise, the planet is destroyed.

    Return true if all asteroids can be destroyed. Otherwise return false.
    '''
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if mass < a:
                return False
            mass += a
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10
        j = [3,9,19,5,21]
        o = True
        self.assertEqual(s.asteroidsDestroyed(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = [4,9,23,4]
        o = False
        self.assertEqual(s.asteroidsDestroyed(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)