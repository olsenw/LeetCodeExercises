# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    An ugly number is a positive whose prime factors are limited to 2,3, and 5.
    
    Given an integer n, return true if n is an ugly number.
    '''
    def isUgly_passes(self, n: int) -> bool:
        # catch negative numbers and special case 1
        if n < 1:
            return False
        while not (n % 2 and n % 3 and n % 5):
            if not n % 2:
                n //= 2
            elif not n % 3:
                n //= 3
            else:
                n //= 5
        return n == 1

    def isUgly(self, n: int) -> bool:
        while n > 1:
            if n % 2 == 0:
                n //= 2
                continue
            if n % 3 == 0:
                n //= 3
                continue
            if n % 5 == 0:
                n //= 5
                continue
            break
        return n == 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 6
        o = True
        self.assertEqual(s.isUgly(i), o)

    def test_two(self):
        s = Solution()
        i = 1
        o = True
        self.assertEqual(s.isUgly(i), o)

    def test_three(self):
        s = Solution()
        i = 14
        o = False
        self.assertEqual(s.isUgly(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)