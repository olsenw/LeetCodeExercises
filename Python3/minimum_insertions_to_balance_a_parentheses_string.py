# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a parentheses string s containing only the characters '(' and ')'. A
    parentheses string is balanced f:
    * Any left parenthesis '(' mus have a corresponding two consecutive right
      parenthesis '))'.
    * Left parentheses '(' must go before the corresponding two consecutive
      right parenthesis '))'.
    
    In other words, '(' is an opening parenthesis and '))' is a closing
    parenthesis.

    It is possible to insert the characters '(' and ')' at any position of the
    string to balance it if needed.

    Return the minimum number of insertions needed to make s balanced.
    '''
    def minInsertions(self, s: str) -> int:
        answer = 0
        left = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '(':
                left += 1
            else:
                if i+1 < n and s[i+1] == ')':
                    i += 1
                else:
                    answer += 1
                if left > 0:
                    left -= 1
                else:
                    answer += 1
            i += 1
        return answer + 2 * left

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "(()))"
        o = 1
        self.assertEqual(s.minInsertions(i), o)

    def test_two(self):
        s = Solution()
        i = "())"
        o = 0
        self.assertEqual(s.minInsertions(i), o)

    def test_three(self):
        s = Solution()
        i =  "))())("
        o = 3
        self.assertEqual(s.minInsertions(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)