# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    The power of the string is the maximum length of a non-empty
    substring that contains only one unique character.

    Given a string s return the power of s.
    '''
    def maxPower(self, s: str) -> int:
        longest = 0
        current = 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                longest = max(longest, current)
                current = 0
            current += 1
        return max(longest, current)

class UnitTesting(unittest.TestCase):
    # actual test to run on Solution
    def test_one(self):
        s = Solution()
        self.assertEqual(s.maxPower("leetcode"), 2)
    def test_two(self):
        s = Solution()
        self.assertEqual(s.maxPower("abbcccddddeeeeedcba"), 5)
    def test_three(self):
        s = Solution()
        self.assertEqual(s.maxPower("triplepillooooow"), 5)
    def test_four(self):
        s = Solution()
        self.assertEqual(s.maxPower("hooraaaaaaaaaaay"), 11)
    def test_four(self):
        s = Solution()
        self.assertEqual(s.maxPower("tourist"), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)