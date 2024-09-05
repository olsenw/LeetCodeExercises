# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a non-negative integer array nums. In operation:
    * Choose a positive integer x such that x is less than or equal to the
      smallest non-zero element in nums.
    * Subtract x from every positive element in nums.

    Return the minimum number of operations to make every element nums equal to
    0.
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        s = set(nums)
        return len(s) - (0 in s)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,5,0,3,5]
        o = 3
        self.assertEqual(s.minimumOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [0]
        o = 0
        self.assertEqual(s.minimumOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)