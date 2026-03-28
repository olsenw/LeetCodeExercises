# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    The LCP matrix of any 0-indexed string word of n lowercase English letters
    as an n x n grid such that:
    * lcp[i][j] is equal to the length of the longest common prefix between the
      substrings word[i,n-1] and word[j,n-1].
    
    Given an n x n matrix lcp, return the alphabetically smallest string word
    that corresponds to lcp. If there is no such string, return an empty string.

    A string a is lexicographically smaller than a string b (of the same length)
    if in the first position where a and b differ, string a has a letter that
    appears earlier in the alphabet than the corresponding letter in b.
    '''
    # based on editorial
    # https://leetcode.com/problems/find-the-string-with-lcp/editorial/?envType=daily-question&envId=2026-03-28
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        current = ord("a")
        # construct the string starting from 'a' to 'z' sequentially
        for i in range(n):
            if not word[i]:
                if current > ord('z'):
                    return ""
                word[i] = chr(current)
                for j in range(i+1, n):
                    if lcp[i][j]:
                        word[j] = word[i]
                current += 1
        # verify if constructed string meets the LCP matrix requirements
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j]:
                        return ""
                else:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i+1][j+1] + 1:
                            return ""
        return "".join(word)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
        o = "abab"
        self.assertEqual(s.findTheString(i), o)

    def test_two(self):
        s = Solution()
        i = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
        o = "aaaa"
        self.assertEqual(s.findTheString(i), o)

    def test_three(self):
        s = Solution()
        i = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
        o = ""
        self.assertEqual(s.findTheString(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)