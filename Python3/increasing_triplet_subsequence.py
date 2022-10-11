# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from math import inf
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums, return true if there exists a triple of indices
    (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
    indices exist, return false.
    '''
    # does not allow for small sequence if larger number passed
    def increasingTriplet_fails(self, nums: List[int]) -> bool:
        found, count = float('-inf'), 3
        for n in nums:
            if n > found:
                count -= 1
                if count == 0:
                    return True
                found = n
        return False

    # does not hold constraint of index i < j < k
    def increasingTriplet_fails2(self, nums: List[int]) -> bool:
        a, b = min(nums), max(nums)
        return any(a < n < b for n in nums)

    # O(3n) time
    # O(2n) space
    def increasingTriplet_slow(self, nums: List[int]) -> bool:
        small = [0] * len(nums)
        small[0] = nums[0]
        for i in range(1, len(nums)):
            small[i] = min(small[i-1], nums[i])
        large = [0] * len(nums)
        large[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            large[i] = max(large[i+1], nums[i])
        for i in range(1,len(nums)-1):
            if small[i-1] < nums[i] < large[i+1]:
                return True
        return False

    # O(2n) time
    # O(n) space
    def increasingTriplet_improved(self, nums: List[int]) -> bool:
        m = nums[0]
        large = [0] * len(nums)
        large[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            large[i] = max(large[i+1], nums[i])
        for i in range(1,len(nums)-1):
            if m < nums[i] < large[i+1]:
                return True
            m = min(m, nums[i])
        return False

    # O(n^2) time
    # O(1) space
    def increasingTriplet_brute(self, nums: List[int]) -> bool:
        for i in range(1,len(nums)-1):
            if min(nums[:i]) < nums[i] < max(nums[i+1:]):
                return True
        return False

    # O(n^2) time
    # O(1) space
    def increasingTriplet_brute_improved(self, nums: List[int]) -> bool:
        m = nums[0]
        for i in range(1,len(nums)-1):
            if m < nums[i] < max(nums[i+1:]):
                return True
            m = min(m, nums[i])
        return False

    # based on discussion post by warrenruud
    # https://leetcode.com/problems/increasing-triplet-subsequence/discuss/2688195/python-3-oror-6-lines-one-pass-wexplanation-oror-TM%3A-9850
    # O(n) time
    # O(1) space
    def increasingTriplet_greedy(self, nums: List[int]) -> bool:
        a,b = inf, inf
        for c in nums:
            if b < c:
                return True
            if c <= a:
                a = c
            else:
                b = c
        return False

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,4,5]
        o = True
        self.assertEqual(s.increasingTriplet(i), o)

    def test_two(self):
        s = Solution()
        i = [5,4,3,2,1]
        o = False
        self.assertEqual(s.increasingTriplet(i), o)

    def test_three(self):
        s = Solution()
        i = [2,1,5,0,4,6]
        o = True
        self.assertEqual(s.increasingTriplet(i), o)

    def test_four(self):
        s = Solution()
        i = [5,4,1,2,3]
        o = True
        self.assertEqual(s.increasingTriplet(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)