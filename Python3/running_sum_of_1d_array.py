# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given the array nums. The running sum of an array is defined as
    runningSum[i] = sum(nums[0], ... , nums[i]).

    Return the running sum of nums.
    '''
    def runningSum(self, nums: List[int]) -> List[int]:
        a = [0] * len(nums)
        a[0] = nums[0]
        for i in range(1,len(nums)):
            a[i] = nums[i] + a[i-1]
        return a

    def runningSum_reuse(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = [1,3,6,10]
        self.assertEqual(s.runningSum(i), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1,1]
        o = [1,2,3,4,5]
        self.assertEqual(s.runningSum(i), o)

    def test_three(self):
        s = Solution()
        i = [3,1,2,10,1]
        o = [3,4,6,16,17]
        self.assertEqual(s.runningSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)