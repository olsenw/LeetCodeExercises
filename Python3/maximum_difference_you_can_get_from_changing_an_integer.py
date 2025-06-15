# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer num. Apply the following steps to nums two separate times:
    * Pick a digit x (0 <= x <= 9).
    * Pick another digit y (0 <= y <= 9). Note y can be equal to x.
    * Replace all the occurrences of x in the decimal representation of num by
      y.

    Let a and b be the two results from applying the operation to num
    independently.

    Return the max difference between a and b.

    Note that neither a nor b may have any leading zeros, and must not be 0.
    '''
    def maxDiff(self, num: int) -> int:
        a = b = num = str(num)
        for c in num:
            if c != '9':
                a = num.replace(c, '9')
                break
        # for c in num:
        #     if c != '1':
        #         num.replace(c, '1')
        if num[0] != '1' or len(num) == 1:
            b = num.replace(num[0], '1')
        else:
            for c in num[1:]:
                if c != '1' and c != '0':
                    b = num.replace(c, '0')
                    break
        return int(a) - int(b)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 555
        o = 888
        self.assertEqual(s.maxDiff(i), o)

    def test_two(self):
        s = Solution()
        i = 9
        o = 8
        self.assertEqual(s.maxDiff(i), o)

    def test_three(self):
        s = Solution()
        i = 1555
        o = 8555
        self.assertEqual(s.maxDiff(i), o)

    def test_four(self):
        s = Solution()
        i = 1118
        o = 8888
        self.assertEqual(s.maxDiff(i), o)

    def test_five(self):
        s = Solution()
        i = 1101057
        o = 8808050
        self.assertEqual(s.maxDiff(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)