# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string containing just the characters '(' and ')' find the
    length of the longest valid (well-formed) parentheses substring.
    '''
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        dp = [0] * len(s)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                j = stack.pop()
                dp[i] = 1
                dp[j] = 1
        for i in range(1, len(dp)):
            if dp[i]:
                dp[i] += dp[i-1]
        return max(dp)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "(()"
        o = 2
        self.assertEqual(s.longestValidParentheses(i), o)

    def test_two(self):
        s = Solution()
        i = ")()())"
        o = 4
        self.assertEqual(s.longestValidParentheses(i), o)

    def test_three(self):
        s = Solution()
        i = ""
        o = 0
        self.assertEqual(s.longestValidParentheses(i), o)

    def test_four(self):
        s = Solution()
        i = "))))))))))()()())((((((((((((("
        o = 6
        self.assertEqual(s.longestValidParentheses(i), o)

    def test_five(self):
        s = Solution()
        i = ")))))))))))((((((((((((("
        o = 0
        self.assertEqual(s.longestValidParentheses(i), o)

    def test_six(self):
        s = Solution()
        i = "())()"
        o = 2
        self.assertEqual(s.longestValidParentheses(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)