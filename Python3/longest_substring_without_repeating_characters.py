# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given a string s, find the length of the longest substring without
    repeating characters.
    '''
    # real slow... but it passes
    def lengthOfLongestSubstring_rebuild_window(self, s: str) -> int:
        i, w, c = 0, 0, {}
        while i < len(s):
            if s[i] in c:
                w = max(w, len(c))
                i = c[s[i]] + 1
                c = {}
            c[s[i]] = i
            i += 1
        return max(w, len(c))

    # based on leetcode optimized sliding window solution
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
    # O(n) time
    # O(min(m, n)) space where m is unique letters and n is length of s
    # could be changed to m using array if possible letters constrained
    def lengthOfLongestSubstring(self, s: str) -> int:
        # i is start index
        # j is ending index
        # w is largest window size
        # c is a mapping of character -> to last known index
        i, w, c = 0, 0, {}
        for j in range(len(s)):
            # seen this letter before
            if s[j] in c:
                # if starting index is past last know position skip
                i = max(i, c[s[j]])
            # best window so far
            w = max(w, j - i + 1)
            # by adding plus one marks new starting index on duplicate
            c[s[j]] = j + 1
        return w

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abcabcbb"
        o = 3
        self.assertEqual(s.lengthOfLongestSubstring(i), o)

    def test_two(self):
        s = Solution()
        i = "bbbbb"
        o = 1
        self.assertEqual(s.lengthOfLongestSubstring(i), o)

    def test_three(self):
        s = Solution()
        i = "pwwkew"
        o = 3
        self.assertEqual(s.lengthOfLongestSubstring(i), o)

    def test_four(self):
        s = Solution()
        i = "dvdf"
        o = 3
        self.assertEqual(s.lengthOfLongestSubstring(i), o)

    def test_five(self):
        s = Solution()
        i = "loddktdji"
        o = 5
        self.assertEqual(s.lengthOfLongestSubstring(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)