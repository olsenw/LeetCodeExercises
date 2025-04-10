# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given three integers start, finish, and limit. Also given a 0-indexed string
    s representing a positive integer.

    A positive integer x is called powerful if it ends with s (in other words s
    is a suffix of x) and each digit in x is a most limit.

    Return the total number of powerful integers in the range [start..finish].

    A string x is a suffix of a string y if and only if x is a substring of y
    that starts from some index (including 0) in y and extends to the index
    y.length - 1. For example, 25 is a suffix of 5125 whereas 512 is not.
    '''
    def numberOfPowerfulInt_brute(self, start: int, finish: int, limit: int, s: str) -> int:
        answer = 0
        for x in range(start, finish+1):
            y = str(x)
            if all(ord(c)-48 <= limit for c in y) and y.endswith(s):
                answer += 1
        return answer

    # Based on Leetcode combinatorial editorial
    # https://leetcode.com/problems/count-the-number-of-powerful-integers/editorial/?envType=daily-question&envId=2025-04-10
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def calculate(test:str) -> int:
            # test string too short to have suffix s
            if len(test) < len(s):
                return 0
            # test is same length, so only valid if greater than s
            if len(test) == len(s):
                # string compare lexographically greatest
                return 1 if test >= s else 0
            answer = 0
            testSuffix = test[len(test) - len(s):]
            # how many positions to work with
            l = len(test) - len(s)
            for i in range(l):
                if limit < int(test[i]):
                    answer += (limit + 1) ** (l - i)
                    return answer
                answer += int(test[i]) * (limit + 1) ** (l - 1 - i)
            if testSuffix >= s:
                answer += 1
            return answer
        return calculate(str(finish)) - calculate(str(start-1))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 1, 6000, 4, '124'
        o = 5
        self.assertEqual(s.numberOfPowerfulInt(*i), o)

    def test_two(self):
        s = Solution()
        i = 15, 215, 6, "10"
        o = 2
        self.assertEqual(s.numberOfPowerfulInt(*i), o)

    def test_three(self):
        s = Solution()
        i = 1000, 2000, 4, "3000"
        o = 0
        self.assertEqual(s.numberOfPowerfulInt(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)