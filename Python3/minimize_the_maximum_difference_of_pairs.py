# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from functools import cache
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed integer array nums and an integer p. Find p pairs of
    indices of nums such that the maximum difference amongst all the pairs is
    minimized. Also, ensure no index appears more than once amongst the p paris.

    Note that for a pair of elements at the index i and j, the difference of
    this pair is | nums[i] - nums[j] |, where |x| represents the absolute value
    of x.

    Return the minimum maximum difference among all p pairs. The maximum of an
    empty set is defined to be zero.
    '''
    # based on LeetCode editorial
    # https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/editorial/
    # binary search + greedy
    # fyi has nothing to do with the hint...
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        # greedy count number of pairs with difference less than threshold
        # this is the important part
        def validate(threshold):
            count = 0
            i = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= threshold:
                    count += 1
                    i += 1
                i += 1
            return count
        # lower and upper bound of answer
        i,j = 0, nums[-1] - nums[0]
        # binary search
        while i < j:
            # calc this way to avoid overflow
            k = i + (j - i) // 2
            # found more pairs than needed move right bound
            if validate(k) >= p:
                j = k
            # found less pairs than needed move left bound
            else:
                i = k + 1
        return i

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [10,1,2,7,1,3]
        j = 2
        o = 1
        self.assertEqual(s.minimizeMax(i,j), o)

    def test_two(self):
        s = Solution()
        i = [4,2,1,2]
        j = 1
        o = 0
        self.assertEqual(s.minimizeMax(i,j), o)

    def test_three(self):
        s = Solution()
        i = [2,2,2,3]
        j = 2
        o = 1
        self.assertEqual(s.minimizeMax(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)