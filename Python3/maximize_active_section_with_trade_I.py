# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary string s of length n, where:
    * '1' represents an active section.
    * '0' represents an inactive section.

    It is possible to preform at most one trade to maximize the number of active
    sessions in s. In each :
    * Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
    * Afterward, convert a contiguous block of '0's that is surrounded by '1's
      to all '1's.
    
    Return the maximum number of active sections in s after making the optimal
    trade.

    Note: Treat s as if is augmented with a '1' at both ends, forming
    t = '1' + s + '1'. The augmented '1's do not contribute to the final count.
    '''
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        splits = []
        a = s[0]
        b = 0
        for c in s:
            if c == a:
                b += 1
            else:
                splits.append([a,b])
                a = c
                b = 1
        splits.append([a,b])
        best = 0
        for i in range(1,len(splits) - 1):
            if splits[i-1][0] == '0' and splits[i][0] == '1' and splits[i+1][0] == '0':
                best = max(best, splits[i-1][1] + splits[i+1][1])
        return ones + best

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "01"
        o = 1
        self.assertEqual(s.maxActiveSectionsAfterTrade(i), o)

    def test_two(self):
        s = Solution()
        i = "0100"
        o = 4
        self.assertEqual(s.maxActiveSectionsAfterTrade(i), o)

    def test_three(self):
        s = Solution()
        i = "1000100"
        o = 7
        self.assertEqual(s.maxActiveSectionsAfterTrade(i), o)

    def test_four(self):
        s = Solution()
        i = "01010"
        o = 4
        self.assertEqual(s.maxActiveSectionsAfterTrade(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)