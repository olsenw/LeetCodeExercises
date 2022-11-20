# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from cProfile import run
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s representing a valid expression, implement a basic
    calculator to evaluate it, and return the result of the evaluation.

    Note: Do not use any built-in functions which evaluates strings as
    mathematical expressions, such as eval().

    Constraints:
    * 1 <= s.length <= 3 * 10^5
    * s consists of digits, '+', '-', '(', ')', and ' '.
    * s represents a valid expression.
    * '+' is not used as a unary operation (ie, +1 and +(2+3) are invalid).
    * '-' could be used as a unary operation (ie, -1 and -(2+3) are valid).
    * There will not be two consecutive operators in the input.
    * Every number and running calculation will fit in a signed 32-bit integer.
    '''
    def calculate(self, s: str) -> int:
        # used for recursion represented by parentheses
        stack = []
        # running value of current segment
        running = 0
        # operation to execute (True is '+' False is '-')
        operation = True
        # number being parsed
        parse = 0
        # iterate over the string
        for c in s:
            # is digit
            if ord('0') <= ord(c) <= ord('9'):
                parse *= 10
                parse += ord(c) - ord('0')
            # is plus
            # is minus
            elif c == '+' or c == '-':
                running += parse if operation else -parse
                operation = c == '+'
                parse = 0
            # is opening parenthesis
            elif c == '(':
                stack.append((running,operation))
                running = 0
                operation = True
                parse = 0
            # is closing parenthesis
            elif c == ')':
                running += parse if operation else -parse
                parse = running
                running, operation = stack.pop()
            # is space
            else:
                pass
        return running + (parse if operation else -parse)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "1 + 1"
        o = 2
        self.assertEqual(s.calculate(i), o)

    def test_two(self):
        s = Solution()
        i = " 2-1 + 2 "
        o = 3
        self.assertEqual(s.calculate(i), o)

    def test_three(self):
        s = Solution()
        i = "(1+(4+5+2)-3)+(6+8)"
        o = 23
        self.assertEqual(s.calculate(i), o)

    def test_four(self):
        s = Solution()
        i = "-1"
        o = -1
        self.assertEqual(s.calculate(i), o)

    def test_five(self):
        s = Solution()
        i = "1-(     -2)"
        o = 3
        self.assertEqual(s.calculate(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)