# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting of lowercase English letters.

    A substring of s is called balanced if all distinct characters in the
    substring appear the same number of times.

    Return the length of the longest balanced substring of s.
    '''
    # brute force
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        answer = 0
        for i in range(n):
            c = Counter()
            for j in range(i,n):
                c[s[j]] += 1
                if all(c[s[j]] == c[k] for k in c):
                    answer = max(answer, j-i+1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abbac"
        o = 4
        self.assertEqual(s.longestBalanced(i), o)

    def test_two(self):
        s = Solution()
        i = "zzabccy"
        o = 4
        self.assertEqual(s.longestBalanced(i), o)

    def test_three(self):
        s = Solution()
        i = "aba"
        o = 2
        self.assertEqual(s.longestBalanced(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)