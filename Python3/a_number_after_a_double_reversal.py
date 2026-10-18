# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Reversing an integer means to reverse all ts digits.

    Given an integer num, reverse num to get reversed1, then reverse reversed1
    to get reversed2. Return true if reversed2 equals num. Otherwise return
    false.
    '''
    def isSameAfterReversals_brute(self, num: int) -> bool:
        r1 = int(str(num)[::-1])
        r2 = int(str(r1)[::-1])
        return num == r2

    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 > 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 526
        o = True
        self.assertEqual(s.isSameAfterReversals(i), o)

    def test_two(self):
        s = Solution()
        i = 1800
        o = False
        self.assertEqual(s.isSameAfterReversals(i), o)

    def test_three(self):
        s = Solution()
        i = 0
        o = True
        self.assertEqual(s.isSameAfterReversals(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)