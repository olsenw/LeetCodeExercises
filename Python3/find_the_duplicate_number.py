# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List

class Solution:
    '''
    Given an array of integers nums containing n+1 integers where each
    integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this number.

    Solve the problem without modifying nums and using constant space.

    Constraints:
    * 1 <= n <= 10^5
    * nums.length == n + 1
    * 1 <= nums[i] <= n
    * All integers in nums appear only once except for precisely one
      integer which appears two or more times. (IMPORTANT duplicate
      number can occur more than twice in nums)
    '''
    # based on leetcode solution
    # https://leetcode.com/problems/find-the-duplicate-number/solution/
    # Floyd's Tortoise and Hare (cycle detection)
    def findDuplicate_floyd(self, nums: List[int]) -> int:
        # i is the tortoise and j is the hare
        i = j = nums[0]
        # find cycle start
        while True:
            i = nums[i]
            j = nums[nums[j]]
            if i == j:
                break
        # find duplicate
        i = nums[0]
        while i != j:
            i = nums[i]
            j = nums[j]
        return j

    # based on leetcode solution
    # https://leetcode.com/problems/find-the-duplicate-number/solution/
    # sum of set bits
    # funky bit manipulation magic
    def findDuplicate_bits(self, nums: List[int]) -> int:
        d = 0
        # largest possible number in nums (from problem constraints)
        n = len(nums) - 1
        # count number of times bit is set
        for b in range(n.bit_length()):
            # bit mask
            m = 1 << b
            # bit count assuming elements 1 to n comprise nums
            bc = 0
            # bit count of actual numbers in nums
            nc = 0
            # check if given bit is set in each element nums
            for i in range(n + 1):
                # check if index has bit set
                if i & m:
                    bc += 1
                # check if element has bit set
                if nums[i] & m:
                    nc += 1
            # set bit in duplicate (only if positive)
            if nc - bc > 0:
                d |= m
        return d

    # This solution makes the assumption that a single number is 
    # repeated exactly once... however the duplicate number can be
    # repeated multiple times according to the problem constraints.
    def findDuplicate_incorrect(self, nums: List[int]) -> int:
        n = len(nums) - 1
        s = n * (n + 1) // 2
        return sum(nums) - s

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,4,2,2]
        o = 2
        self.assertEqual(s.findDuplicate_floyd(i), o)
        self.assertEqual(s.findDuplicate_bits(i), o)

    def test_two(self):
        s = Solution()
        i = [3,1,3,4,2]
        o = 3
        self.assertEqual(s.findDuplicate_floyd(i), o)
        self.assertEqual(s.findDuplicate_bits(i), o)

    def test_three(self):
        s = Solution()
        i = [2,2,2,2,2]
        o = 2
        self.assertEqual(s.findDuplicate_floyd(i), o)
        self.assertEqual(s.findDuplicate_bits(i), o)

    def test_four(self):
        s = Solution()
        i = [4,3,1,4,2]
        o = 4
        self.assertEqual(s.findDuplicate_floyd(i), o)
        self.assertEqual(s.findDuplicate_bits(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)