# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n.

    Form a new integer x by concatenating all the non-zero digits of n in their
    original order. If there are no non-zero digits, x = 0.

    Let sum be the sum of digits in x.

    Return an integer representing the value of x * sum.
    '''
    def sumAndMultiply(self, n: int) -> int:
        x = [s for s in str(n) if s != '0']
        if len(x) == 0:
            x.append('0')
        y = sum(int(s) for s in x)
        return int(''.join(x)) * y

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10203004
        o = 12340
        self.assertEqual(s.sumAndMultiply(i), o)

    def test_two(self):
        s = Solution()
        i = 1000
        o = 1
        self.assertEqual(s.sumAndMultiply(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)