# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer num. Rearrange the digits of num such that its value is
    minimized and it does not contain any leading zeros.

    Return the rearranged number with minimal value.

    Note that the sign of the number does not change after rearranging the
    digits.
    '''
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num < 0:
            return -int(''.join(sorted(str(abs(num)), reverse=True)))
        num = str(num)
        zeros = num.count('0')
        num = sorted(n for n in num if n != '0')
        return int(num[0] + ('0' * zeros) + ''.join(num[1:]))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 310
        o = 103
        self.assertEqual(s.smallestNumber(i), o)

    def test_two(self):
        s = Solution()
        i = -7605
        o = -7650
        self.assertEqual(s.smallestNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)