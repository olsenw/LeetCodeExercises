# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s which represents an expression, evaluate this
    expression and return its value.

    The integer division should truncate toward zero.

    It is assumed that the given expression is always valid. All 
    intermediate results will be in the range of [-2^31, 2^31-1].

    The string s will only consist of integers, operators '+','-','*',
    '/' and some number of whitespaces.
    '''
    def calculate_stack(self, s: str) -> int:
        def nextArg(i) -> (int, str):
            n = ""
            for c in i:
                if c.isdigit():
                    n += c
                elif c in "+-*/":
                    return (int(n), c)
                else:
                    continue
            return (int(n), '!')
        
        from collections import deque
        d = deque()
        i = iter(s)
        n, o = nextArg(i)
        while o != '!':
            if o=='+' or o=='-':
                d.append(n)
                d.append(o)
            elif o=='*':
                a, o = nextArg(i)
                n = n * a
                continue
            elif o=='/':
                a, o = nextArg(i)
                n = n // a
                continue
            else:
                print('o is', o)
                return False
            n, o = nextArg(i)
        else:
            d.append(n)
        while len(d) >= 3:
            a = d.popleft()
            o = d.popleft()
            b = d.popleft()
            if o == '+':
                d.appendleft(a+b)
            else:
                d.appendleft(a-b)
        return d.pop()

    # based on leetcode solution and discussions
    def calculate_smart(self, s: str) -> int:
        last = 0
        current = 0
        result = 0
        op = '+'
        for c in s:
            if c == ' ':
                continue
            elif c.isdigit():
                current = current * 10 + int(c)
            elif c in "+-*/":
                if op == '+':
                    result += last
                    last = current
                elif op == '-':
                    result += last
                    last = -current
                elif op == '*':
                    last *= current
                elif op == '/':
                    # need this for truncate toward zero
                    # https://stackoverflow.com/questions/19919387/in-python-what-is-a-good-way-to-round-towards-zero-in-integer-division#:~:text=To%20do%20truncation%20towards%20zero%2C%20and%20maintain%20integer,do%20integer%20division%20and%20always%20round%20towards%20zero%3A
                    last = last // current if last * current > 0 else (last + (-last % current)) // current
                current = 0
                op = c
        else:
            if op == '+':
                result += last
                last = current
            elif op == '-':
                result += last
                last = -current
            elif op == '*':
                last *= current
            elif op == '/':
                # need this for truncate toward zero
                # https://stackoverflow.com/questions/19919387/in-python-what-is-a-good-way-to-round-towards-zero-in-integer-division#:~:text=To%20do%20truncation%20towards%20zero%2C%20and%20maintain%20integer,do%20integer%20division%20and%20always%20round%20towards%20zero%3A
                last = last // current if last * current > 0 else (last + (-last % current)) // current
        return result + last

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        i = "3+2*2"
        a = 7
        self.assertEqual(s.calculate_stack(i), a)
        self.assertEqual(s.calculate_smart(i), a)

    def test_two(self):
        s = Solution()
        i = " 3/2 "
        a = 1
        self.assertEqual(s.calculate_stack(i), a)
        self.assertEqual(s.calculate_smart(i), a)

    def test_three(self):
        s = Solution()
        i = " 3+5 / 2 "
        a = 5
        self.assertEqual(s.calculate_stack(i), a)
        self.assertEqual(s.calculate_smart(i), a)

    def test_four(self):
        s = Solution()
        i = "3+3*3/2-1"
        a = 6
        self.assertEqual(s.calculate_stack(i), a)
        self.assertEqual(s.calculate_smart(i), a)

    def test_five(self):
        s = Solution()
        i = " 100 / 2 + 05"
        a = 55
        self.assertEqual(s.calculate_stack(i), a)
        self.assertEqual(s.calculate_smart(i), a)

    def test_six(self):
        s = Solution()
        i = "1-1+1"
        a = 1
        self.assertEqual(s.calculate_stack(i), a)
        self.assertEqual(s.calculate_smart(i), a)

    def test_seven(self):
        s = Solution()
        i = "14-3/2"
        a = 13
        self.assertEqual(s.calculate_stack(i), a)
        self.assertEqual(s.calculate_smart(i), a)

if __name__ == '__main__':
    unittest.main(verbosity=2)