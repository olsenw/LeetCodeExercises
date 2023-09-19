# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A parentheses string is valid if and only if:
    * It is the empty string,
    * It can be written as AB (A concatenated with B), where A and B are valid
      strings, or
    * It can be written as (A), where is A is a valid string.

    Given a parentheses string s. In one move, it is possible to insert a
    parenthesis at any position of the string.

    Return the minimum number of moves required to make s valid.
    '''
    # wrong... order of parens matters
    def minAddToMakeValid_wrong(self, s: str) -> int:
        left = 0
        right = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
        return max(left, right) - min(left, right)

    def minAddToMakeValid(self, s: str) -> int:
        answer = 0
        left = 0
        for c in s:
            if c == '(':
                left += 1
            elif left > 0:
                left -= 1
            else:
                answer += 1
        return answer + left

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "())"
        o = 1
        self.assertEqual(s.minAddToMakeValid(i), o)

    def test_two(self):
        s = Solution()
        i = "((("
        o = 3
        self.assertEqual(s.minAddToMakeValid(i), o)

    def test_three(self):
        s = Solution()
        i = "()))(("
        o = 4
        self.assertEqual(s.minAddToMakeValid(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)