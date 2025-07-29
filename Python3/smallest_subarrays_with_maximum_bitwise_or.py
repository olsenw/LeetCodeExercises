# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given a 0-indexed array nums of length n, consisting of non-negative
    integers. For each index i from 0 to n - 1, determine the size of the
    minimum sized non-empty subarray of nums starting at i (inclusive) that has
    the maximum possible bitwise OR.

    The bitwise OR of an array is the bitwise OR of all the numbers in it.

    Return an integer array answer of size n where answer[i] is the length of
    the minimum sized subarray starting at i with maximum bitwise OR.

    A subarray is a contiguous non-empty sequence of elements within an array.
    '''
    # brute force O(n^2)
    def smallestSubarrays_brute(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            index = i
            best = nums[i]
            a = nums[i]
            for j in range(i, len(nums)):
                a |= nums[j]
                if a > best:
                    best = a
                    index = j
            answer.append(index - i + 1)
        return answer

    # based on hints
    # index tracking wrong (should be right to left instead)
    def smallestSubarrays_fails(self, nums: List[int]) -> List[int]:
        a = 0
        for n in nums:
            a |= n
        indices = [len(nums) - 1 if a & (1 << i) > 0 else 0 for i in range(32)]
        answer = []
        for i in range(len(nums) - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j) > 0:
                    indices[j] = i
            answer.append(max(indices) - i + 1)
        return answer[::-1]

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        answer = []
        indices = [0] * 32
        for i in range(len(nums)-1,-1,-1):
            for j in range(32):
                if nums[i] & (1 << j) > 0:
                    indices[j] = i
            # note non-empty subarray has minimum length of 1
            answer.append(max(max(indices) - i + 1,1))
        return answer[::-1]

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,0,2,1,3]
        o = [3,3,2,2,1]
        self.assertEqual(s.smallestSubarrays(i), o)

    def test_two(self):
        s = Solution()
        i = [1,2]
        o = [2,1]
        self.assertEqual(s.smallestSubarrays(i), o)

    def test_three(self):
        s = Solution()
        i = [4,0,5,6,3,2]
        o = [4,3,2,2,1,1]
        self.assertEqual(s.smallestSubarrays(i), o)

    def test_four(self):
        s = Solution()
        i = [1,0]
        o = [1,1]
        self.assertEqual(s.smallestSubarrays(i), o)

    def test_five(self):
        s = Solution()
        i = [1,0,0,0,0,0]
        o = [1,1,1,1,1,1]
        self.assertEqual(s.smallestSubarrays(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)