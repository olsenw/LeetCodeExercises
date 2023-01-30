# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    The Tribonacci sequence Tn is defined as follows:

    T0 = 0, T1 = 1, T2 = 1 and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0

    Given n, return the value of Tn.
    '''
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        a,b,c = 0,1,1
        for _ in range(3, n+1):
            a,b,c = b,c,a+b+c
        return c

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 4
        o = 4
        self.assertEqual(s.tribonacci(i), o)

    def test_two(self):
        s = Solution()
        i = 25
        o = 1389537
        self.assertEqual(s.tribonacci(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)