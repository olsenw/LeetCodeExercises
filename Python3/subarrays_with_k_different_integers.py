# needed for python unit testings
# https://docs.python.org/3/library/unittest.html
from collections import Counter, defaultdict
import unittest

# required for type hinting
# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
from typing import List, Dict, Set, Optional

class Solution:
    '''
    Given an integer array nums and an integer k, return the number of good
    subarrays of nums.

    A good array is an array where the number of different integers in that
    array is exactly k.

    A subarray is a contiguous part of an array.
    '''
    def subarraysWithKDistinct_wrong(self, nums: List[int], k: int) -> int:
        answer = 0
        c = Counter()
        i = 0
        for j in range(len(nums)):
            c[nums[j]] += 1
            if len(c) == k:
                answer += 1
            if len(c) > k:
                c[nums[j]] -= 1
                while len(c) == k:
                    c[nums[i]] -= 1
                    i += 1
                    if len(c) == k:
                        answer += 1
                c[nums[j]] -= 1
        return answer

    def subarraysWithKDistinct_wrong_again(self, nums: List[int], k: int) -> int:
        answer = 0
        c = defaultdict(int)
        i = 0
        for j in range(len(nums)):
            c[nums[j]] += 1
            a = c.copy()
            b = i
            while b < j and len(a) == k:
                answer += 1
                a[nums[b]] -= 1
                if a[nums[b]] == 0:
                    del a[nums[b]]
                b += 1
            while i < j and len(c) > k:
                c[nums[i]] -= 1
                if c[nums[i]] == 0:
                    del c[nums[i]]
                i += 1
        return answer

    def subarraysWithKDistinct_brute(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0
        for j in range(n):
            c = Counter()
            for i in range(j, -1, -1):
                c[nums[i]] += 1
                if len(c) == k:
                    answer += 1
        return answer

    # based on solution by leetcode
    # https://leetcode.com/problems/subarrays-with-k-different-integers/editorial/?envType=daily-question&envId=2024-03-30
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            f = defaultdict(int)
            i = 0
            answer = 0
            for j in range(len(nums)):
                f[nums[j]] += 1
                while len(f) > k:
                    f[nums[i]] -= 1
                    if f[nums[i]] == 0:
                        del f[nums[i]]
                    i += 1
                answer += j - i + 1
            return answer
        return helper(nums, k) - helper(nums, k-1)

class UnitTesting(unittest.TestCase):
    def test_one(self):
        s = Solution()
        i = [1,2,1,2,3]
        j = 2
        o = 7
        self.assertEqual(s.subarraysWithKDistinct(i,j), o)

    def test_two(self):
        s = Solution()
        i = [1,2,1,3,4]
        j = 3
        o = 3
        self.assertEqual(s.subarraysWithKDistinct(i,j), o)

    def test_three(self):
        s = Solution()
        i = [1,1,1,3,1,1,4]
        j = 2
        o = 13
        self.assertEqual(s.subarraysWithKDistinct(i,j), o)

if __name__ == '__main__':
    unittest.main(verbosity=2)