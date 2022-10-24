# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of strings arr. A string s is formed by the concatenation of
    a subsequence of arr that has unique characters.

    Return the maximum possible length of s.

    A subsequence is an array that can be derived from another array by deleting
    some or no elements without changing the order of the remaining elements.
    '''
    # the answer is in the range [1, 26]
    def maxLength(self, arr: List[str]):
        def toBitSet(s) -> int:
            b, l = 0, 0
            for c in s:
                a = 1 << (ord(c) - ord('a'))
                if b & a:
                    return 0,0
                b |= a
                l += 1
            return b,l
        a = [toBitSet(s) for s in arr]
        @cache
        def dp(i,b) -> int:
            if i == len(a):
                return 0
            # do not take or cannot take
            if a[i][0] == 0 or b & a[i][0]:
                return dp(i+1, b)
            # possible to take
            else:
                return max(dp(i+1, b), a[i][1] + dp(i+1, b | a[i][0]))
        return dp(0,0)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["un","iq","ue"]
        o = 4
        self.assertEqual(s.maxLength(i), o)

    def test_two(self):
        s = Solution()
        i = ["cha","r","act","ers"]
        o = 6
        self.assertEqual(s.maxLength(i), o)

    def test_three(self):
        s = Solution()
        i = ["abcdefghijklmnopqrstuvwxyz"]
        o = 26
        self.assertEqual(s.maxLength(i), o)

    def test_four(self):
        s = Solution()
        i = ["unu","iq","ue"]
        o = 4
        self.assertEqual(s.maxLength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)