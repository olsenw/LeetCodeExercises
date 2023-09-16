# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The Hamming Distance between two integers is the number of positions at
    which the corresponding bits are different.

    Given two integers x and y, return teh Hamming distance between them.
    '''
    def hammingDistance(self, x: int, y: int) -> int:
        return sum((x >> i) & 1 != (y >> i) & 1 for i in range(32,-1,-1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        j = 4
        o = 2
        self.assertEqual(s.hammingDistance(i,j), o)

    def test_two(self):
        s = Solution()
        i = 3
        j = 1
        o = 1
        self.assertEqual(s.hammingDistance(i,j), o)

    def test_three(self):
        s = Solution()
        i = 12435
        j = 7654322
        o = 13
        self.assertEqual(s.hammingDistance(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)