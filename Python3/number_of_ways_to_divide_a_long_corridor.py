# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Along a long library corridor, there is a line of seats and decorative
    plants. Given a 0-indexed string corridor of length n consisting of letters
    'S' and 'P' where each 'S' represents a seat and each 'P' represents a
    plant.

    One room divider has already been installed to the left of index 0, and
    another to the right of index n - 1. Additional room dividers can be
    installed. For each position between indices i - 1 and i (1 <= i <= n-1), at
    most one divider can be installed.

    Divide the corridor into non-overlapping sections, where each section has
    exactly two seats with any number of plants. There may be multiple ways to
    perform the division. Two ways are different if there is a position with a
    room divider installed in the first way but not the second way.

    Return the number of ways to divide the corridor. Since the answer may be
    very large, return it modulo 10^9 + 7. If there is no way, return 0.
    '''
    # based on the hints
    def numberOfWays(self, corridor: str) -> int:
        # if there are an odd number of chairs it is impossible to create
        # sections containing two chairs. (Same for no chairs!)
        c = corridor.count('S')
        if c == 0 or c % 2:
            return 0
        # mark first seats and second seats
        f,l = [], []
        for i,c in enumerate(corridor):
            if c == 'S':
                if len(f) == len(l):
                    f.append(i)
                else:
                    l.append(i)
        f[0] = 0
        l[-1] = len(corridor) - 1
        answer = 1
        for i in range(len(f) - 1):
            answer *= f[i+1] - l[i]
        return answer % (10**9 + 7)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "SSPPSPS"
        o = 3
        self.assertEqual(s.numberOfWays(i), o)

    def test_two(self):
        s = Solution()
        i = "PPSPSP"
        o = 1
        self.assertEqual(s.numberOfWays(i), o)

    def test_three(self):
        s = Solution()
        i = "S"
        o = 0
        self.assertEqual(s.numberOfWays(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)