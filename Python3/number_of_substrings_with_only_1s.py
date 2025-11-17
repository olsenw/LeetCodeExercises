# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a binary string s, return the number of substrings with all characters
    1's. Since the answer may be large, return it modulo 10^9 + 7.
    '''
    def numSub(self, s: str) -> int:
        m = 10**9 + 7
        answer = 0
        count = 0
        for c in s:
            if c == '1':
                count += 1
                answer = (answer + count) % m
            else:
                count = 0
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "0110111"
        o = 9
        self.assertEqual(s.numSub(i), o)

    def test_two(self):
        s = Solution()
        i = "101"
        o = 2
        self.assertEqual(s.numSub(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)