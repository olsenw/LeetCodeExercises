# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums, where nums[i] is a digit between 0 and
    9 (inclusive).

    The triangular sum of nums is the value of the only element present in nums
    after the following process terminates.

    1. Let nums comprise of n elements. If n == 1, end the process. Otherwise,
       create a new 0-indexed integer array newNums of length n - 1.
    2. For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as
       (nums[i] + nums[i+1]) % 10, where % denotes modulo.
    3. Replace the array nums with newNums.
    4. Repeat the entire process starting from step 1.

    Return the triangular sum of nums.
    '''
    def triangularSum(self, nums: List[int]) -> int:
        for j in range(len(nums),0,-1):
            for i in range(j - 1):
                nums[i] = (nums[i] + nums[i+1]) % 10
        return nums[0]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 8
        self.assertEqual(s.triangularSum(i), o)

    def test_two(self):
        s = Solution()
        i = [5]
        o = 5
        self.assertEqual(s.triangularSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)