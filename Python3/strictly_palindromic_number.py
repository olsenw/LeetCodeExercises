# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An integer n is strictly palindromic if, for every base between 2 and n-2
    (inclusive), the string representation of the integer n in base b is
    palindromic.

    Given an integer n, return true if n is strictly palindromic and false
    otherwise.

    A string is palindromic if it reads the same forward and backward.
    '''
    def isStrictlyPalindromic_passes(self, n: int) -> bool:
        def toBase(n, b) -> List[int]:
            answer = []
            while n:
                answer.append(n % b)
                n //= b
            return answer[::-1]
        for b in range(2, n-1):
            a = toBase(n, b)
            if a != a[::-1]:
                return False
        return True

    # no way to ever be palindromic
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 8
        o = False
        self.assertEqual(s.isStrictlyPalindromic(i), o)

    def test_two(self):
        s = Solution()
        i = 4
        o = False
        self.assertEqual(s.isStrictlyPalindromic(i), o)

    def test_three(self):
        s = Solution()
        i = 10000
        o = False
        self.assertEqual(s.isStrictlyPalindromic(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)