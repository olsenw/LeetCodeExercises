# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from itertools import accumulate
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums, find the leftmost middleIndex (ie, the
    smallest amongst all the possible ones).

    A middleIndex is an index where nums[0] + nums[1] + ... + 
    nums[middleIndex - 1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + 
    nums[nums.length-1].

    If middleIndex == 0, the left side sum is considered to be 0. Similarly, if
    middleIndex == nums.length - 1, the right side sum is considered to be 0.

    Return the leftmost middleIndex that satisfies the conditions, or -1 if
    there is no such index.
    '''
    def findMiddleIndex_passes(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        a,b = list(accumulate(nums)), list(accumulate(nums[::-1]))[::-1]
        if n > 1 and b[1] == 0:
            return 0
        for i in range(1,len(nums)-1):
            if a[i-1] == b[i+1]:
                return i
        if n > 1 and a[-2] == 0:
            return n-1
        return -1

    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        a = 0
        for i in range(n):
            s -= nums[i]
            if a == s:
                return i
            a += nums[i]
        return -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [2,3,-1,8,4]
        o = 3
        self.assertEqual(s.findMiddleIndex(i), o)

    def test_two(self):
        s = Solution()
        i = [1,-1,4]
        o = 2
        self.assertEqual(s.findMiddleIndex(i), o)

    def test_three(self):
        s = Solution()
        i = [2,5]
        o = -1
        self.assertEqual(s.findMiddleIndex(i), o)

    def test_four(self):
        s = Solution()
        i = [1]
        o = 0
        self.assertEqual(s.findMiddleIndex(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)