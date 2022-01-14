# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Implement the myAtoi(string s) function which converts a string to a
    32-bit signed integer (similar to C/C++ atoi function).

    See code comments for the algorithm/assumptions used.
    '''
    def myAtoi(self, s: str) -> int:
        # setup
        index = 0 # index in string
        sign = 1
        digits = ""
        number = 0

        # 1) read/parse/ignore whitespace
        while index < len(s):
            if not s[index].isspace():
                break
            index += 1

        # 2) check if character is "+" or "-" (assume positive)
        # don't forget to bounds check (ie empty string)
        if index < len(s) and (s[index] == "+" or s[index] == "-"):
            # ord("+") = 43 while ord("-") = 45 force sign to be 1 or -1
            sign = 44 - ord(s[index])
            index += 1

        # 3) read characters until next non-digit character
        digits = index
        while index < len(s):
            if not s[index].isdigit():
                break
            index += 1
        digits = s[digits:index]

        # 4) convert digits into signed integer (assume zero)
        for d in digits:
            # update significant digit
            number *= 10
            # ord("0") = 48 ord("1") = 49 ... ord("9") = 57
            number += ord(d) - 48
        number *= sign

        # 5) clamp integer to [-2^31, 2^31 - 1] range
        # this only works because python allows inf length integers
        # otherwise this would have to been checked during conversion
        number = max(min(2**31 - 1, number), -2**31)

        # 6) return final result
        return number

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "42"
        o = 42
        self.assertEqual(s.myAtoi(i), o)

    def test_two(self):
        s = Solution()
        i = "   -42"
        o = -42
        self.assertEqual(s.myAtoi(i), o)

    def test_three(self):
        s = Solution()
        i = "4193 with words"
        o = 4193
        self.assertEqual(s.myAtoi(i), o)

    def test_four(self):
        s = Solution()
        i = ""
        o = 0
        self.assertEqual(s.myAtoi(i), o)

    def test_five(self):
        s = Solution()
        i = "Only Words"
        o = 0
        self.assertEqual(s.myAtoi(i), o)

    def test_six(self):
        s = Solution()
        i = "-negative 0"
        o = 0
        self.assertEqual(s.myAtoi(i), o)

    def test_seven(self):
        s = Solution()
        i = "- 123 space after sign"
        o = 0
        self.assertEqual(s.myAtoi(i), o)

    def test_eight(self):
        s = Solution()
        i = "2147483648"
        o = 2147483647
        self.assertEqual(s.myAtoi(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)