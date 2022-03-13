# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s containing just the characters "(){}[]" determine
    if the input string is valid.

    An input string is valid if
    * Open brackets must be closed by the same
      type of brackets.
    * Open brackets must be closed in the correct order.
    '''
    def isValid_match_case(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case '(':
                    stack.append(c)
                case ')':
                    if not stack or '(' != stack.pop():
                        return False
                case '{':
                    stack.append(c)
                case '}':
                    if not stack or '{' != stack.pop():
                        return False
                case '[':
                    stack.append(c)
                case ']':
                    if not stack or '[' != stack.pop():
                        return False
                case _:
                    return False
        return False if stack else True

    def isValid_if_ladder(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif not stack or c != stack.pop():
                return False
        return False if stack else True

    pairs = {'(':')','{':'}','[':']'}
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.pairs:
                stack.append(self.pairs[c])
                continue
            if not stack:
                return False
            p = stack.pop()
            if c != p:
                return False
        return False if stack else True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "()"
        o = True
        self.assertEqual(s.isValid(i), o)

    def test_two(self):
        s = Solution()
        i = "(){}[]"
        o = True
        self.assertEqual(s.isValid(i), o)

    def test_three(self):
        s = Solution()
        i = "(]"
        o = False
        self.assertEqual(s.isValid(i), o)

    def test_four(self):
        s = Solution()
        i = "("
        o = False
        self.assertEqual(s.isValid(i), o)

    def test_five(self):
        s = Solution()
        i = "]"
        o = False
        self.assertEqual(s.isValid(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)