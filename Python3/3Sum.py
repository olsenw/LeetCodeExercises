# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an integer array nums, return all the triplets
    [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and
    nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
    '''
    # O(n^3)
    def threeSum_brute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        a,b,c = None,None,None
        for i in range(len(nums)):
            if nums[i] == a:
                continue
            a = nums[i]
            b = None
            for j in range(i + 1, len(nums)):
                if nums[j] == b:
                    continue
                b = nums[j]
                c = None
                for k in range(j + 1, len(nums)):
                    if nums[k] == c:
                        continue
                    c = nums[k]
                    if nums[i] + nums[j] + nums[k] == 0:
                        answer.append([nums[i],nums[j],nums[k]])
        return answer

    # O(n^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i + 1, len(nums) - 1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t == 0:
                    answer.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif t < 0:
                    l += 1
                else:
                    r -= 1
        return answer


class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [-1,0,1,2,-1,-4]
        o = [[-1,-1,2],[-1,0,1]]
        self.assertEqual(s.threeSum(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,1]
        o = []
        self.assertEqual(s.threeSum(i), o)

    def test_three(self):
        s = Solution()
        i = [0,0,0]
        o = [[0,0,0]]
        self.assertEqual(s.threeSum(i), o)

    def test_four(self):
        s = Solution()
        i = [-1,-1,2,-1,-1]
        o = [[-1,-1,2]]
        self.assertEqual(s.threeSum(i), o)

    def test_five(self):
        s = Solution()
        i = [0,0,0,0]
        o = [[0,0,0]]
        self.assertEqual(s.threeSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)