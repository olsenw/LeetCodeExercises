# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import math
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array deck where deck[i] represents the number written on
    the ith card.

    Partition the cards into one or more groups such that:
    * Each group has exactly x cards where x > 1 and
    * All the cards in one group have the same integer written on them.

    Return True if such partition is possible, or false otherwise.
    '''
    def hasGroupsSizeX_fails(self, deck: List[int]) -> bool:
        c = Counter(deck)
        m = min(c[i] for i in c)
        if m == 1:
            return False
        for i in c:
            if c[i] % m > 0:
                return False
        return True

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return math.gcd(*Counter(deck).values()) > 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,4,3,2,1]
        o = True
        self.assertEqual(s.hasGroupsSizeX(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,2,2,2,3,3]
        o = False
        self.assertEqual(s.hasGroupsSizeX(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = False
        self.assertEqual(s.hasGroupsSizeX(i), o)

    def test_four(self):
        s = Solution()
        i = [1,1,2,2,2,2]
        o = True
        self.assertEqual(s.hasGroupsSizeX(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)