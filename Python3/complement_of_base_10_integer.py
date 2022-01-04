# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    The complement of an integer is the integer you get when you flip
    all the 0's to 1's and all the 1's to 0's in its binary
    representation.

    Given an integer n, return its complement
    '''
    # done for differentness, perfer answer from 476 (look below)
    def bitwiseComplement(self, n: int) -> int:
        # using the string
        b = bin(n)[2:]
        c = 0
        d = 1
        for i in range(len(b)-1, -1, -1):
            if b[i] == '0':
                # add a bit at position i to c
                c += d
            d <<= 1
        return c

    # solution from problem 476 number complement
    def bitwiseComplement_476(self, n: int) -> int:
        mask = 1
        while mask < n:
            mask = (mask << 1) + 1
        return n ^ mask

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        o = 2
        self.assertEqual(s.bitwiseComplement(i), o)
        self.assertEqual(s.bitwiseComplement_476(i), o)

    def test_two(self):
        s = Solution()
        i = 7
        o = 0
        self.assertEqual(s.bitwiseComplement(i), o)
        self.assertEqual(s.bitwiseComplement_476(i), o)

    def test_three(self):
        s = Solution()
        i = 0
        o = 1
        self.assertEqual(s.bitwiseComplement(i), o)
        self.assertEqual(s.bitwiseComplement_476(i), o)

    def test_four(self):
        s = Solution()
        i = 10
        o = 5
        self.assertEqual(s.bitwiseComplement(i), o)
        self.assertEqual(s.bitwiseComplement_476(i), o)

    def test_five(self):
        s = Solution()
        i = 1
        o = 0
        self.assertEqual(s.bitwiseComplement(i), o)
        self.assertEqual(s.bitwiseComplement_476(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)