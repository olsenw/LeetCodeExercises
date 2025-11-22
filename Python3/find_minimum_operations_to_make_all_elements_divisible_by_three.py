# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. In one operation it is possible to add or
    subtract 1 from any element of nums.

    Return the minimum number of operations to make all elements of nums
    divisible by 3.
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        # nums 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        # cost 1 1 0 1 1 0 1 1 0  1  1  0  1  1  0
        return sum(n % 3 > 0 for n in nums)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = 3
        self.assertEqual(s.minimumOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [3,6,9]
        o = 0
        self.assertEqual(s.minimumOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)