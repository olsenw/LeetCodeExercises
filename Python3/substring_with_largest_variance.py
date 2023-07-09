# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The variance of a string is defined as the largest difference between the
    number of occurrences of any 2 character present in the string. Note the two
    characters may or may not be the same.

    Given a string s consisting of lowercase English letters only, return the
    largest variance possible among all substrings of s.

    A substring is a contiguous sequence of characters within a string.
    '''
    def largestVariance_brute(self, s: str) -> int:
        n = len(s)
        p = [[0] * 26]
        p[0][ord(s[0]) - ord('a')] = 1
        for i in range(1,n):
            p.append([i for i in p[-1]])
            p[i][ord(s[i]) - ord('a')] += 1
        v = 0
        for i in range(n):
            for j in range(i, n):
                s = [i for i in [p[j][k] - p[i][k] for k in range(26)] if i > 0]
                v = max(v, max(s) - min(s) if len(s) > 0 else 0)
        return v

    # modified Kadane's algorithm
    # based on leetcode editorial
    # https://leetcode.com/problems/substring-with-largest-variance/editorial/
    # Kadane is modified by calculating the answer of give pair of character
    # (zero) out any other character in that run, and only considering cases
    # where there is at least two different characters
    def largestVariance(self, s: str) -> int:
        c = Counter(s)
        global_max = 0
        # major
        for i in "abcdefghijklmnopqrstuvwxyz":
            # minor
            for j in "abcdefghijklmnopqrstuvwxyz":
                # major and minor cannot be the same and both characters must be
                # present in the string
                if i == j or c[i] == 0 or c[j] == 0:
                    continue
                # find the maximum variance of major - minor
                major_count = 0
                minor_count = 0
                # remaining minor count in s
                reset_minor = c[j]
                for k in s:
                    if k == i:
                        major_count += 1
                    if k == j:
                        minor_count += 1
                        reset_minor -= 1
                    # only update variance (local max) if there is at lest one
                    # minor
                    if minor_count > 0:
                        global_max = max(global_max, major_count - minor_count)
                    # can discard previous string if there is at lest one
                    # remaining minor
                    if major_count < minor_count and reset_minor > 0:
                        major_count = 0
                        minor_count = 0
        return global_max


class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aababbb"
        o = 3
        self.assertEqual(s.largestVariance(i), o)

    def test_two(self):
        s = Solution()
        i = "abcde"
        o = 0
        self.assertEqual(s.largestVariance(i), o)

    def test_three(self):
        s = Solution()
        i = "a" * (10**4)
        o = 0
        self.assertEqual(s.largestVariance(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)