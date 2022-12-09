# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a signed 32-bit integer x, return x with its digits reversed. If
    reversing x causes the values to go outside the signed 32-bit integer range
    [-2^31, 2^31 - 1]. the return 0.

    Assume the environment does not allow 64-bit integers (signed or unsigned).
    '''
    def reverse_invalid(self, x: int) -> int:
        s = str(x)[::-1]
        if x < 0:
            s = s[:-1]
        n = int(s)
        if n < -2**31 or n > 2**31-1:
            return 0
        return n if x >= 0 else -n
    
    def reverse_brute(self, x: int) -> int:
        s = str(x)[::-1]
        if x < 0:
            s = s[:-1]
        if len(s) < 10:
            return -int(s) if x < 0 else int(s)
        elif len(s) == 10:
            c = "2147483648" if x < 0 else '2147483647'
            for i,j in zip(s,c):
                if i < j:
                    return -int(s) if x < 0 else int(s)
                elif i == j:
                    continue
                else:
                    return 0
            return 0
        else:
            return 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 123
        o = 321
        self.assertEqual(s.reverse(i), o)

    def test_two(self):
        s = Solution()
        i = -123
        o = -321
        self.assertEqual(s.reverse(i), o)

    def test_three(self):
        s = Solution()
        i = 2147483647
        o = 0
        self.assertEqual(s.reverse(i), o)

    def test_three(self):
        s = Solution()
        i = -2147483648
        o = 0
        self.assertEqual(s.reverse(i), o)

    def test_four(self):
        s = Solution()
        i = 120
        o = 21
        self.assertEqual(s.reverse(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)