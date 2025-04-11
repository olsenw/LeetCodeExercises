# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two positive integers low and high.

    An integer x consisting of 2 * n digits is symmetric if the sum of the first
    n digits of x is equal to the sum of the last n digits of x. Numbers with an
    odd number of digits are never symmetric.

    Return the number of symmetric integers in range [low, high].
    '''
    # brute force
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        answer = 0
        for i in range(low, high+1):
            s = str(i)
            if len(s) % 2:
                continue
            a = sum(ord(c) for c in s[:len(s)//2])
            b = sum(ord(c) for c in s[len(s)//2:])
            if a == b:
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1, 100
        o = 9
        self.assertEqual(s.countSymmetricIntegers(*i), o)

    def test_two(self):
        s = Solution()
        i = 1200, 1230
        o = 4
        self.assertEqual(s.countSymmetricIntegers(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)