# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A parentheses string is a non-empty string consisting only of '(' and ')'.
    It is valid if any of the following conditions is true:
    * It is ().
    * It can be written as AB (A concatenated with B), where A and B are valid
      parentheses strings.
    * It can be written as (A), where A is a valid parentheses string.

    Given a parentheses string s and a string locked, both of length n. locked
    is a binary string consisting only of '0's and '1's. For each index i of
    locked,
    * If locked[i] is '1', it is impossible to change s[i].
    * If locked[i] is '0', it is possible to change s[i] to either '(' or ')'.

    Return true if is is possible to make s a valid parentheses string.
    Otherwise, return false.
    '''
    def canBeValid_fails(self, s: str, locked: str) -> bool:
        n = len(s)
        stack = []
        for i in range(n):
            if locked[i] == '1':
                if s[i] == ')':
                    if stack:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append('(')
            else:
                stack.append('*')
        pass
        # while len(stack) > 1 and stack[-1] == '*':
        #     stack.pop()
        #     stack.pop()
        open, free = 0, 0
        for c in stack:
            if c == '(':
                open += 1
            elif open:
                open -= 1
            else:
                free += 1
        return open == 0 and free % 2 == 0

    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        s = ''.join(s[i] if locked[i] == '1' else '*' for i in range(n))
        stack = [['*',0]]
        for c in s:
            if c == ')':
                if stack[-1][0] == '(':
                    _,f = stack.pop()
                    stack[-1][1] += f
                elif stack[-1][1]:
                    stack[-1][1] -= 1
                else:
                    return False
            elif c == '*':
                stack[-1][1] += 1
            else:
                stack.append(['(',0])
        while len(stack) > 1:
            if stack[-1][1]:
                _,f = stack.pop()
                stack[-1][1] += f - 1
            else:
                return False
        return stack[-1][1] % 2 == 0

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "))()))"
        j = "010100"
        o = True
        self.assertEqual(s.canBeValid(i,j), o)

    def test_two(self):
        s = Solution()
        i = "()()"
        j = "0000"
        o = True
        self.assertEqual(s.canBeValid(i,j), o)

    def test_three(self):
        s = Solution()
        i = ")"
        j = "0"
        o = False
        self.assertEqual(s.canBeValid(i,j), o)

    def test_four(self):
        s = Solution()
        i = "((()(()()))()((()()))))()((()(()"
        j = "10111100100101001110100010001001"
        o = True
        self.assertEqual(s.canBeValid(i,j), o)

    def test_five(self):
        s = Solution()
        i = "())()))()(()(((())(()()))))((((()())(())"
        j = "1011101100010001001011000000110010100101"
        o = True
        self.assertEqual(s.canBeValid(i,j), o)

    def test_six(self):
        s = Solution()
        i = "()()))()())(((()((()((()((()()()))(()()((()((()()(((()())))))()((()(()(())((()()((())))))))(())(())))()()()((()())())(()()))((((((())()())())))))())((((()())(())(())()()()(()(()((()))((((()((()((()())(())((((())(())))(()((((())))((()(((((()()))))((((()))))())()))))())"
        j = "0111000100000011110100010110101001110111010111110111111011101000100000011101010000110110001100100100100011000001110101101110011000000011111000111111111001011101100000100111010111010000001100011101000110101011001000100100111110110110100101010111111001000010000010010010"
        o = True
        self.assertEqual(s.canBeValid(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)