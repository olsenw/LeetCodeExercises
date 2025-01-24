# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums that represents a circular array. Create a new
    array result of the same size following these rules:

    # For each index i (where 0 <= i < nums.length), perform the following
    independent actions:
    * If nums[i] > 0: Start at index i and move nums[i] steps to the right in
      the circular array. Set result[i] to the value of the index.
    * If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left
      in the circular array. Set result[i] to the value of the index.
    * If nums[i] == 0: Set result[i] to nums[i].

    Return the new array result.

    Note: Since nums is circular, moving past the last element wraps around to
    the beginning and moving before the first element wraps back to the end.
    '''
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            j = i + nums[i]
            result[i] = nums[j % n if j else -(j % n)]
        return result

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,-2,1,1]
        o = [1,1,1,3]
        self.assertEqual(s.constructTransformedArray(i), o)

    def test_two(self):
        s = Solution()
        i = [-1,4,-1]
        o = [-1,-1,4]
        self.assertEqual(s.constructTransformedArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)