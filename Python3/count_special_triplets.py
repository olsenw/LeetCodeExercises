# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    A special triplet is defined as a triplet of indices (i , j, k) such that:
    * 0 <= i < j < k < n, where n = nums.length
    * nums[i] == nums[j] * 2
    * nums[k] == nums[j] * 2

    Return the total number of special triplets in the array.

    Since the answer may be large, return it modulo 10^9 + 7.
    '''
    def specialTriplets(self, nums: List[int]) -> int:
        m = 10**9 + 7
        left = Counter()
        answer = 0
        right = Counter(nums)
        for n in nums:
            right[n] -= 1
            answer = (answer + (((left[2 * n] % m) * (right[2 * n] % m)) % m)) % m
            left[n] += 1
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [6,3,6]
        o = 1
        self.assertEqual(s.specialTriplets(i), o)

    def test_two(self):
        s = Solution()
        i = [0,1,0,0]
        o = 1
        self.assertEqual(s.specialTriplets(i), o)

    def test_three(self):
        s = Solution()
        i = [8,4,2,8,4]
        o = 2
        self.assertEqual(s.specialTriplets(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)