# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import cycle, repeat, zip_longest
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    For two strings s and t, it is said that "t divides s" if and only if
    s = t + .... + t (ie t is concatenated with itself one or more times).

    Given two strings str1 and str2, return the largest string x such that x
    divides both str1 and str2.
    '''
    # feels very brutish
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        answer = str1 if len(str1) > len(str2) else str2
        def gcd(s, t):
            if len(s) % len(t):
                return False
            for i,j in zip(s, cycle(t)):
                if i != j:
                    return False
            return True
        while answer and (gcd(str1, answer) == False or gcd(str2, answer) == False):
            answer = answer[:-1]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ABCABC"
        j = "ABC"
        o = "ABC"
        self.assertEqual(s.gcdOfStrings(i,j), o)

    def test_two(self):
        s = Solution()
        i = "ABABAB"
        j = "ABAB"
        o = "AB"
        self.assertEqual(s.gcdOfStrings(i,j), o)

    def test_three(self):
        s = Solution()
        i = "LEET"
        j = "CODE"
        o = ""
        self.assertEqual(s.gcdOfStrings(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)