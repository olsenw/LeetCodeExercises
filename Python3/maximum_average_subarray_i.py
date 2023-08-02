# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums consisting of n elements, and an integer k.

    Find a contiguous subarray whose length is equal to k that has the maximum
    average value and return this value. Any answer with a calculation error
    less that 10^-5 will be accepted.
    '''
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        s = sum(nums[:k])
        answer = s / k
        for i in range(k,n):
            s += nums[i]
            s -= nums[i - k]
            answer = max(answer, s / k)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,12,-5,-6,50,3]
        j = 4
        o = 12.75000
        self.assertEqual(s.findMaxAverage(i,j), o)

    def test_two(self):
        s = Solution()
        i = [5]
        j = 1
        o = 5.0
        self.assertEqual(s.findMaxAverage(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)