# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, calculate its reverse degree.

    The reverse degree is calculated as follows:
    1) For each character, multiply its position in the reversed alphabet
       ('a'=26, 'b'=25, ..., 'z'=1) with its position in the string (1-indexed).
    2) Sum these products for all characters in the string.

    Return the reverse degree of s.
    '''
    m = {i:j for i,j in zip("abcdefghijklmnopqrstuvwxyz", range(26,0,-1))}
    def reverseDegree(self, s: str) -> int:
        # answer = 0
        # for i in range(len(s)):
        #     answer += (i+1) * self.m[s[i]]
        #     pass
        # return answer
        return sum((i+1) * self.m[s[i]] for i in range(len(s)))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "abc"
        o = 148
        self.assertEqual(s.reverseDegree(i), o)

    def test_two(self):
        s = Solution()
        i = "zaza"
        o = 160
        self.assertEqual(s.reverseDegree(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)