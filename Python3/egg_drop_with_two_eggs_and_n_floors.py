# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two identical eggs and access to a building with n floors labeled from
    1 to n.

    There exists a floor f where 0 <= f <= n such that any egg dropped at a
    floor higher than f will break, and any egg dropped at or below floor f will
    not break.

    In each move, it is possible to an unbroken egg and drop it from any floor x
    (where 1 <= x <= n). If the egg breaks, it can no longer be used. However,
    if the egg does not break, it may be reused in future moves.

    Return the minimum number of moves that are needed to determine with
    certainty what the value of f is.
    '''
    # based on solution by ye15
    # https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/solutions/1247673/python3-egg-dropping-problem/
    def twoEggDrop(self, n: int) -> int:
        @cache
        def dp(n,k):
            # have to try all the floors (one egg)
            if k == 1: return n
            # no more floors
            if n == 0: return 0
            ans = 10**7+1
            for i in range(1,n+1):
                # egg broke on this floor
                a = dp(i-1,k-1)
                # egg did not break on this floor
                b = dp(n-i, k)
                ans = min(ans, 1 + max(a,b))
            return ans
        return dp(n, 2)
    
    # based on 42ms code sample
    # slick math...
    def twoEggDrop(self, n: int) -> int:
        one, two = 1, 1
        while two < n:
            two += one + 1
            one += 1
        return one

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        o = 2
        self.assertEqual(s.twoEggDrop(i), o)

    def test_two(self):
        s = Solution()
        i = 100
        o = 14
        self.assertEqual(s.twoEggDrop(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)