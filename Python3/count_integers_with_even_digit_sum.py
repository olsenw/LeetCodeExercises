# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer num, return the number of positive integers less
    than of equal to num whose digit sums are even.

    The digit sum of a positive integer is the sum of all its digits
    '''
    def countEven(self, num: int) -> int:
        return sum(sum(int(i) for i in str(x)) % 2 == 0 for x in range(1,num+1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        o = 2
        self.assertEqual(s.countEven(i), o)

    def test_two(self):
        s = Solution()
        i = 30
        o = 14
        self.assertEqual(s.countEven(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)