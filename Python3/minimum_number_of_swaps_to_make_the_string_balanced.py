# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed string s of even length n. The string consists of exactly
    n / 2 opening brackets '[' and n / 2 closing brackets ']'.

    A string is called balanced if and only if:
    * It is the empty string, or
    * It can be written as AB, where both A and B are balanced strings, or
    * It can be written as [C], where C is a balanced string.

    It is possible to swap the brackets at any two indices any number of times.

    Return the minimum number of swaps to make s balanced.
    '''
    # fails
    def minSwaps_fails(self, s: str) -> int:
        answer = 0
        open = 0
        for c in s:
            if c == '[':
                open += 1
            elif open:
                open -= 1
            else:
                answer += 1
        return answer

    # based on hints
    def minSwaps(self, s: str) -> int:
        answer = 0
        open = 0
        closed = 0
        for c in s:
            if c == '[':
                open += 1
            else:
                closed += 1
            if closed > open:
                answer += 1
                open += 1
                closed -= 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "][]["
        o = 1
        self.assertEqual(s.minSwaps(i), o)

    def test_two(self):
        s = Solution()
        i = "]]][[["
        o = 2
        self.assertEqual(s.minSwaps(i), o)

    def test_three(self):
        s = Solution()
        i = "[]"
        o = 0
        self.assertEqual(s.minSwaps(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)