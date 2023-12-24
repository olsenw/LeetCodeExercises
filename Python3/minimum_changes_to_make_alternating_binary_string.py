# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a string s consisting only of the characters '0' and '1'. In one
    operation, change any '0' to '1' or vice versa.

    The string is called alternating if no two adjacent characters are equal.

    Return the minimum number of operations needed to make s alternating.
    '''
    # very slow... should turn this into a loop
    def minOperations(self, s: str) -> int:
        def flip0(i: int) -> int:
            if i == len(s):
                return 0
            if s[i] == '0':
                return 1 + flip1(i+1)
            else:
                return flip1(i+1)
        def flip1(i: int) -> int:
            if i == len(s):
                return 0
            if s[i] == '1':
                return 1 + flip0(i+1)
            else:
                return flip0(i+1)
        return min(flip0(0), flip1(0))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "0100"
        o = 1
        self.assertEqual(s.minOperations(i), o)

    def test_two(self):
        s = Solution()
        i = "10"
        o = 0
        self.assertEqual(s.minOperations(i), o)

    def test_three(self):
        s = Solution()
        i = "1111"
        o = 2
        self.assertEqual(s.minOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)