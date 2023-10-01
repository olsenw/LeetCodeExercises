# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    There are n rings and each ring is either red, green, or blue. The rings are
    distributed across ten rods labeled from 0 to 9.

    Given a string rings of length 2n that describes the n rings that are placed
    onto the rods. Every two characters in rings forms a color position pair
    that is used to describe each ring where:
    * The first character of the ith pair denotes the ith ring's color
      ('R','G','B').
    * The second character of the ith pair denotes the rod that the ith ring is
      placed on ('0' to '9').
    
    Return the number of rods that have all three colors of rings on them.
    '''
    def countPoints(self, rings: str) -> int:
        rods = {i:set() for i in "0123456789"}
        for i in range(0, len(rings), 2):
            rods[rings[i+1]].add(rings[i])
        return sum(len(rods[i]) == 3 for i in rods)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "B0B6G0R6R0R6G9"
        o = 1
        self.assertEqual(s.countPoints(i), o)

    def test_two(self):
        s = Solution()
        i = "B0R0G0R9R0B0G0"
        o = 1
        self.assertEqual(s.countPoints(i), o)

    def test_three(self):
        s = Solution()
        i = "G4"
        o = 0
        self.assertEqual(s.countPoints(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)