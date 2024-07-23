# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer, check whether it has alternating bits: namely, if
    two adjacent bits will always have different values.
    '''
    def hasAlternatingBits(self, n: int) -> bool:
        i = n & 1
        while n:
            n >>= 1
            if n & 1 == i:
                return False
            i = n & 1
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        o = True
        self.assertEqual(s.hasAlternatingBits(i), o)

    def test_two(self):
        s = Solution()
        i = 7
        o = False
        self.assertEqual(s.hasAlternatingBits(i), o)

    def test_three(self):
        s = Solution()
        i = 11
        o = False
        self.assertEqual(s.hasAlternatingBits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)