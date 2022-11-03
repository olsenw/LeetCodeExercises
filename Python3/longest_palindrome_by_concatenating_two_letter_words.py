# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List

class Solution:
    '''
    Given an array of strings words. Each element of words consists of two
    lowercase English letters.

    Create the longest possible palindrome by selecting some elements from words
    and concatenating them in any order. Each element can be selected at most
    once.

    Return the length of the longest palindrome that can be created. If it is
    impossible to create any palindrome, return 0.

    A palindrome is a string that read the same forward and backward.
    '''
    def longestPalindrome(self, words: List[str]) -> int:
        a = 0
        middle = False
        c = Counter(words)
        for w in c:
            if w == w[::-1]:
                a += c[w] // 2
            elif w[::-1] in c:
                a += min(c[w], c[w[::-1]])
                c[w] = 0
            if w == w[::-1] and c[w] % 2:
                middle = True
        return 4 * a + 2 if middle else 4 * a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = ["lc","cl","gg"]
        o = 6
        self.assertEqual(s.longestPalindrome(i), o)

    def test_two(self):
        s = Solution()
        i = ["ab","ty","yt","lc","cl","ab"]
        o = 8
        self.assertEqual(s.longestPalindrome(i), o)

    def test_three(self):
        s = Solution()
        i = ["cc","ll","xx"]
        o = 2
        self.assertEqual(s.longestPalindrome(i), o)

    def test_four(self):
        s = Solution()
        i = ["cc","cc","cc","ab","ba"]
        o = 10
        self.assertEqual(s.longestPalindrome(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)