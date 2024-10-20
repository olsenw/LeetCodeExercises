# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A boolean expression is an expression that evaluates to either true or
    false. It can be in one of the following shapes:
    * 't' that evaluates to true.
    * 'f' that evaluates to false.
    * '!(subExpr)' that evaluates to the logical NOT of the inner expression
      subExpr.
    * '&(subExpri, subExpr2, ..., subExprn)' that evaluates to the logical AND
      of the inner expression subExpr1, subExpr2, ..., subExprn where n >= 1.
    * '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of
      the inner expression subExpr1, subExpr2, ..., subExprn where n >= 1.
    
    Given a string expression that represents a boolean expression, return the
    evaluation of that expression.

    It is guaranteed that the given expression is valid and follows the given
    rules.
    '''
    def n(self, expression: str) -> bool:
        return not(self.parseBoolExpr(expression))
    def o(self, expression: str) -> bool:
        answer = False
        p = 0
        e = ""
        for c in expression:
            if c == ',' and p == 0:
                answer |= self.parseBoolExpr(e)
                e = ""
            elif c == '(':
                p += 1
                e += c
            elif c == ')':
                p -= 1
                e += c
            else:
                e += c
        return answer | self.parseBoolExpr(e)
    def a(self, expression: str) -> bool:
        answer = True
        p = 0
        e = ""
        for c in expression:
            if c == ',' and p == 0:
                answer &= self.parseBoolExpr(e)
                e = ""
            elif c == '(':
                p += 1
                e += c
            elif c == ')':
                p -= 1
                e += c
            else:
                e += c
        return answer & self.parseBoolExpr(e)
    def parseBoolExpr(self, expression: str) -> bool:
        n = len(expression)
        if expression[0] == 't':
            return True
        elif expression[0] == 'f':
            return False
        elif expression[0] == '!':
            return self.n(expression[2:n-1])
        elif expression[0] == '|':
            return self.o(expression[2:n-1])
        elif expression[0] == '&':
            return self.a(expression[2:n-1])
        else:
            raise Exception("bad character")

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "&(|(f))"
        o = False
        self.assertEqual(s.parseBoolExpr(i), o)

    def test_two(self):
        s = Solution()
        i = "|(f,f,f,t)"
        o = True
        self.assertEqual(s.parseBoolExpr(i), o)

    def test_three(self):
        s = Solution()
        i = "!(&(f,t))"
        o = True
        self.assertEqual(s.parseBoolExpr(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)