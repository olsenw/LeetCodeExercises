# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer n and an integer start.

    Define an array nums where nums[i] = start + 2 * i (o-indexed) and
    n == nums.length.

    Return the bitwise XOR of all elements of nums.
    '''
    def xorOperation(self, n: int, start: int) -> int:
        answer = start
        for i in range(1, n):
            answer ^= start + 2 * i
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5, 0
        o = 8
        self.assertEqual(s.xorOperation(*i), o)

    def test_two(self):
        s = Solution()
        i = 4, 3
        o = 8
        self.assertEqual(s.xorOperation(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)