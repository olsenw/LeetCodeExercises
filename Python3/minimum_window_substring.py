# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given two strings s and t of lengths m and n respectively, return the
    minimum window substring of s such that every character in t (including
    duplicates) is included in the window. If there is no such substring, return
    the empty string "".

    The testcases are generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.
    '''
    # O(n^2) time
    def minWindow_Brute(self, s: str, t: str) -> str:
        tc = Counter(t)
        a = ""
        for i in range(len(s)):
            c = Counter()
            for j in range(i, len(s)):
                c[s[j]] += 1
                if all(tc[k] <= c[k] for k in tc) and (a == "" or len(a) > j - i):
                    a = s[i:j+1]
        return a

    # O(n^2) time
    def minWindow_Brute_Alt(self, s: str, t: str) -> str:
        tc = Counter(t)
        a = ""
        for i in range(len(s)):
            c = Counter(tc)
            for j in range(i, len(s)):
                if c[s[j]]:
                    c[s[j]] -= 1
                    if not any(c.values()):
                        if not a or len(a) > j - i:
                            a = s[i:j+1]
                        break
        return a

    # based on Leetcode hints
    # (m * n) time ??? (check takes n time) (iterate through m characters)
    def minWindow_slow(self, s: str, t: str) -> str:
        def check(c):
            return sum(max(v,0) for v in c.values()) == 0
        window = Counter(t)
        i, j = 0, 0
        # hint 2 (move right pointer until all values covered)
        while not check(window) and j < len(s):
            if s[j] in window:
                window[s[j]] -= 1
            j += 1
        if not check(window):
            return ""
        j -= 1
        # hint 3 (move left pointer while all values covered)
        while i <= j and check(window):
            if s[i] in window:
                if window[s[i]] == 0:
                    break
                window[s[i]] += 1
            i += 1
        # hint 4 (move window to right shrink when can)
        a,b = i,j
        while j < len(s)-1:
            j += 1
            if s[j] in window:
                window[s[j]] -= 1
            # hint 3 (move left pointer while all values covered)
            while i <= j and check(window):
                if s[i] in window:
                    if window[s[i]] == 0:
                        break
                    window[s[i]] += 1
                i += 1
            if j - i < b - a:
                a,b = i,j
        return s[a:b+1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "ADOBECODEBANC"
        j = "ABC"
        o = "BANC"
        self.assertEqual(s.minWindow(i,j), o)

    def test_two(self):
        s = Solution()
        i = "a"
        j = "a"
        o = "a"
        self.assertEqual(s.minWindow(i,j), o)

    def test_three(self):
        s = Solution()
        i = "a"
        j = "aa"
        o = ""
        self.assertEqual(s.minWindow(i,j), o)

    def test_four(self):
        s = Solution()
        i = "ab"
        j = "a"
        o = "a"
        self.assertEqual(s.minWindow(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)