# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed binary string target of length n. Given another binary
    string of length n that is initially set to all zeros. Make s equal to
    target.

    In one operation, pick an index i where 0 <= i < n and flip all bits in the
    inclusive range [i, n-1]. Flip means changing '0' to '1' and '1' to '0'.

    Return the minimum number of operations needed to make s equal to target.
    '''
    def minFlips(self, target: str) -> int:
        answer = 0
        flip = "0"
        for i in target:
            if i != flip:
                flip = "1" if flip == "0" else "0"
                answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = "10111"
        o = 3
        self.assertEqual(s.minFlips(i), o)

    def test_two(self):
        s = Solution()
        i = "101"
        o = 3
        self.assertEqual(s.minFlips(i), o)

    def test_three(self):
        s = Solution()
        i = "00000"
        o = 0
        self.assertEqual(s.minFlips(i), o)

    def test_four(self):
        s = Solution()
        i = "11111111010010101011111111110000000000000000000000000000111010011111111111111111010101010100000000000000111010011111111111111100000000111001010101011010101010110111"
        o = 57
        self.assertEqual(s.minFlips(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)