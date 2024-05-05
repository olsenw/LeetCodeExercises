# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from math import sqrt
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a non-negative integer c, decide whether there're two integers a and b
    such that a^2 + b^2 = c
    '''
    def judgeSquareSum(self, c: int) -> bool:
        '''
        Could change from linear to log n by doing binary search
        lo = 0 hi = sqrt(c)
        '''
        for i in range(int(sqrt(c)+1)):
            j = int(sqrt(c - (i * i)))
            if i * i + j * j == c:
                return True
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        o = True
        self.assertEqual(s.judgeSquareSum(i), o)

    def test_two(self):
        s = Solution()
        i = 3
        o = False
        self.assertEqual(s.judgeSquareSum(i), o)

    def test_three(self):
        s = Solution()
        i = 1
        o = True
        self.assertEqual(s.judgeSquareSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)