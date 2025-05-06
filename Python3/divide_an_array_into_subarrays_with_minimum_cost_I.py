# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums of length n.

    The cost of an array is the value of its first element.

    Divide nums into 3 disjoint contiguous subarrays.

    Return the minimum possible sum of the cost of these subarrays.
    '''
    # fails, does not account for order
    def minimumCost_fails(self, nums: List[int]) -> int:
        return sum(sorted(nums)[:3])

    def minimumCost(self, nums: List[int]) -> int:
        return nums[0] + sum(sorted(nums[1:])[:2])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,12]
        o = 6
        self.assertEqual(s.minimumCost(i), o)

    def test_two(self):
        s = Solution()
        i = [5,4,3]
        o = 12
        self.assertEqual(s.minimumCost(i), o)

    def test_three(self):
        s = Solution()
        i = [10,3,1,1]
        o = 12
        self.assertEqual(s.minimumCost(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)