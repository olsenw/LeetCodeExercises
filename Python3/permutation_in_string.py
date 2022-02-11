# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two strings s1 and s2, return true if s2 contains a 
    permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the
    substring of s2.
    '''
    # could improve by fast forwarding window to next possible position
    # when fail character detected instead of sliding over whole string
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        c = Counter(s1)
        n = len(s1)
        # sliding window of size len(s1)
        t = Counter(s2[:n])
        for i in range(n, len(s2)):
            if t == c:
                return True
            t[s2[i-n]] -= 1
            t[s2[i]] += 1
        return t == c

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ab"
        j = "eidbaooo"
        o = True
        self.assertEqual(s.checkInclusion(i, j), o)

    def test_two(self):
        s = Solution()
        i = "ab"
        j = "eidboaoo"
        o = False
        self.assertEqual(s.checkInclusion(i, j), o)

    def test_three(self):
        s = Solution()
        i = "adc"
        j = "dcda"
        o = True
        self.assertEqual(s.checkInclusion(i, j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)