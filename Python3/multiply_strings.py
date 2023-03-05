# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import zip_longest
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two non-negative integers num1 and num2 represented as strings, return
    the product of num1 and num2, also represented as a string.

    Note: do not use any built-in big integer libraries or convert the inputs to
    integers directly.
    '''
    # wow... this passed... barely 
    def multiply_slow(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        # all the multiplications
        interim = []
        for i, x in enumerate(num2[::-1]):
            for j, y in enumerate(num1[::-1]):
                # answer.append((int(x) * int(y), i + j))
                number = [d for d in str(int(x) * int(y))] + [0] * (i + j)
                interim.append(number[::-1])
        # add up the multiplications
        answer = ["0"]
        for i in interim:
            current = []
            carry = 0
            for x,y in zip_longest(answer, i, fillvalue="0"):
                number = int(x) + int(y) + carry
                current.append(str(number % 10))
                carry = number // 10
            if carry:
                current.append("1")
            answer = current
        return ''.join(answer[::-1])

    # based on LeetCode solution approach 3
    # https://leetcode.com/problems/multiply-strings/editorial/
    # much smart here
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        answer = [0] * (len(num1) + len(num2))
        for i,x in enumerate(num2[::-1]):
            for j,y in enumerate(num1[::-1]):
                zeros = i + j
                carry = answer[zeros]
                number = int(x) * int(y) + carry
                answer[zeros] = number % 10
                answer[zeros + 1] += number // 10
        if answer[-1] == 0:
            answer.pop()
        return ''.join(str(d) for d in reversed(answer))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "2"
        j = "3"
        o = "6"
        self.assertEqual(s.multiply(i,j), o)

    def test_two(self):
        s = Solution()
        i = "123"
        j = "456"
        o = "56088"
        self.assertEqual(s.multiply(i,j), o)

    def test_three(self):
        s = Solution()
        i = "1" * 200
        j = "2" * 200
        o = "246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580246913580241975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308641975308642"
        self.assertEqual(s.multiply(i,j), o)

    def test_four(self):
        s = Solution()
        i = "9" * 200
        j = "9" * 200
        o = "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001"
        self.assertEqual(s.multiply(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)