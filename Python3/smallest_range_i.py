# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k.

    In one operation, choose any index i where 0 <= i < nums.length and change
    nums[i] to nums[i] + x where x is an integer from the range [-k, k]. This 
    operation can be applied at most once for each index i.

    The score of nums is the difference between the maximum and minimum elements
    in nums.

    Return the minimum score of nums after applying the mentioned operation at
    most once for each index in it.
    '''
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        a, b = min(nums), max(nums)
        if a + k >= b - k:
            return 0
        return b - a - k - k

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1]
        j = 0
        o = 0
        self.assertEqual(s.smallestRangeI(i,j), o)

    def test_two(self):
        s = Solution()
        i = [0,10]
        j = 2
        o = 6
        self.assertEqual(s.smallestRangeI(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,3,6]
        j = 3
        o = 0
        self.assertEqual(s.smallestRangeI(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)