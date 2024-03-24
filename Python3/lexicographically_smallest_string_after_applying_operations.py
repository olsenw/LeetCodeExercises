# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import deque
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s of even length consisting of digits from 0 to 9, and two
    integers a and b.

    It is possible to apply either of the following operations any number of
    times and in any order on s:
    * Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back
      to 0.
    * Rotate s to the right by b positions.

    Return the lexicographically smallest string that can be obtained by
    applying the above operations any number of times on s.

    A string a is lexicographically smaller than a string b (of the same length)
    if in the first position where a and b differ, string a has a letter that
    appears earlier in the alphabet than the corresponding letter in b.
    '''
    # help from Spaulding_ on how to do dfs search (instead of BFS hint suggests)
    # https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/solutions/3436071/python-3-12-lines-recursion-dfs-t-m-80-12/
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # map the character to another character after adding a
        m = {i:str((int(i)+a) % 10) for i in "0123456789"}
        # states already seen
        sequence = set()
        # explore the search space
        def dfs(s):
            # already explored, bail
            if s in sequence:
                return
            # prevent looking at the same thing
            sequence.add(s)
            # search odd edited string
            dfs(''.join(m[j] if i % 2 else j for i,j in enumerate(s)))
            # search rotated string
            dfs(s[b:]+s[:b])
        # explore search space
        dfs(s)
        # find the smallest string in the search space
        return min(sequence)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "5525", 9, 2
        o = "2050"
        self.assertEqual(s.findLexSmallestString(*i), o)

    def test_two(self):
        s = Solution()
        i = "74",5,1
        o = "24"
        self.assertEqual(s.findLexSmallestString(*i), o)

    def test_three(self):
        s = Solution()
        i = "0011",4,2
        o = "0011"
        self.assertEqual(s.findLexSmallestString(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)