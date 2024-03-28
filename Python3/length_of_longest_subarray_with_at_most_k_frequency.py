# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k.

    The frequency of an element x is the number of times it occurs in an array.

    An array is called good if the frequency of each element in this array is
    less than or equal to k.

    Return the length of the longest good subarray of nums.

    A subarray is a contiguous non-empty sequence of elements within an array.
    '''
    def maxSubarrayLength_time_limit_exceeded(self, nums: List[int], k: int) -> int:
        answer = 0
        c = Counter()
        i = 0
        for j in range(len(nums)):
            c[nums[j]] += 1
            while i < j and any(c[v] > k for v in c):
                c[nums[i]] -= 1
                i += 1
            answer = max(answer, j - i + 1)
        return answer

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        answer = 1
        c = Counter()
        i = 0
        for j in range(len(nums)):
            c[nums[j]] += 1
            while c[nums[j]] > k:
                c[nums[i]] -= 1
                i += 1
            answer = max(answer, j - i + 1)
        return answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3,1,2,3,1,2]
        j = 2
        o = 6
        self.assertEqual(s.maxSubarrayLength(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,1,2,1,2,1,2]
        j = 1
        o = 2
        self.assertEqual(s.maxSubarrayLength(i,j), o)

    def test_three(self):
        s = Solution()
        i = [5,5,5,5,5,5,5]
        j = 4
        o = 4
        self.assertEqual(s.maxSubarrayLength(i,j), o)

    def test_four(self):
        s = Solution()
        i = [2,2,3]
        j = 1
        o = 2
        self.assertEqual(s.maxSubarrayLength(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)