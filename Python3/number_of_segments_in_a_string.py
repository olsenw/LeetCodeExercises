# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s, return the number of segments in the string.

    A segment is defined to be a contiguous sequence of non-space characters.
    '''
    # build in solution
    def countSegments(self, s: str) -> int:
        return len(s.split())

    def countSegments(self, s: str) -> int:
        answer = 0
        last = ' '
        for c in s:
            if c == ' ' and last != ' ':
                answer += 1
            last = c
        return answer + (last != ' ')

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "Hello, my name is John"
        o = 5
        self.assertEqual(s.countSegments(i), o)

    def test_two(self):
        s = Solution()
        i = "Hello"
        o = 1
        self.assertEqual(s.countSegments(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)