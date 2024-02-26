# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array nums of size n consisting of non-negative integers.

    Apply n - 1 operations to this array where, in the ith operation (0-indexed)
    apply the following on the ith element of nums:
    * if nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i+1] to
      0. Otherwise skip this operation.
    
    After performing all the operations, shift all the 0's to the end of the
    array.

    Return the resulting array.

    Note that the operations are applied sequentially, not all at once.
    '''
    def applyOperations(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i]:
                answer.append(nums[i])
        if nums[-1]:
            answer.append(nums[-1])
        if len(answer) < len(nums):
            answer.extend([0] * (len(nums) - len(answer)))
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,1,1,0]
        o = [1,4,2,0,0,0]
        self.assertEqual(s.applyOperations(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1]
        o = [1,0]
        self.assertEqual(s.applyOperations(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)