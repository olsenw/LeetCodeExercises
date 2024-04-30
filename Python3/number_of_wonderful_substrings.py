# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import Counter, List, Dict, Set, Optional

class Solution:
    '''
    A wonderful string is a string where at most one letters appears an odd
    number of times.

    Given a string word that consists of the first ten lowercase English letters
    ('a' through 'j'), return the number of wonderful non-empty substrings in
    word. If the same substring appears multiple times in word, then count each
    occurrence separately.

    A substring is a contiguous sequence of characters in a string.
    '''
    # based on Leetcode editorial
    # https://leetcode.com/problems/number-of-wonderful-substrings/editorial/?envType=daily-question&envId=2024-04-30
    # hints given away the bit mask idea
    # needed editorial for how to do the counting
    def wonderfulSubstrings(self, word: str) -> int:
        answer = 0
        c = Counter([0])
        p = 0
        for i in word:
            p ^= 1 << (ord(i) - 97)
            answer += c[p]
            c[p] += 1
            for j in range(10):
                answer += c[p ^ (1 << j)]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aba"
        o = 4
        self.assertEqual(s.wonderfulSubstrings(i), o)

    def test_two(self):
        s = Solution()
        i = "aabb"
        o = 9
        self.assertEqual(s.wonderfulSubstrings(i), o)

    def test_three(self):
        s = Solution()
        i = "he"
        o = 2
        self.assertEqual(s.wonderfulSubstrings(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)