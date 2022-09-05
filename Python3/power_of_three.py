# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer n, return true if it is a power of three. Otherwise
    return false.

    An integer n is a power of three, if there exists an integer x such
    that n == 3^x.
    '''
    # the leetcode solution for this problem is very interesting
    # not a trivial problem
    def isPowerOfThree(self, n: int) -> bool:
        '''
        # brute force iteration
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
        '''
        # based on problem constraints (int max size)
        # 1162261467 is 3^19 largest power of 3 inside 2^31 range
        return n > 0 and 1162261467 % n == 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 27
        o = True
        self.assertEqual(s.isPowerOfThree(i), o)

    def test_two(self):
        s = Solution()
        i = 0
        o = False
        self.assertEqual(s.isPowerOfThree(i), o)

    def test_three(self):
        s = Solution()
        i = -1
        o = False
        self.assertEqual(s.isPowerOfThree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)