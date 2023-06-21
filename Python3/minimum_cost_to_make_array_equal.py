# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given two 0-indexed arrays nums and cost consisting each of n positive
    integers.

    The following operation can be done any number of times:
    * Increase or decrease any element of the array nums by 1.

    The cost of doing one operation on the ith element is cost[i].

    Return the minimum total cost such that all the elements of the array nums
    become equal.
    '''
    # hint is that becoming a target value is optimal
    def minCost_brute(self, nums: List[int], cost: List[int]) -> int:
        def count(target):
            return sum(abs(target - nums[i]) * cost[i] for i in range(len(nums)))
        return min(count(nums[i]) for i in range(len(nums)))

    # right idea needed help with how to binary search
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        keys = sorted(set(nums))
        def count(target):
            return sum(abs(target - nums[i]) * cost[i] for i in range(len(nums)))
        a = count(nums[0])
        i,j = min(nums), max(nums)
        while i < j:
            k = (i + j) // 2
            c1, c2 = count(k), count(k + 1)
            a = min(c1, c2)
            if c1 > c2:
                i = k + 1
            else:
                j = k
        return a

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,5,2]
        j = [2,3,1,14]
        o = 8
        self.assertEqual(s.minCost(i,j), o)

    def test_two(self):
        s = Solution()
        i = [2,2,2,2,2]
        j = [4,2,8,1,3]
        o = 0
        self.assertEqual(s.minCost(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)