# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given 3 positive numbers a, b and c. Return the minimum flips required in
    some bits of a and b to make (a OR b == c). (bitwise OR operation). Flip
    operation consists of change any single bit 1 to 0 or change the 0 to 1 in
    their binary representation.
    '''
    def minFlips(self, a: int, b: int, c: int) -> int:
        answer = 0
        while a > 0 or b > 0 or c > 0:
            bit = c & 1
            # bit is one
            if bit:
                if not a & 1 and not b & 1:
                    answer += 1
            # bit is zero
            else:
                if a & 1:
                    answer += 1
                if b & 1:
                    answer += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 2
        j = 6
        k = 5
        o = 3
        self.assertEqual(s.minFlips(i,j,k), o)

    def test_two(self):
        s = Solution()
        i = 4
        j = 2
        k = 7
        o = 1
        self.assertEqual(s.minFlips(i,j,k), o)

    def test_three(self):
        s = Solution()
        i = 1
        j = 2
        k = 3
        o = 0
        self.assertEqual(s.minFlips(i,j,k), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)