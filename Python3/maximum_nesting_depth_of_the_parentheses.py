# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A string is a valid parentheses string (denoted VPS) if it meets one of the
    following:
    * It is an empty string "", or a single character not equal to "(" or ")",
    * It can be written as AB (A concatenated with B), where A and B are VPS's,
    * It can be written as (A), where A is a VPS.

    The nesting depth depth(s) of any VPS S can be defined as follows:
    * depth("") = 0
    * depth(C) = 0, where C is a string with a single character not equal to "("
      or ")".
    * depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
    * depth("(" + A + ")") = 1 + depth(A), where A is a VPS.

    Given a VPS represented as string s, return the nesting depth of s.
    '''
    def maxDepth(self, s: str) -> int:
        answer = 0
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
                answer = max(answer, depth)
            elif c == ')':
                depth -= 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "(1+(2*3)+((8)/4))+1"
        o = 3
        self.assertEqual(s.maxDepth(i), o)

    def test_two(self):
        s = Solution()
        i = "(1)+((2))+(((3)))"
        o = 3
        self.assertEqual(s.maxDepth(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)