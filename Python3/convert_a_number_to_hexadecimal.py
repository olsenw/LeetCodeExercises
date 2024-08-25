# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 32-bit integer num, return a string representing its hexadecimal
    representation. For negative integers, two's complement method is used.

    All the letters in the answer string should be lowercase characters, and
    there should not be any leading zeros in the answer except for zero itself.

    Note: it is not permitted to use a built-in library method to directly solve
    this problem.
    '''
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        # twos complement
        if num < 0:
            num = ((2**32 - 1) ^ (-num)) + 1
        answer = ""
        while num > 0:
            if num % 16 > 9:
                answer += chr(ord('a') + num % 16 - 10)
            else:
                answer += str(num % 16)
            num //= 16
        return answer[::-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 26
        o = "1a"
        self.assertEqual(s.toHex(i), o)

    def test_two(self):
        s = Solution()
        i = -1
        o = "ffffffff"
        self.assertEqual(s.toHex(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)