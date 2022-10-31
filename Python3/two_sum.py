# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of integers nums and an integer target, return indices of the
    two numbers such that they add up to target.

    It is assumed that each input has exactly one solution and it is invalid to
    use the same element twice.
    '''
    # O(n^2) time
    def twoSum_tle(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i,j]
        # unreachable if valid test case
        return [-1,-1]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # maps a value to another value
        # in this case the value of nums[i] to its index i
        h = {nums[0]:0}
        # go through indices of array
        for i in range(1, len(nums)):
            if target - nums[i] in h:
                return [h[target - nums[i]], i]
            h[nums[i]] = i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,7,11,15]
        j = 9
        o = [0,1]
        self.assertEqual(s.twoSum(i,j), o)

    def test_two(self):
        s = Solution()
        i = [3,2,4]
        j = 6
        o = [1,2]
        self.assertEqual(s.twoSum(i,j), o)

    def test_three(self):
        s = Solution()
        i = [3,3]
        j = 6
        o = [0,1]
        self.assertEqual(s.twoSum(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)