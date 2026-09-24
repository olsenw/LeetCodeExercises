# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    Return the smallest index i such that the sum of the digits of nums[i] is
    equal to i.

    If no such index exists, return -1
    '''
    # this is first index equals value
    def smallestIndex_incorrect(self, nums: List[int]) -> int:
        for i,j in enumerate(nums):
            if i == j:
                return i
        return -1

    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(num:int) -> int:
            answer = 0
            while num:
                answer += num % 10
                num //= 10
            return answer
        for i,j in enumerate(nums):
            if i == digitSum(j):
                return i
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2]
        o = 2
        self.assertEqual(s.smallestIndex(i), o)

    def test_two(self):
        s = Solution()
        i = [1,10,11]
        o = 1
        self.assertEqual(s.smallestIndex(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3]
        o = -1
        self.assertEqual(s.smallestIndex(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)