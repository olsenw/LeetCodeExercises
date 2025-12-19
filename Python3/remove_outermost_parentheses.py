# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A valid parentheses string is either empty "", "(" + A + ")", or A + B,
    where A and B are valid parentheses string, and + represents string
    concatenation.

    A valid parentheses string s is primitive if it is nonempty, and there does
    not exist a way to split it into s = A + B, with A and B nonempty valid
    parentheses strings.

    Given a valid parentheses string s, consider its primitive decomposition:
    s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

    Return s after removing the outermost parentheses of every primitive string
    in the primitive decomposition of s.
    '''
    # does not maintain order
    def removeOuterParentheses_fails(self, s: str) -> str:
        answer = ""
        a = ""
        p = 0
        for c in s:
            if c == '(':
                p += 1
            else:
                if p > 1:
                    a = '(' + a + ')'
                p -= 1
                if p == 0:
                    answer += a
                    a = ""
        return answer + a

    def removeOuterParentheses(self, s: str) -> str:
        answer = ""
        start = 0
        open = 0
        for i in range(len(s)):
            if s[i] == '(':
                open += 1
            else:
                open -= 1
            if open == 0:
                answer += s[start+1:i]
                start = i + 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "(()())(())"
        o = "()()()"
        self.assertEqual(s.removeOuterParentheses(i), o)

    def test_two(self):
        s = Solution()
        i = "(()())(())(()(()))"
        o = "()()()()(())"
        self.assertEqual(s.removeOuterParentheses(i), o)

    def test_three(self):
        s = Solution()
        i = "()()"
        o = ""
        self.assertEqual(s.removeOuterParentheses(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)