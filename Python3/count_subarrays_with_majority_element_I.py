# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer target.

    Return the number of subarrays of nums in which target is the majority
    element.

    The majority element of a subarray is the element that appears strictly more
    than half of the times in that subarray.
    '''
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            for j in range(i,-1,-1):
                c = 0
                for k in range(j,n):
                    if nums[k] == target:
                        c += 1
                    if k - j < 2 * c:
                        answer += 1
        return answer

    # brute force hint
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            c = 0
            for j in range(i,n):
                if nums[j] == target:
                    c += 1
                if j-i+1 < 2 * c:
                    answer += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,2,3]
        j = 2
        o = 5
        self.assertEqual(s.countMajoritySubarrays(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,1,1,1]
        j = 1
        o = 10
        self.assertEqual(s.countMajoritySubarrays(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3]
        j = 4
        o = 0
        self.assertEqual(s.countMajoritySubarrays(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)