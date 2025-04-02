# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums.

    Return the maximum value over all triplets of indices (i, j, k) such that
    i < j < k. If all such triplets have a negative value, return 0.

    The value of a triplet of indices (i,j,k) is equal to
    (nums[i] - nums[j] * nums[k]).
    '''
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        last = [nums[0]] * n
        next = [nums[-1]] * n
        answer = 0
        for i in range(1,n):
            last[i] = max(nums[i], last[i-1])
        for i in range(n-2, 0, -1):
            next[i] = max(nums[i], next[i+1])
        for i in range(1, n-1):
            answer = max((last[i-1] - nums[i]) * next[i+1], answer)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [12,6,1,2,7]
        o = 77
        self.assertEqual(s.maximumTripletValue(i), o)

    def test_two(self):
        s = Solution()
        i = [1,10,3,4,19]
        o = 133
        self.assertEqual(s.maximumTripletValue(i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3]
        o = 0
        self.assertEqual(s.maximumTripletValue(i), o)

    def test_four(self):
        s = Solution()
        i = [6,11,12,12,7,9,2,11,12,4,19,14,16,8,16]
        o = 190
        self.assertEqual(s.maximumTripletValue(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)