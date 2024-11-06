# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array of positive integers nums.

    In one operation, it is possible to swap any two adjacent elements if they
    have the same number of set bits. It is possible to do this operation any
    number of times (including zero).

    Return true if the array can be sorted, else return false.
    '''
    # hints help
    def canSortArray(self, nums: List[int]) -> bool:
        last = 0
        current = 0
        bits = 0
        for n in nums:
            b = n.bit_count()
            if bits != b:
                last = current
                bits = b
            if n <= last:
                return False
            current = max(current, n)
        return True

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [8,4,2,30,15]
        o = True
        self.assertEqual(s.canSortArray(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = True
        self.assertEqual(s.canSortArray(i), o)

    def test_three(self):
        s = Solution()
        i = [3,16,8,4,2]
        o = False
        self.assertEqual(s.canSortArray(i), o)

    def test_four(self):
        s = Solution()
        i = [20,16]
        o = False
        self.assertEqual(s.canSortArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)