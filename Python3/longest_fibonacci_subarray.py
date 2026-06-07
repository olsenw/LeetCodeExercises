# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers nums.

    A Fibonacci array is a contiguous sequence whose third and subsequent terms
    each equal the sum of the two preceding terms.

    Return the length of longest Fibonacci subarray in nums.

    Note: Subarrays of length 1 or 2 are always Fibonacci.
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        answer = 2
        a = 2
        for i in range(2,len(nums)):
            if nums[i] == nums[i-1] + nums[i-2]:
                a += 1
            else:
                answer = max(answer, a)
                a = 2
        return max(answer, a)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,1,1,1,2,3,5,1]
        o = 5
        self.assertEqual(s.longestSubarray(i), o)

    def test_two(self):
        s = Solution()
        i = [5,2,7,9,16]
        o = 5
        self.assertEqual(s.longestSubarray(i), o)

    def test_three(self):
        s = Solution()
        i = [1000000000,1000000000,1000000000]
        o = 2
        self.assertEqual(s.longestSubarray(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)