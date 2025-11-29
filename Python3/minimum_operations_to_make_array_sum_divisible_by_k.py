# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums an integer k. Perform the following operation
    any number of times:
    * Select an index i and replace nums[i] with num[i] - 1

    Return the minimum number of operations required to make the sum of the
    array divisible by k.
    '''
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,9,7]
        j = 5
        o = 4
        self.assertEqual(s.minOperations(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,1,3]
        j = 4
        o = 0
        self.assertEqual(s.minOperations(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3,2]
        j = 6
        o = 5
        self.assertEqual(s.minOperations(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)