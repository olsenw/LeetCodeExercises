# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a positive number n.

    Return the smallest number x greater than or equal to n, such that the
    binary representation of x contains only set bits.
    '''
    def smallestNumber(self, n: int) -> int:
        answer = 1
        while n > answer:
            answer <<= 1
            answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = 5
        o = 7
        self.assertEqual(s.smallestNumber(i), o)

    def test_two(self):
        s = Solution()
        i = 10
        o = 15
        self.assertEqual(s.smallestNumber(i), o)

    def test_three(self):
        s = Solution()
        i = 3
        o = 3
        self.assertEqual(s.smallestNumber(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)