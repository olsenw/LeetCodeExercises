# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import zip_longest
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two non-negative integers, num1 and num2 represented as strings,
    return the sum of num1 and num2 as a string.

    Solve this problem without using any built-in libraries for handling large
    integers or by converting the inputs to integers directly.
    '''
    def addStrings_passes(self, num1: str, num2: str) -> str:
        answer = []
        carry = 0
        for a,b in zip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            step = int(a) + int(b) + carry
            carry = 0
            if step > 9:
                step -= 10
                carry = 1
            answer.append(str(step))
        if carry:
            answer.append("1")
        return "".join(answer[::-1])

    def addStrings(self, num1: str, num2: str) -> str:
        answer = []
        carry = 0
        for a,b in zip_longest(num1[::-1],num2[::-1],fillvalue="0"):
            step = int(a) + int(b) + carry
            carry = step // 10
            answer.append(str(step % 10))
        if carry:
            answer.append(str(carry))
        return "".join(answer[::-1])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "11"
        j = "123"
        o = "134"
        self.assertEqual(s.addStrings(i,j), o)

    def test_two(self):
        s = Solution()
        i = "456"
        j = "77"
        o = "533"
        self.assertEqual(s.addStrings(i,j), o)

    def test_three(self):
        s = Solution()
        i = "0"
        j = "0"
        o = "0"
        self.assertEqual(s.addStrings(i,j), o)

    def test_four(self):
        s = Solution()
        i = "999"
        j = "1"
        o = "1000"
        self.assertEqual(s.addStrings(i,j), o)

    def test_five(self):
        s = Solution()
        i = "999"
        j = "101"
        o = "1100"
        self.assertEqual(s.addStrings(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)