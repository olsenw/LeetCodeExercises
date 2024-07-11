# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s that consists of lower case English letters and brackets.

    Reverse the strings in each pair of matching parentheses, starting from the
    innermost one.

    The result should not contain any brackets.
    '''
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for c in s:
            if c == '(':
                stack.append("")
            elif c == ')':
                c = stack.pop()[::-1]
                stack[-1] += c
            else:
                stack[-1] += c
        return stack[-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "(abcd)"
        o = "dcba"
        self.assertEqual(s.reverseParentheses(i), o)

    def test_two(self):
        s = Solution()
        i = "(u(love)i)"
        o = "iloveu"
        self.assertEqual(s.reverseParentheses(i), o)

    def test_three(self):
        s = Solution()
        i = "(ed(et(oc))el)"
        o = "leetcode"
        self.assertEqual(s.reverseParentheses(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)