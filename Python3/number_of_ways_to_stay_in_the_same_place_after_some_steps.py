# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a pointer at index 0 in an array of size arrLen. At each step, it is
    possible to move 1 position to the left, 1 position to the right, or stay in
    the same place (The pointer is unable to leave the bounds of the array).

    Given two integers steps and arrLen, return the number of ways that the
    pointer remains at index 0 after exactly steps steps. Since the answer may
    be large, return it modulo 10^9 + 7.
    '''
    def numWays(self, steps: int, arrLen: int) -> int:
        m = 10**9 + 7
        # current index of pointer and remaining steps
        @cache
        def dp(i, r):
            # unable to move
            if r == 0:
                return 1 if i == 0 else 0
            answer = 0
            # move left
            if i > 0:
                answer += dp(i - 1, r - 1)
            # move right
            if i < arrLen - 1:
                answer += dp(i + 1, r - 1)
            # stay still
            answer += dp(i, r - 1)
            # cheating a bit here because python has no upper int limit
            return answer % m
        return dp(0, steps)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 3
        j = 2
        o = 4
        self.assertEqual(s.numWays(i,j), o)

    def test_two(self):
        s = Solution()
        i = 2
        j = 4
        o = 2
        self.assertEqual(s.numWays(i,j), o)

    def test_three(self):
        s = Solution()
        i = 4
        j = 2
        o = 8
        self.assertEqual(s.numWays(i,j), o)

    def test_four(self):
        s = Solution()
        i = 500
        j = 1000000
        o = 374847123
        self.assertEqual(s.numWays(i,j), o)

    def test_five(self):
        s = Solution()
        i = 500
        j = 100
        o = 459871446
        self.assertEqual(s.numWays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)