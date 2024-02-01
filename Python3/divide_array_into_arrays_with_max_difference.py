# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums of size n and a positive integer k.

    Divide the array into one or more arrays of size 3 satisfying the following
    conditions:
    * Each element of nums should be in exactly one array.
    * The difference between any two elements in one array is less than or equal
      to k.
    
    Return a 2D array containing all the arrays. If it is impossible to satisfy
    the conditions, return an empty array. And if there are multiple different
    answers, return any of them.
    '''
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        answer = []
        if n % 3:
            return []
        for i in range(0, n, 3):
            if nums[i+2] - nums[i] > k:
                return []
            answer.append(nums[i:i+3])
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,4,8,7,9,3,5,1]
        j = 2
        o = [[1,1,3],[3,4,5],[7,8,9]]
        self.assertEqual(s.divideArray(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,3,3,2,7,3]
        j = 3
        o = []
        self.assertEqual(s.divideArray(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)