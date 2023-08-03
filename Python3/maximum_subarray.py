# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    given an integer array nums, find the subarray with the largest sum, and
    return its sum.
    '''
    # based on solution by archit91
    # https://leetcode.com/problems/maximum-subarray/solutions/1595195/c-python-7-simple-solutions-w-explanation-brute-force-dp-kadane-divide-conquer/
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for n in nums[1:]:
            prefix.append(n + max(prefix[-1], 0))
        return max(prefix)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = 15
        self.assertEqual(s.maxSubArray(i), o)

    def test_two(self):
        s = Solution()
        i = [-2,1,-3,4,-1,2,1,-5,4]
        o = 6
        self.assertEqual(s.maxSubArray(i), o)

    def test_three(self):
        s = Solution()
        i = [1]
        o = 1
        self.assertEqual(s.maxSubArray(i), o)

    def test_four(self):
        s = Solution()
        i = [5,4,-1,7,8]
        o = 23
        self.assertEqual(s.maxSubArray(i), o)

    def test_five(self):
        s = Solution()
        i = [-5,-4,-3,-4,-5]
        o = -3
        self.assertEqual(s.maxSubArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)