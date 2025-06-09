# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given strings jewels representing the types of stones that are jewels, and
    stones representing the stones currently obtained. Each character in stones
    is a type of stone currently obtained. Find out how many of the stones are
    jewels.

    Letters are case sensitive, so 'a' is considered a different type of stone
    from 'A'.
    '''
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "aA"
        j = "aAAbbbb"
        o = 3
        self.assertEqual(s.numJewelsInStones(i,j), o)

    def test_two(self):
        s = Solution()
        i = "z"
        j = "ZZ"
        o = 0
        self.assertEqual(s.numJewelsInStones(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)