# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 2D integer array nums, return all elements of nums in diagonal order
    as show in the images on LeetCode.
    '''
    def findDiagonalOrder_tle(self, nums: List[List[int]]) -> List[int]:
        answer = []
        m = max(len(n) for n in nums)
        for i in range(m*len(nums)):
            j = 0
            for k in range(i, -1, -1):
                if k < len(nums) and j < len(nums[k]):
                    answer.append(nums[k][j])
                j += 1
        return answer

    def findDiagonalOrder_wrong(self, nums: List[List[int]]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            j = 0
            for k in range(i, -1, -1):
                if j < len(nums[k]):
                    answer.append(nums[k][j])
                j += 1
        for i in range(1, len(nums[-1])):
            j = i
            for k in range(len(nums)-1,-1,-1):
                if j < len(nums[k]):
                    answer.append(nums[k][j])
                j += 1
        return answer

    # based on leetcode hint    
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        values = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                values.append((i+j,-i,j))
        values.sort()
        return [nums[-j][k] for i,j,k in values]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [[1,2,3],[4,5,6],[7,8,9]]
        o = [1,4,2,7,5,3,8,6,9]
        self.assertEqual(s.findDiagonalOrder(i), o)

    def test_two(self):
        s = Solution()
        i = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
        o = [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
        self.assertEqual(s.findDiagonalOrder(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)