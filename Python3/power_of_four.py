# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer n, return true if it is a power of four. Otherwise,
    return false.

    An integer n is a power of four, if there exists an integer x such
    that n == 4^x.
    '''
    def isPowerOfFour(self, n: int) -> bool:
        '''
        return any(4**i==n for i in range(16))
        '''
        mask = 0b01010101010101010101010101010101
        # make sure positive
        # make sure it is possible power four (n & mask == n)
        # make sure it is power of two (n & (n-1) == 0)
        return n > 0 and n & mask == n and n & (n-1) == 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 16
        o = True
        self.assertEqual(s.isPowerOfFour(i), o)

    def test_two(self):
        s = Solution()
        i = 5
        o = False
        self.assertEqual(s.isPowerOfFour(i), o)

    def test_three(self):
        s = Solution()
        i = 1
        o = True
        self.assertEqual(s.isPowerOfFour(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)