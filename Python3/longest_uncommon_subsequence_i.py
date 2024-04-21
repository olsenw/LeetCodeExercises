# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two strings a and b, return the length of the longest uncommon
    subsequence between a and b. If no such uncommon subsequence exists, return
    -1.

    A uncommon subsequence between two strings is a string that is a subsequence
    of exactly one of them.
    '''
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1
        # if len(a) != len(b):
        #     return max(len(a), len(b))
        # if a == b:
        #     return -1
        # answer = 0
        # for i in range(len(a)):
        #     for j in range(i, len(a)):
        #         if a[i:j+1] not in b:
        #             answer = max(answer, j - i + 1)
        # return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aba"
        j = "cdc"
        o = 3
        self.assertEqual(s.findLUSlength(i,j), o)

    def test_two(self):
        s = Solution()
        i = "aaa"
        j = "aaa"
        o = -1
        self.assertEqual(s.findLUSlength(i,j), o)

    def test_three(self):
        s = Solution()
        i = "aaa"
        j = "bbb"
        o = 3
        self.assertEqual(s.findLUSlength(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)