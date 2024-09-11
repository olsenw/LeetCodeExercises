# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A bit flip of a number x is choosing a bit in the binary representation of x
    and flipping it from either 0 to 1 or 1 to 0.

    Given two integers start and goal, return the minimum number of bit flips to
    convert start to goal.
    '''
    def minBitFlips(self, start: int, goal: int) -> int:
        answer = 0
        while start or goal:
            if start & 1 != goal & 1:
                answer += 1
            start >>= 1
            goal >>= 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 10, 7
        o = 3
        self.assertEqual(s.minBitFlips(*i), o)

    def test_two(self):
        s = Solution()
        i = 3, 4
        o = 3
        self.assertEqual(s.minBitFlips(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)