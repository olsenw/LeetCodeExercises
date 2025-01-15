# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two positive integers num1 and num2, find the positive integer x such
    that:
    * x has the same number of set bits as num2, and
    * The value x XOR num1 is minimal.

    Note that XOR is the bitwise XOR operation.

    Return the integer x. The test cases are generated such that x is uniquely
    determined.

    The number of set bits of an integer is the number of 1's in it binary
    representation.
    '''
    def minimizeXor(self, num1: int, num2: int) -> int:
        answer = [0] * 32
        i = len(answer) - 1
        while i > -1 and num1 > 0:
            answer[i] = num1 & 1
            num1 >>= 1
            i -= 1
        num2 = num2.bit_count()
        pass
        for i in range(len(answer)):
            if answer[i] == 0:
                continue
            if num2 > 0:
                num2 -= 1
            else:
                answer[i] = 0
        pass
        for i in range(len(answer)-1,-1,-1):
            if answer[i] == 1:
                continue
            if num2 > 0:
                num2 -= 1
                answer[i] = 1
            else:
                break
        a = 0
        for i in answer:
            a <<= 1
            a += i
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3, 5
        o = 3
        self.assertEqual(s.minimizeXor(*i), o)

    def test_two(self):
        s = Solution()
        i = 1, 12
        o = 3
        self.assertEqual(s.minimizeXor(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)