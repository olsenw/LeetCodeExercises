# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Write a function that takes an unsigned integer and returns the
    number of '1' bits it has (also known as the Hamming weight).
    '''
    def hammingWeight(self, n: int) -> int:
        a = 0
        while n > 0:
            if n & 1:
                a += 1
            n >>= 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 0b00000000000000000000000000001011
        o = 3
        self.assertEqual(s.hammingWeight(i), o)

    def test_two(self):
        s = Solution()
        i = 0b00000000000000000000000010000000
        o = 1
        self.assertEqual(s.hammingWeight(i), o)

    def test_three(self):
        s = Solution()
        i = 0b11111111111111111111111111111101
        o = 31
        self.assertEqual(s.hammingWeight(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)