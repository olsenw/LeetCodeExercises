# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s of '(' ')' and lowercase English characters.

    Remove the minimum number of parentheses (in any position) so that
    the resulting parentheses string is valid and return any valid
    string.

    Formally, a parentheses string is valid if and only if some of the
    following hold:
    * It is the empty string
    * It contains only lowercase letters
    * It can be written as AB (A concatenated with B), where A and B are
      valid strings
    * It can be written as (A), where A is a valid string
    '''
    def minRemoveToMakeValid(self, s: str) -> str:
        from collections import deque
        stack = deque([''])
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append('')
            elif s[i] == ')':
                if len(stack) > 1:
                    t = f'({stack.pop()})'
                    stack[-1] += t
            else:
                stack[-1] += s[i]
            i += 1
        return ''.join(stack)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "lee(t(c)o)de)"
        o = "lee(t(c)o)de"
        #   "lee(t(co)de)"
        #   "lee(t(c)ode)"
        self.assertEqual(s.minRemoveToMakeValid(i), o)

    def test_two(self):
        s = Solution()
        i = "a)b(c)d"
        o = "ab(c)d"
        self.assertEqual(s.minRemoveToMakeValid(i), o)

    def test_three(self):
        s = Solution()
        i = "))(("
        o = ""
        self.assertEqual(s.minRemoveToMakeValid(i), o)

    def test_four(self):
        s = Solution()
        i = "(a(b)"
        o = "a(b)" # or "(ab)"
        self.assertEqual(s.minRemoveToMakeValid(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)