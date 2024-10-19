# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two positive integers n and k, the binary string sn is formed as
    follows:
    * S1 = "0"
    * Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1

    Where + denotes the concatenation operation, reverse(x) returns the reversed
    string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1
    changes to 0).

    For example, the first four strings in the sequence are:
    * S1 = "0"
    * S2 = "011"
    * S3 = "0111001"
    * S4 = "011100110110001"

    Return the kth bit in the Sn. It is guaranteed that k is valid for the given
    n.
    '''
    def findKthBit(self, n: int, k: int) -> str:
        @cache
        def r(n):
            if n == 1:
                return "0"
            return f'{r(n-1)}1{"".join("1" if i == "0" else "0" for i in reversed(r(n-1)))}'
        return r(n)[k-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3, 1
        o = "0"
        self.assertEqual(s.findKthBit(*i), o)

    def test_two(self):
        s = Solution()
        i = 4, 11
        o = "1"
        self.assertEqual(s.findKthBit(*i), o)

    def test_three(self):
        s = Solution()
        i = 20, 48575
        o = "1"
        self.assertEqual(s.findKthBit(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)