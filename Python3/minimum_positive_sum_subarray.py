# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and two integers l and r. Find the minimum sum
    of a subarray whose size is between l and r (inclusive) and whose sum is
    greater than 0.

    Return the minimum sum of a such a subarray. If no such subarray exists,
    return -1.

    A subarray is a contiguous non-empty sequence of elements within an array.
    '''
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        answer = float('inf')
        for i in range(l,r+1):
            s = sum(nums[:i])
            if s > 0:
                answer = min(answer, s)
            for j in range(i, len(nums)):
                s -= nums[j-i]
                s += nums[j]
                if s > 0:
                    answer = min(answer, s)
        return answer if answer < float('inf') else -1

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1, 2, 3, 4], 2, 4
        o = 3
        self.assertEqual(s.minimumSumSubarray(*i), o)

    def test_two(self):
        s = Solution()
        i = [-2, 2, -3, 1], 2, 3
        o = -1
        self.assertEqual(s.minimumSumSubarray(*i), o)

    def test_three(self):
        s = Solution()
        i = [3, -2, 1, 4], 2, 3
        o = 1
        self.assertEqual(s.minimumSumSubarray(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)