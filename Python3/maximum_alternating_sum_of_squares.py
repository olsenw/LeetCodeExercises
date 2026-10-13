# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. It is possible to rearrange the elements in any
    order.

    The alternating score of an array arr is defined as:
    * score = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...

    Return an integer denoting the maximum possible alternating score of nums
    after rearranging its elements.
    '''
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted((n * n for n in nums), reverse=True)
        i,j = 0, len(nums) - 1
        answer = 0
        while i < j:
            answer += nums[i]
            i += 1
            answer -= nums[j]
            j -= 1
        if i == j:
            answer += nums[i]
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = 12
        self.assertEqual(s.maxAlternatingSum(i), o)

    def test_two(self):
        s = Solution()
        i = [1,-1,2,-2,3,-3]
        o = 16
        self.assertEqual(s.maxAlternatingSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)