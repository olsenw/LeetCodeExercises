# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary string s and a positive integer k.

    A substring of s is beautiful if the number of 1's in it is exactly k.

    Let len be the length of the shortest beautiful substring.

    Return the lexicographically smallest beautiful substring of string s with
    length equal to len. If s doesn't contain a beautiful substring, return an
    empty string.
    '''
    # brute force
    # very small solution space (len(s) <= 100)
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ""
        n = len(s)
        best = "1" * n
        for i in range(n):
            for j in range(i,n):
                b = s[i:j+1]
                if len(b) > len(best):
                    continue
                if b.count('1') == k:
                    if len(b) < len(best):
                        best = b
                    else:
                        best = min(best, b)
        return best

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "100011001"
        j = 3
        o = "11001"
        self.assertEqual(s.shortestBeautifulSubstring(i,j), o)

    def test_two(self):
        s = Solution()
        i = "1011"
        j = 2
        o = "11"
        self.assertEqual(s.shortestBeautifulSubstring(i,j), o)

    def test_three(self):
        s = Solution()
        i = "000"
        j = 1
        o = ""
        self.assertEqual(s.shortestBeautifulSubstring(i,j), o)

    def test_four(self):
        s = Solution()
        i = "1100100101011001001"
        j = 7
        o = "1100100101011"
        self.assertEqual(s.shortestBeautifulSubstring(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)