# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import bisect
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    A harmonious array is defined as an array where the difference between its
    maximum value and its minimum value is exactly 1.

    Given an integer array nums, return the length of its longest harmonious
    subsequence among all its possible subsequences.
    '''
    def findLHS(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for i,j in enumerate(nums):
            k = bisect.bisect(nums,j+1,i)
            # if k < len(nums) or nums[-1] == j+1:
            if nums[k - 1] == j + 1:
                answer = max(answer, k - i)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,3,2,2,5,2,3,7]
        o = 5
        self.assertEqual(s.findLHS(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2,3,4]
        o = 2
        self.assertEqual(s.findLHS(i), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,1]
        o = 0
        self.assertEqual(s.findLHS(i), o)

    def test_four(self):
        s = Solution()
        i = [1,2,2,1]
        o = 4
        self.assertEqual(s.findLHS(i), o)

    def test_five(self):
        s = Solution()
        i = [1,3,5,7,9,11,13,15,17]
        o = 0
        self.assertEqual(s.findLHS(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)