# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a balanced parentheses string s, return the score of the
    string.

    The score of a balanced parentheses string is based on the following
    rule:
    * "()" has a score 1.
    * AB has score A + B, where A and B are balanced parentheses
      strings.
    * (A) has a score 2 * A where A is a balanced parentheses string.
    '''
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                score = 2 * stack.pop()
                if not score:
                    score = 1
                stack[-1] += score
        return stack[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "()"
        o = 1
        self.assertEqual(s.scoreOfParentheses(i), o)

    def test_two(self):
        s = Solution()
        i = "(())"
        o = 2
        self.assertEqual(s.scoreOfParentheses(i), o)

    def test_three(self):
        s = Solution()
        i = "()()"
        o = 2
        self.assertEqual(s.scoreOfParentheses(i), o)

    def test_four(self):
        s = Solution()
        i = "()(())"
        o = 3
        self.assertEqual(s.scoreOfParentheses(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)