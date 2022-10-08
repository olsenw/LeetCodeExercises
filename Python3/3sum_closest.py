# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums of length n and an integer target, find three
    integers in nums such that the sum is closest to target.
    
    Return the sum of the three integers.
    
    It is assumed that each test case has a single solution.
    '''
    # O(n^3) time
    def threeSumClosest_brute(self, nums: List[int], target: int) -> int:
        best = float('inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1,len(nums)):
                    curr = nums[i] + nums[j] + nums[k]
                    if abs(curr - target) < abs(best - target):
                        best = curr
        return best

    # O(n^2) time
    def threeSumClosest_fails(self, nums: List[int], target: int) -> int:
        nums.sort()
        a,b = 0, float('inf')
        i,j = 0, len(nums) - 1
        while i < j:
            c = nums[i] + nums[j] - target
            for k in range(i+1,j):
                if abs(c + nums[k]) < abs(b):
                    a = nums[i] + nums[j] + nums[k]
                    b = c + nums[k]
            # this choice here is wrong...
            if b < 0:
                i += 1
            else:
                j -= 1
        return a

    # inspired by discussion post by Google
    # https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution
    # additional inspiration from comments (niuniu1397, juleslemenestrel)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        r = sum(nums[:3])
        for i in range(0, len(nums)):
            # skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                c = nums[i] + nums[j] + nums[k]
                if c < target:
                    j += 1
                elif c > target:
                    k -= 1
                else:
                    return target
            if abs(c - target) < abs(r - target):
                    r = c
        return r

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-1,2,1,-4]
        j = 1
        o = 2
        self.assertEqual(s.threeSumClosest(i,j), o)

    def test_two(self):
        s = Solution()
        i = [0,0,0]
        j = 1
        o = 0
        self.assertEqual(s.threeSumClosest(i,j), o)

    def test_three(self):
        s = Solution()
        i = [-100,-98,-2,-1]
        j = -101
        o = -101
        self.assertEqual(s.threeSumClosest(i,j), o)

    def test_four(self):
        s = Solution()
        i = [4,0,5,-5,3,3,0,-4,-5]
        j = -2
        o = -2
        self.assertEqual(s.threeSumClosest(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)