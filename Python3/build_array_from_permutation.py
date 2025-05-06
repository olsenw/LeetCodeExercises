# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a zero-based permutation nums (o-indexed) build an array ans of the
    same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and
    return it.

    A zero-based permutation nums is an array of distinct integers from 0 to
    nums.length - 1 (inclusive).
    '''
    # O(n) space
    def buildArray_lazy(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        for i in range(len(nums)):
            answer[i] = nums[nums[i]]
        return answer

    # O(1) space
    # based on Leetcode editorial
    # https://leetcode.com/problems/build-array-from-permutation/editorial/?envType=daily-question&envId=2025-05-06
    # works because of the upper bound
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] += 1000 * (nums[nums[i]] % 1000)
        for i in range(n):
            nums[i] //= 1000
        return nums

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [0,2,1,5,3,4]
        o = [0,1,2,4,5,3]
        self.assertEqual(s.buildArray(i), o)

    def test_two(self):
        s = Solution()
        i = [5,0,1,2,3,4]
        o = [4,5,0,1,2,3]
        self.assertEqual(s.buildArray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)