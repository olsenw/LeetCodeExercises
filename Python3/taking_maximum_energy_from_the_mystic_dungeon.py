# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    In a mystic dungeon, n magicians are standing in a line. Each magician has
    an attribute that grants energy. Some magicians can grant negative energy,
    which means taking energy.

    There is a curse that after absorbing energy from magician i, there is a
    jump to magician (i + k). This process will be repeated until reaching
    magician (i + k) does not exist.

    In other words, choose a starting magician then teleport with k jumps until
    reaching the end of the magicians' sequence, absorbing all the energy during
    the journey.

    Given an array energy and an integer k. Return the maximum possible energy
    that can be gained.

    Note when being teleported the energy must be absorbed, whether it is
    negative or positive energy.
    '''
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(len(energy) - 1, k - 1, -1):
            energy[i-k] += energy[i]
        return max(energy)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,2,-10,-5,1]
        j = 3
        o = 3
        self.assertEqual(s.maximumEnergy(i,j), o)

    def test_two(self):
        s = Solution()
        i = [-2,-3,-1]
        j = 2
        o = -1
        self.assertEqual(s.maximumEnergy(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)