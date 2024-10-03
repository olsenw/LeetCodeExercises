# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an array of positive integers nums, remove the smallest subarray
    (possibly empty) such that the sum of the remaining elements is divisible by
    p. It is not allowed to remove the whole array.

    Return the length of the smallest subarray that would need to be removed or
    -1 if it is impossible.

    A subarray is defined as a contiguous block of elements in the array.
    '''
    def minSubarray_brute(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        if s < p:
            return -1
        if s % p == 0:
            return 0
        for i in range(1, len(nums) - 1):
            t = sum(nums[:i])
            if (s - t) % p == 0:
                return i
            for j in range(i, len(nums)):
                t += nums[j]
                t -= nums[j - i]
                if (s - t) % p == 0:
                    return i
        return -1

    def minSubarray_fails(self, nums: List[int], p: int) -> int:
        answer = len(nums)
        s = sum(nums)
        t = s % p
        map = {nums[0]%p:0}
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
            if t - (prefix[-1] % p) in map:
                return i - map[t - (prefix[-1] % p)]
            map[prefix[-1] % p] = i
        return -1 if answer == len(nums) else answer

    # based on LeetCode editorial
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        t = s % p
        if t == 0:
            return 0
        m = {0:-1}
        s = 0
        answer = len(nums)
        for i in range(len(nums)):
            s = (s + nums[i]) % p
            n = (s - t + p) % p
            if n in m:
                answer = min(answer, i - m[n])
            m[s] = i
        return -1 if answer == len(nums) else answer

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [3,1,4,2], 6
        o = 1
        self.assertEqual(s.minSubarray(*i), o)

    def test_two(self):
        s = Solution()
        i = [6,3,5,2], 9
        o = 2
        self.assertEqual(s.minSubarray(*i), o)

    def test_three(self):
        s = Solution()
        i = [1,2,3], 3
        o = 0
        self.assertEqual(s.minSubarray(*i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)