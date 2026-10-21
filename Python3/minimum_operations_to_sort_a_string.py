# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters.

    In one operation, it is possible to select any substring of s that is not
    the entire string and sort it in non-decreasing alphabetical order.

    Return the minimum number of operations required to make s sorted in
    non-deceasing order. If it is not possible, return -1.
    '''
    def minOperations_fails(self, s: str) -> int:
        # if len(s) == 1 or s == "".join(sorted(s)):
        if s == "".join(sorted(s)):
            return 0
        mn = min(s)
        mx = max(s)
        # if len(s) == 2 and s[0] == mx and s[1] == mn:
        if len(s) == 2:
            return -1
        if s[0] == mn or s[-1] == mx:
            return 1
        if len(s) == 3 and s[0] == mx and s[-1] == mn and s[1] != mx and s[1] != mn:
            return 3
        return 2

    # based on Leetcode editorial
    # https://leetcode.com/problems/minimum-operations-to-sort-a-string/editorial/?envType=daily-question&envId=2026-10-21
    def minOperations(self, s: str) -> int:
        # case 1 already sorted
        if s == "".join(sorted(s)):
            return 0
        # case 2 length 2 and not sorted
        if len(s) == 2:
            return -1
        # case 3 first or last character is smallest/largest
        mx = max(s)
        mn = min(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        # case 4 first is largest and last is smallest (no duplicates of smallest and largest character)
        mxc = s.count(mx)
        mnc = s.count(mn)
        if s[0] == mx and s[-1] == mn and mxc == 1 == mnc:
            return 3
        # all other cases take two sorts
        return 2

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "dog"
        o = 1
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = "card"
        o = 2
        self.assertEqual(s.minOperations(i), o)

    def test_three(self):
        s = Solution()
        i = "gf"
        o = -1
        self.assertEqual(s.minOperations(i), o)

    def test_four(self):
        s = Solution()
        i = "edc"
        o = 3
        self.assertEqual(s.minOperations(i), o)

    def test_five(self):
        s = Solution()
        i = "jgg"
        o = 2
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)