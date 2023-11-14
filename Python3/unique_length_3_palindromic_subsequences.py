# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given s string s, return the number of unique palindromes of length three
    that are a subsequence of s.

    Note that even if there are multiple ways to obtain the same subsequence, it
    is still only counted once.

    A palindrome is a string that reads the same forwards and backwards.

    A subsequence of a string is a new string generated from the original string
    with some characters (can be none) deleted without changing the relative
    order of the remaining characters.
    '''
    def countPalindromicSubsequence(self, s: str) -> int:
        answer = set()
        f = Counter(s[1:])
        b = Counter(s[0])
        for c in s[1:]:
            pass
            f[c] -= 1
            for a in b:
                if f[a] > 0:
                    answer.add(f'{a}{c}{a}')
            b[c] += 1
        return len(answer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aabca"
        o = 3
        self.assertEqual(s.countPalindromicSubsequence(i), o)

    def test_two(self):
        s = Solution()
        i = "adc"
        o = 0
        self.assertEqual(s.countPalindromicSubsequence(i), o)

    def test_two(self):
        s = Solution()
        i = "bbcbaba"
        o = 4
        self.assertEqual(s.countPalindromicSubsequence(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)