# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s that consists of lowercase English letter.

    A string is called special if it is made up of only a single character.

    Return the length of the longest special substring of s which occurs at
    least thrice, or -1 if no special substring occurs at least thrice.

    A substring is a contiguous non-empty subsequence of characters within a
    string.
    '''
    # assumes no overlap of substrings allowed
    def maximumLength_fails(self, s: str) -> int:
        answer = 0
        last = "|"
        for i in range(len(s)):
            if s[i] != last[-1]:
                last = ""
            last += s[i]
            j = s.find(last, i+1)
            if j > 0:
                k = s.find(last, j + len(last))
                if k > 0:
                    answer = max(answer, len(last))
        return answer if answer else -1

    def maximumLength(self, s: str) -> int:
        answer = 0
        start = -1
        last = "|"
        for i in range(len(s)):
            if s[i] != last[-1]:
                last = ""
                start = i
            last += s[i]
            j = s.find(last, start+1)
            if j > 0:
                k = s.find(last, j+1)
                if k > 0:
                    answer = max(answer, len(last))
        return answer if answer else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aaaa"
        o = 2
        self.assertEqual(s.maximumLength(i), o)

    def test_two(self):
        s = Solution()
        i = "abcdef"
        o = -1
        self.assertEqual(s.maximumLength(i), o)

    def test_three(self):
        s = Solution()
        i = "abcaba"
        o = 1
        self.assertEqual(s.maximumLength(i), o)

    def test_four(self):
        s = Solution()
        i = "abcccccdddd"
        o = 3
        self.assertEqual(s.maximumLength(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)