# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums. The absolute sum of a subarray [numsl, numsl+1,
    ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

    Return the maximum absolute sum of any (possibly empty) subarray of nums.
    '''
    # hints about Kadane's algorithm helpful
    # https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/#
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minAnswer = 0
        small = 0
        maxAnswer = 0
        large = 0
        for n in nums:
            large = max(large + n, n)
            maxAnswer = max(large, maxAnswer)
            small = min(small + n, n)
            minAnswer = min(small, minAnswer)
        return max(abs(minAnswer), maxAnswer)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,-3,2,3,-4]
        o = 5
        self.assertEqual(s.maxAbsoluteSum(i), o)

    def test_two(self):
        s = Solution()
        i = [2,-5,1,-4,3,-2]
        o = 8
        self.assertEqual(s.maxAbsoluteSum(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)