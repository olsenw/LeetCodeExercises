# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive integer num consisting of exactly four digits. Split num
    into two new integers new1 and new2 by using the digits found in num.
    Leading zeros are allowed in new1 and new2, and all the digits found in num
    must be used.

    Return the minimum possible sum of new1 and new2.
    '''
    def minimumSum(self, num: int) -> int:
        num = [int(i) for i in sorted(str(num))]
        return num[0] * 10 + num[2] + num[1] * 10 + num[3]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2932
        o = 52
        self.assertEqual(s.minimumSum(i), o)

    def test_two(self):
        s = Solution()
        i = 4009
        o = 13
        self.assertEqual(s.minimumSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)