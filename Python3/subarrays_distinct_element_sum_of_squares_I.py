# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums.

    The distinct count of a subarray of nums is defined as:
    * Let nums[i..j] be a subarray of nums consisting of all the indices from i
      to j such that 0 <= i <= j < nums.length. Then the number of distinct
      values in nums[i..j] is called the distinct count of nums[i..j].
    
    Return the sum of the squares of distinct counts of all subarrays of nums.

    A subarray is a contiguous non-empty sequence of elements within an array.
    '''
    def sumCounts(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            values = set()
            for j in range(i, len(nums)):
                values.add(nums[j])
                answer += len(values) ** 2
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1]
        o = 15
        self.assertEqual(s.sumCounts(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1]
        o = 3
        self.assertEqual(s.sumCounts(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)