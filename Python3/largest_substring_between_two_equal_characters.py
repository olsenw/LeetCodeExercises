# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, return the length of the longest substring between two
    equal characters, excluding the two characters. If there is no such
    substring return -1.

    A substring is a contiguous sequence of characters within a string.
    '''
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        h = dict()
        for i,j in enumerate(s):
            if j in h:
                h[j][1] = i
            else:
                h[j] = [i,i]
        answer = -1
        for i in h:
            x,y = h[i]
            answer = max(answer, y - x - 1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aa"
        o = 0
        self.assertEqual(s.maxLengthBetweenEqualCharacters(i), o)

    def test_two(self):
        s = Solution()
        i = "abca"
        o = 2
        self.assertEqual(s.maxLengthBetweenEqualCharacters(i), o)

    def test_three(self):
        s = Solution()
        i = "cbzxy"
        o = -1
        self.assertEqual(s.maxLengthBetweenEqualCharacters(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)