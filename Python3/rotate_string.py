# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s and goal, return true if and only if s can become goal
    after some number of shifts on s.

    A shift on s consists of moving the leftmost character of s to the rightmost
    position.
    '''
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        return goal in s + s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcde", "cdeab"
        o = True
        self.assertEqual(s.rotateString(*i), o)

    def test_two(self):
        s = Solution()
        i = "abcde", "abced"
        o = False
        self.assertEqual(s.rotateString(*i), o)

    def test_three(self):
        s = Solution()
        i = "aa", "a"
        o = False
        self.assertEqual(s.rotateString(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)