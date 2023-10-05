# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n, return a binary string representing its representation
    in base -2.

    Note that the string should not have leading zeros unless the string is "0".
    '''
    # based on solution by bupt_wc
    # https://leetcode.com/problems/convert-to-base-2/solutions/265688/4-line-python-clear-solution-with-explanation/
    def baseNeg2(self, n: int) -> str:
        for i in range(1,33,2):
            # mask of ones that result in positive increases
            # (-2)^0 (-2)^2 (-2)^4 ... (-2)^32
            mask = 1 << i
            # check if mask is set in n already
            if n & mask:
                # this left shits the mask by one
                n += mask * 2
        return bin(n)[2:]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        o = "110"
        self.assertEqual(s.baseNeg2(i), o)

    def test_two(self):
        s = Solution()
        i = 3
        o = "111"
        self.assertEqual(s.baseNeg2(i), o)

    def test_three(self):
        s = Solution()
        i = 4
        o = "100"
        self.assertEqual(s.baseNeg2(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)