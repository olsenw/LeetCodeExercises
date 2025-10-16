# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums and an integer value.

    In one operation, it is possible to add or subtract value from any element
    of nums.

    the MEX (minimum excluded) of an array is the smallest missing non-negative
    integer in it.

    Return the maximum MEX of nums after applying the mentioned operation any
    number of times.
    '''
    # hints help a lot (points out the modular counting)
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        c = Counter(i % value for i in nums)
        i = 0
        while c[i % value] > 0:
            c[i % value] -= 1
            i += 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,-10,7,13,6,8]
        j = 5
        o = 4
        self.assertEqual(s.findSmallestInteger(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,-10,7,13,6,8]
        j = 7
        o = 2
        self.assertEqual(s.findSmallestInteger(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)