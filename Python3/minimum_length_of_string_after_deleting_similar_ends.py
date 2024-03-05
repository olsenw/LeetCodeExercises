# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting only of characters 'a', 'b', and 'c'. Apply the
    following algorithm on the string any number of times:
    1) Pick a non-empty prefix from the string s where all the characters in the
       prefix are equal.
    2) Pick a non-empty suffix from the string s where all the characters in the
       suffix are equal.
    3) The prefix and the suffix should not intersect at any index.
    4) The characters from the prefix and suffix must be the same.
    5) Delete both the prefix and the suffix.

    Return the minimum length of s after performing the above operation any
    number of times (possibly zero times).
    '''
    def minimumLength(self, s: str) -> int:
        i,j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            pass
            while i < j and s[i] == s[j]:
                i += 1
            while i <= j and s[i-1] == s[j]:
                j -= 1
        return j - i + 1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ca"
        o = 2
        self.assertEqual(s.minimumLength(i), o)

    def test_two(self):
        s = Solution()
        i = "cabaabac"
        o = 0
        self.assertEqual(s.minimumLength(i), o)

    def test_three(self):
        s = Solution()
        i = "aabccabba"
        o = 3
        self.assertEqual(s.minimumLength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)