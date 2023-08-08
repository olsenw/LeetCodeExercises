# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums, return an array answer such that answer[i] is
    equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
    integer.

    The algorithm must run in O(n) time and may not use the division operation.
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        suffix = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]
        answer = [1] * n
        for i in range(n):
            answer[i] = prefix[i] * suffix[i+1]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4]
        o = [24,12,8,6]
        self.assertEqual(s.productExceptSelf(i), o)

    def test_two(self):
        s = Solution()
        i = [-1,1,0,-3,3]
        o = [0,0,9,0,0]
        self.assertEqual(s.productExceptSelf(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)