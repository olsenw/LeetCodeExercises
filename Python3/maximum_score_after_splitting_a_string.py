# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s of zeros and ones, return the maximum score after splitting
    the string into two non-empty substrings (ie left substring and right
    substring).

    The score after splitting a string is the number of zeros in the left
    substring plus the number of ones in the right substring.
    '''
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = 0
        score = 0
        for c in s[:-1]:
            if c == '1':
                ones -= 1
            else:
                zeros += 1
            score = max(score, zeros + ones)
        return score

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "011101"
        o = 5
        self.assertEqual(s.maxScore(i), o)

    def test_two(self):
        s = Solution()
        i = "00111"
        o = 5
        self.assertEqual(s.maxScore(i), o)

    def test_three(self):
        s = Solution()
        i = "1111"
        o = 3
        self.assertEqual(s.maxScore(i), o)

    def test_four(self):
        s = Solution()
        i = "0000"
        o = 3
        self.assertEqual(s.maxScore(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)