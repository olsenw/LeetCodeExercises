# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given positive integers n and m.

    Define two integers as follows:
    * num1: The sum of all integers in the range [1,n] (both inclusive) that are
      not divisible by m.
    * num2: The sum of all integers in the range [1,n] (both inclusive) that are
      divisible by m.
    
    Return the integer num1 - num2.
    '''
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(i for i in range(1,n+1) if i % m != 0) - sum(i for i in range(1,n+1) if i % m == 0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10
        j = 3
        o = 19
        self.assertEqual(s.differenceOfSums(i,j), o)

    def test_two(self):
        s = Solution()
        i = 5
        j = 6
        o = 15
        self.assertEqual(s.differenceOfSums(i,j), o)

    def test_tthree(self):
        s = Solution()
        i = 5
        j = 1
        o = -15
        self.assertEqual(s.differenceOfSums(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)