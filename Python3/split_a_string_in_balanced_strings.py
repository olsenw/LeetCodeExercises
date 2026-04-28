# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Balanced strings are those that have equal quantity of 'L' and 'R'
    characters.

    Given a balanced string s, split it into some number of substrings such
    that:
    * Each substring is balanced.

    Return the maximum number of balanced strings that can be obtained.
    '''
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        answer = 0
        for c in s:
            if c == 'R':
                r += 1
            else:
                r -= 1
            if r == 0:
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "RLRRLLRLRL"
        o = 4
        self.assertEqual(s.balancedStringSplit(i), o)

    def test_two(self):
        s = Solution()
        i = "RLRRRLLRLL"
        o = 2
        self.assertEqual(s.balancedStringSplit(i), o)

    def test_three(self):
        s = Solution()
        i = "LLLLRRRR"
        o = 1
        self.assertEqual(s.balancedStringSplit(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)