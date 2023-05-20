# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a license key represented as a string s that consists of only
    alphanumeric characters and dashes. The string is separated into n+1 groups
    by n dashes. Also given an integer k.

    Reformat the string s such that each group contains exactly k characters,
    except for the first group, which could be shorter than k but still must
    contain at least one character. Furthermore, there must be a dash inserted
    between two groups, and all lowercase letters should be converted to
    uppercase.

    Return the reformatted license key.
    '''
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        answer = []
        dash = 0
        for c in s[::-1]:
            if c == '-':
                continue
            if dash == k:
                dash = 0
                answer.append('-')
            answer.append(c.upper())
            dash += 1
        return ''.join(answer[::-1])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "5F3Z-2e-9-w"
        j = 4
        o = "5F3Z-2E9W"
        self.assertEqual(s.licenseKeyFormatting(i,j), o)

    def test_two(self):
        s = Solution()
        i = "2-5g-3-J"
        j = 2
        o = "2-5G-3J"
        self.assertEqual(s.licenseKeyFormatting(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)