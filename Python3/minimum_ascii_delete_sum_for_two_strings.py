# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings s1 and s2, return the lowest ASCII sum of deleted
    characters to make two strings equal.
    '''
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n = len(s1), len(s2)
        # i is s[i:] and j is s[j:]
        @cache
        def dp(i,j):
            if i < 0 and j < 0:
                return 0
            if i < 0:
                return ord(s2[j]) + dp(i, j-1)
            if j < 0:
                return ord(s1[i]) + dp(i-1,j)
            if s1[i] == s2[j]:
                return dp(i-1, j-1)
            else:
                return min(
                    ord(s1[i]) + dp(i-1,j),
                    ord(s2[j]) + dp(i, j-1)
                    )
        return dp(m-1,n-1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "sea"
        j = "eat"
        o = 231
        self.assertEqual(s.minimumDeleteSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = "delete"
        j = "leet"
        o = 403
        self.assertEqual(s.minimumDeleteSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)