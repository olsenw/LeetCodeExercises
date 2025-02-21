# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of integers nums and an integer k, an element nums[i] is
    considered good if it is strictly greater than the elements at indices i - k
    and i + k (if those indices exist). If neither of those indices exists,
    nums[i] is still considered good.

    Return the sum of all the good elements in the array.
    '''
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        return sum(nums[i] for i in range(len(nums)) if (i - k < 0 or nums[i-k] < nums[i]) and (i + k >= len(nums) or nums[i] > nums[i+k]))

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2,1,5,4], 2
        o = 12
        self.assertEqual(s.sumOfGoodNumbers(*i), o)

    def test_two(self):
        s = Solution()
        i = [2,1], 1
        o = 2
        self.assertEqual(s.sumOfGoodNumbers(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)