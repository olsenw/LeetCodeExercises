# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer n, return the smallest positive integer that is a
    multiple of both 2 and n.
    '''
    def smallestEvenMultiple(self, n: int) -> int:
        return 2 * n if n % 2 else n

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        o = 10
        self.assertEqual(s.smallestEvenMultiple(i), o)

    def test_two(self):
        s = Solution()
        i = 6
        o = 6
        self.assertEqual(s.smallestEvenMultiple(i), o)

    def test_three(self):
        s = Solution()
        i = 8
        o = 8
        self.assertEqual(s.smallestEvenMultiple(i), o)

    def test_four(self):
        s = Solution()
        i = 88
        o = 88
        self.assertEqual(s.smallestEvenMultiple(i), o)

    def test_five(self):
        s = Solution()
        i = 111
        o = 222
        self.assertEqual(s.smallestEvenMultiple(i), o)

    def test_six(self):
        s = Solution()
        i = 112
        o = 112
        self.assertEqual(s.smallestEvenMultiple(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)