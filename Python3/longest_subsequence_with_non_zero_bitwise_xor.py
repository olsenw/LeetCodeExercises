# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums.

    Return the length of the longest subsequence in nums whose bitwise XOR is
    non-zero. If no such subsequence exists, return 0.
    '''
    # can go from 0 XOR to non-zero XOR be extending subsequence
    def longestSubsequence_fails(self, nums: List[int]) -> int:
        answer = 0
        running = 0
        i = 0
        for j in range(len(nums)):
            running ^= nums[j]
            pass
            while i < j and running == 0:
                running ^= nums[i]
                i += 1
            answer = max(answer, j - i + 1)
        return answer

    def longestSubsequence_fails(self, nums: List[int]) -> int:
        answer = 0
        seen = dict()
        running = 0
        for i in range(len(nums)):
            running ^= nums[i]
            if running not in seen:
                seen[running] = i+1
            pass
            for v,j in seen.items():
                if running ^ v != 0:
                    answer = max(answer, i - j + 1)
        return answer

    # based on hints
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n
        if xor == 0:
            return 0 if all(n == 0 for n in nums) else len(nums) - 1
        return len(nums)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,3]
        o = 2
        self.assertEqual(s.longestSubsequence(i), o)

    def test_two(self):
        s = Solution()
        i = [2,3,4]
        o = 3
        self.assertEqual(s.longestSubsequence(i), o)

    def test_three(self):
        s = Solution()
        i = [7,6,1,9]
        o = 4
        self.assertEqual(s.longestSubsequence(i), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)