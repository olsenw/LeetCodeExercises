# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given three integers x, y, and z, representing the positions of three people
    on a number line.
    * x is the position of Person 1.
    * y is the position of Person 2.
    * z is the position of Person 3, who does not move.

    Both Person 1 and Person 2 move toward Person 3 at the same speed.

    Determine which person reaches Person 3 first:
    * Return 1 if Person 1 arrives first.
    * Return 2 if Person 2 arrives first.
    * return 0 if both arrive at the same time.

    Return the result accordingly.
    '''
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = abs(x - z)
        b = abs(y - z)
        if a == b:
            return 0
        elif a < b:
            return 1
        else:
            return 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2,7,4
        o = 1
        self.assertEqual(s.findClosest(*i), o)

    def test_two(self):
        s = Solution()
        i = 2,5,6
        o = 2
        self.assertEqual(s.findClosest(*i), o)

    def test_three(self):
        s = Solution()
        i = 1,5,3
        o = 0
        self.assertEqual(s.findClosest(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)