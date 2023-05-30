# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer num, return true if num is a perfect square or
    false otherwise.

    A perfect square is an integer that is the square of an integer. In other
    words, it is the product of some integer with itself.

    Do not use a built in function such as sqrt.
    '''
    def isPerfectSquare(self, num: int) -> bool:
        i,j = 1, num
        while i < j:
            k = (i + j) // 2
            if k * k < num:
                i = k + 1
            else:
                j = k
        return i * j == num

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 16
        o = True
        self.assertEqual(s.isPerfectSquare(i), o)

    def test_two(self):
        s = Solution()
        i = 14
        o = False
        self.assertEqual(s.isPerfectSquare(i), o)

    def test_three(self):
        s = Solution()
        i = 256
        o = True
        self.assertEqual(s.isPerfectSquare(i), o)

    def test_four(self):
        s = Solution()
        i = 1024
        o = True
        self.assertEqual(s.isPerfectSquare(i), o)

    def test_five(self):
        s = Solution()
        i = 1111111
        o = False
        self.assertEqual(s.isPerfectSquare(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)