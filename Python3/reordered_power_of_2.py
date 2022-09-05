# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter

class Solution:
    '''
    Given an integer n. Reorder the digits of n in any order (including
    the original order) such that the leading digit is not zero.

    Return true if and only if this can be done such that the resulting
    number is a power of two.
    '''
    def reorderedPowerOf2(self, n: int) -> bool:
        s = str(n)
        print(s, len(s))
        c = Counter(s)
        a = 0
        b = '1'
        while len(b) < len(s):
            print(b, len(b))
            a += 1
            b = str(2**a)
        while len(b) == len(s):
            print(b, len(b))
            if c == Counter(b):
                return True
            a += 1
            b = str(2**a)
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1
        o = True
        self.assertEqual(s.reorderedPowerOf2(i), o)

    def test_two(self):
        s = Solution()
        i = 10
        o = False
        self.assertEqual(s.reorderedPowerOf2(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)