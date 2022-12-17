# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +,-,*, and /. Each operand may be an integer or another
    expression.

    Note that division between two integers should truncate toward zero.

    It is guaranteed that the given RPN expression is always valid. That means
    the expression always evaluate to a result, and there will not be any
    division by zero operation.
    '''
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        d = {
            '+': lambda b,a: a+b,
            '-': lambda b,a: a-b,
            '*': lambda b,a: a*b,
            '/': lambda b,a: -(abs(a)//abs(b)) if (a < 0) ^ (b < 0) else a//b,
        }
        for c in tokens:
            s.append(d[c](s.pop(),s.pop()) if c in d else int(c))
        return s[-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["2","1","+","3","*"]
        o = 9
        self.assertEqual(s.evalRPN(i), o)

    def test_two(self):
        s = Solution()
        i = ["4","13","5","/","+"]
        o = 6
        self.assertEqual(s.evalRPN(i), o)

    def test_three(self):
        s = Solution()
        i = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        o = 22
        self.assertEqual(s.evalRPN(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)