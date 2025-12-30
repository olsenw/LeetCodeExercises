# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums, and an integer k.

    In one operation, it is possible to remove one occurrence of the smallest
    element of nums.

    Return the minimum number of operations needed so that all elements of the
    array are greater than or equal to k.
    '''
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(n < k for n in nums)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,11,10,1,3]
        j = 10
        o = 3
        self.assertEqual(s.minOperations(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,2,4,9]
        j = 1
        o = 0
        self.assertEqual(s.minOperations(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,1,2,4,9]
        j = 9
        o = 4
        self.assertEqual(s.minOperations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)