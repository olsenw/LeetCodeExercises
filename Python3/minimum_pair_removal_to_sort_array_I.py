# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array nums, perform the following operation any number of times:
    * Select the adjacent pair with the minimum sum in nums. If multiple such
      pairs exist, choose the leftmost one.
    * Replace the pair with their sum.

    Return the minimum number of operations needed to make the array
    non-decreasing.

    An array is said to be non-decreasing if each element greater than to equal
    to its previous element (it if exists).
    '''
    # solved different problem
    # incorrect assumption to remove only non-decreasing pairs
    def minimumPairRemoval_incorrect(self, nums: List[int]) -> int:
        def replace(nums: List[int], idx1:int, idx2:int):
            s = nums[idx1] + nums[idx2]
            return nums[:idx1] + [s] + nums[idx2+1:]
        answer = 0
        op = True
        while op:
            op = False
            s,x,y = 10000,0,0
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1] and nums[i] + nums[i+1] < s:
                    s,x,y = nums[i] + nums[i+1], i, i+1
                    op = True
            if op:
                nums = replace(nums, x, y)
                answer += 1
        return answer

    def minimumPairRemoval(self, nums: List[int]) -> int:
        def replace(nums: List[int], idx1:int, idx2:int):
            s = nums[idx1] + nums[idx2]
            return nums[:idx1] + [s] + nums[idx2+1:]
        def nonDecreasing(nums: List[int]) -> bool:
            return any(nums[i] > nums[i+1] for i in range(len(nums) - 1))
        def smallestPair(nums: List[int]) -> List[int]:
            s,x,y = float('inf'),0,0
            for i in range(len(nums) - 1):
                if nums[i] + nums[i+1] < s:
                    s,x,y = nums[i] + nums[i+1], i, i+1
            return [x,y]
        answer = 0
        while nonDecreasing(nums):
            answer += 1
            x,y = smallestPair(nums)
            nums = replace(nums, x, y)
        return answer
        
class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [5,2,3,1]
        o = 2
        self.assertEqual(s.minimumPairRemoval(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,2]
        o = 0
        self.assertEqual(s.minimumPairRemoval(i), o)

    def test_three(self):
        s = Solution()
        i = [2,2,-1,3,-2,2,1,1,1,0,-1]
        o = 9
        self.assertEqual(s.minimumPairRemoval(i), o)

    def test_four(self):
        s = Solution()
        i = [1000,999,998,997,996,995,994,993,992,991,990,989,988,987,986,985,984,983,982,981,980,979,978,977,976,975,974,973,972,971,970,969,968,967,966,965,964,963,962,961,960,959,958,957,956,955,954,953,952,951]
        o = 48
        self.assertEqual(s.minimumPairRemoval(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)