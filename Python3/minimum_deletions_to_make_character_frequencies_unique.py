# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

from collections import Counter

class Solution:
    '''
    A string s is called good if there are no two different characters
    in s that have the same frequency.

    Given a string s, return the minimum number of characters that have
    to be deleted to make s good.

    The frequency of a character in a string is the number of times it
    appears in the string.
    '''
    def minDeletions(self, s: str) -> int:
        a = 0
        c = sorted(Counter(s).values(), reverse=True)
        for i in range(1, len(c)):
            while c[i] and c[i] >= c[i - 1]:
                a += 1
                c[i] -= 1
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aab"
        o = 0
        self.assertEqual(s.minDeletions(i), o)

    def test_two(self):
        s = Solution()
        i = "aaabbbcc"
        o = 2
        self.assertEqual(s.minDeletions(i), o)

    def test_three(self):
        s = Solution()
        i = "ceabaacb"
        o = 2
        self.assertEqual(s.minDeletions(i), o)

    def test_four(self):
        s = Solution()
        i = "abcabc"
        o = 3
        self.assertEqual(s.minDeletions(i), o)

    def test_five(self):
        s = Solution()
        i = "bbcebab"
        o = 2
        self.assertEqual(s.minDeletions(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)