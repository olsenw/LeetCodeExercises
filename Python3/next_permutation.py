# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    A permutation of an array of integers is an arrangement of its
    members into a sequence or linear order.
    
    The next permutation of an array is the next lexicographically
    greater permutation of its integer. More formally, if all the
    permutations of the array are sorted in one container according to
    their lexicographical order, then the next permutation of that array
    is the permutation that follows it in the sorted container. If such
    arrangement is not possible, the array must be rearranged as the
    lowest possible order (ie sorted in ascending order).

    Given an array of integers nums, find the next permutation of nums.

    Do the replacement in place using constant 
    '''
    # based on leetcode solution
    # https://leetcode.com/problems/next-permutation/solution/
    # O(n) time
    # O(1) space
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # swap
            nums[i], nums[j] = nums[j], nums[i]
        # reverse
        nums[i+1:] = reversed(nums[i+1:])

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = [1,3,2]
        s.nextPermutation(i)
        self.assertEqual(i, o)

    def test_two(self):
        s = Solution()
        i = [3,2,1]
        o = [1,2,3]
        s.nextPermutation(i)
        self.assertEqual(i, o)

    def test_three(self):
        s = Solution()
        i = [1,1,5]
        o = [1,5,1]
        s.nextPermutation(i)
        self.assertEqual(i, o)

    def test_four(self):
        s = Solution()
        i = [5,4,2,1,3]
        o = [5,4,2,3,1]
        s.nextPermutation(i)
        self.assertEqual(i, o)

    def test_five(self):
        s = Solution()
        i = [5,1,4,3,2]
        o = [5,2,1,3,4]
        s.nextPermutation(i)
        self.assertEqual(i, o)

if __name__ == '__main__':
    unittest.main(verbosity=2)