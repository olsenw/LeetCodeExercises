# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    An additive number is a string whose digits can form an additive sequence.

    A valid additive sequence should contain at least three numbers. Except for
    the first two numbers, each subsequent number in the sequence must be the
    sum of the preceding two.

    Given a string containing only digits, return true if it is an additive
    number or false otherwise.

    Note: Numbers in the additive sequence cannot have leading zeros, so
    sequence 1,2,03 or 1,02,3 is invalid.
    '''
    def isAdditiveNumber(self, num: str) -> bool:
        # for value a and value b find in s
        # a + b = s[:i] and backtrack(b,s[:i],s[i:])
        def backtrack(a:int, b:int, s:str) -> bool:
            if len(s) == 0:
                return True
            for i in range(1,len(s)+1):
                c = int(s[:i])
                if c < (i-1) * 10:
                    break # leading zero detected
                if a + b == c and backtrack(b, c, s[i:]):
                    return True
            return False
        answer = False
        for i in range(1,len(num)):
            a = int(num[:i])
            if i > 1 and num[0] == '0':
                break # leading zero detected
            for j in range(i+1,len(num)):
                b = int(num[i:j])
                if j-i > 1 and num[i] == '0':
                    break # leading zero detected
                answer = answer or backtrack(a,b,num[j:])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "199100199"
        o = True
        self.assertEqual(s.isAdditiveNumber(i), o)

    def test_two(self):
        s = Solution()
        i = "112358"
        o = True
        self.assertEqual(s.isAdditiveNumber(i), o)

    def test_three(self):
        s = Solution()
        i = "0101020"
        o = True
        self.assertEqual(s.isAdditiveNumber(i), o)

    def test_four(self):
        s = Solution()
        i = "011112"
        o = False
        self.assertEqual(s.isAdditiveNumber(i), o)

    def test_five(self):
        s = Solution()
        i = "44"
        o = False
        self.assertEqual(s.isAdditiveNumber(i), o)

    def test_six(self):
        s = Solution()
        i = "23"
        o = False
        self.assertEqual(s.isAdditiveNumber(i), o)

    def test_seven(self):
        s = Solution()
        i = "123"
        o = True
        self.assertEqual(s.isAdditiveNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)